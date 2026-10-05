# Write movement's FreeMoCap star-jump recording with FreeMoCap v1's own writers.
#
#   python scripts/freemocap_star_jump.py <freemocap clone> <tag> <recording> <out dir>
#
# <recording> is recording_15_30_36_gmt+1/ from movement's
# FreeMoCap_star-jump_session-folder.zip (CC BY 4.0, shared by Max Staras,
# Sainsbury Wellcome Centre): https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data
# or https://gin.g-node.org/neuroinformatics/movement-test-data, poses/. Its
# output_data/ holds the arrays FreeMoCap (about v1.6) saved after processing:
# the post-processed skeleton, the centres of mass and the reprojection errors.
#
# The script runs the last two steps of FreeMoCap's processing pipeline
# (process_recording_folder() in
# core_processes/process_motion_capture_videos/process_recording_folder.py) on
# those arrays, with FreeMoCap's own modules taken unchanged from the clone at
# <tag>:
#
# * split_and_save() (core_processes/post_process_skeleton_data/split_and_save.py)
#   writes the per-model wide files, output_data/mediapipe_body_3d_xyz.csv and
#   so on, from the skeleton array, as save_data() does;
# * DataSaver.save_all() (data_layer/data_saver/data_saver.py, reading the folder
#   with data_loader.py) writes <recording>_by_frame.csv and
#   <recording>_by_trajectory.csv.
#
# The model info is skellytracker's own MediapipeModelInfo, from skellytracker
# 2025.10.1024 (the version FreeMoCap v1.7.3 and v1.8.2 pin), installed without its
# dependencies: MediaPipe itself is replaced by the landmark names and face
# point count that model info reads from it, and the body names are checked
# against the recording's own wide body file, which FreeMoCap wrote from
# MediaPipe. Of path_getters.py only the three folder lookups the loader calls
# are taken, since the rest needs the GUI.
#
# The 478 face mesh points are left out of the tidy files to keep them small:
# the wide face file split_and_save() writes is deleted before DataSaver runs,
# and DataSaver's loader then treats the recording as one without face data
# (DataSaver's own include_face=False fails at these tags). No data is filled
# in: the recording has its own reprojection errors (NaN where a point was not
# triangulated). The zip has no synchronized_videos/ folder, which the loader
# needs to exist, so an empty one is made; with no timestamps folder in it the
# timestamps are empty, as FreeMoCap writes them for a recording without one.
#
# Needs numpy, pandas and pydantic (FreeMoCap v1.8.2's lock: numpy 1.26.2,
# pandas 2.1.4, pydantic 2.11.9), and skellytracker==2025.10.1024 installed
# with --no-deps.
import ast
import enum
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import types
from pathlib import Path

import numpy as np
import pandas as pd

clone, tag, source, out = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
out.mkdir(parents=True, exist_ok=True)


def show(path):
    return subprocess.run(
        ["git", "-C", clone, "show", f"{tag}:{path}"],
        capture_output=True, text=True, check=True,
    ).stdout


# A package of FreeMoCap's own modules at <tag>
pkg = Path(tempfile.mkdtemp())
modules = [
    "freemocap/data_layer/data_saver/data_loader.py",
    "freemocap/data_layer/data_saver/data_saver.py",
    "freemocap/data_layer/data_saver/data_models.py",
    "freemocap/system/paths_and_filenames/file_and_folder_names.py",
    "freemocap/core_processes/post_process_skeleton_data/split_and_save.py",
]
for m in modules:
    (pkg / m).parent.mkdir(parents=True, exist_ok=True)
    (pkg / m).write_text(show(m))

# path_getters.py: only the folder lookups the DataLoader calls
getters = ast.parse(show("freemocap/system/paths_and_filenames/path_getters.py"))
wanted = {
    "get_output_data_folder_path",
    "get_synchronized_videos_folder_path",
    "get_timestamps_directory",
}
functions = [n for n in getters.body if isinstance(n, ast.FunctionDef) and n.name in wanted]
assert {f.name for f in functions} == wanted
(pkg / "freemocap/system/paths_and_filenames/path_getters.py").write_text(
    "import logging\nfrom pathlib import Path\nfrom typing import Optional, Union\n"
    "from freemocap.system.paths_and_filenames.file_and_folder_names import (\n"
    "    OUTPUT_DATA_FOLDER_NAME, SYNCHRONIZED_VIDEOS_FOLDER_NAME)\n"
    "logger = logging.getLogger(__name__)\n\n"
    + "\n\n".join(ast.unparse(f) for f in functions)
)
for d in pkg.rglob("*"):
    if d.is_dir():
        (d / "__init__.py").touch()
sys.path.insert(0, str(pkg))


# skellytracker's model info, without running skellytracker's __init__ (which
# configures logging and imports the trackers) and without MediaPipe
def module(name, path=None, **attrs):
    mod = types.ModuleType(name)
    if path is not None:
        mod.__path__ = [str(path)]
    mod.__dict__.update(attrs)
    sys.modules[name] = mod


module("skellytracker", importlib.util.find_spec("skellytracker").submodule_search_locations[0])

POSE = """nose left_eye_inner left_eye left_eye_outer right_eye_inner right_eye
right_eye_outer left_ear right_ear mouth_left mouth_right left_shoulder
right_shoulder left_elbow right_elbow left_wrist right_wrist left_pinky
right_pinky left_index right_index left_thumb right_thumb left_hip right_hip
left_knee right_knee left_ankle right_ankle left_heel right_heel
left_foot_index right_foot_index""".split()
HAND = """wrist thumb_cmc thumb_mcp thumb_ip thumb_tip index_finger_mcp
index_finger_pip index_finger_dip index_finger_tip middle_finger_mcp
middle_finger_pip middle_finger_dip middle_finger_tip ring_finger_mcp
ring_finger_pip ring_finger_dip ring_finger_tip pinky_mcp pinky_pip pinky_dip
pinky_tip""".split()
module(
    "mediapipe.python.solutions.holistic",
    PoseLandmark=enum.IntEnum("PoseLandmark", [n.upper() for n in POSE], start=0),
    HandLandmark=enum.IntEnum("HandLandmark", [n.upper() for n in HAND], start=0),
)
module("mediapipe.python.solutions.face_mesh", FACEMESH_NUM_LANDMARKS_WITH_IRISES=478)
module(
    "mediapipe.python.solutions",
    holistic=sys.modules["mediapipe.python.solutions.holistic"],
    face_mesh=sys.modules["mediapipe.python.solutions.face_mesh"],
)
module("mediapipe.python", solutions=sys.modules["mediapipe.python.solutions"])
module("mediapipe", python=sys.modules["mediapipe.python"])

from skellytracker.trackers.mediapipe_tracker.mediapipe_model_info import MediapipeModelInfo

from freemocap.core_processes.post_process_skeleton_data.split_and_save import split_and_save
from freemocap.data_layer.data_saver.data_saver import DataSaver
from freemocap.system.paths_and_filenames import file_and_folder_names as names

model_info = MediapipeModelInfo()
prefix = model_info.name + "_"

# A copy of the recording folder, as FreeMoCap leaves it after processing
recording = Path(tempfile.mkdtemp()) / source.name
shutil.copytree(source, recording)
output = recording / names.OUTPUT_DATA_FOLDER_NAME
# The zip leaves the videos out, but the loader looks for their folder
(recording / names.SYNCHRONIZED_VIDEOS_FOLDER_NAME).mkdir()

# The recording's own wide body file names MediaPipe's landmarks
recorded = pd.read_csv(output / (prefix + names.BODY_3D_DATAFRAME_CSV_FILE_NAME), nrows=0)
assert list(recorded.columns[::3]) == [f"body_{n}_x" for n in model_info.body_landmark_names]

skeleton = np.load(output / (prefix + names.DATA_3D_NPY_FILE_NAME))
assert skeleton.shape[1] == model_info.num_tracked_points
split_and_save(skeleton_3d_data=skeleton, model_info=model_info, output_data_folder_path=str(output))

# Leave the face mesh out of the tidy files, to keep them small. DataSaver's
# include_face=False fails (its loader then never sets face_dataframe), so the
# wide face file is removed instead, which the loader handles as a recording
# without face data.
(output / (prefix + names.FACE_3D_DATAFRAME_CSV_FILE_NAME)).unlink()
DataSaver(recording_folder_path=recording, model_info=model_info).save_all()

for f in [recording / f"{recording.name}_by_frame.csv",
          recording / f"{recording.name}_by_trajectory.csv",
          output / (prefix + names.BODY_3D_DATAFRAME_CSV_FILE_NAME)]:
    (out / f.name).write_bytes(f.read_bytes())
    print(out / f.name, f.stat().st_size)
