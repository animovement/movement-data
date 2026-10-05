# movement-data

Sample data for testing the [animovement](https://github.com/animovement) R packages,
served to users through `aniread::get_sample_data()`.

Every file here is small on purpose. These are fixtures for exercising readers, not
datasets for analysis — most are excerpts of a longer recording, kept just long enough
to cover the format variant they represent.

## What is here

| Directory | Software | Files | Shared by | Terms |
| --- | --- | --- | --- | --- |
| `accelerometer/bebe/` | Bio-logger (BEBE) | 1 | Dominic L. DeSantis et al., via [BEBE](https://doi.org/10.5281/zenodo.7947104) | CC BY 4.0 |
| `accelerometer/cwa/` | Axivity AX3, AX6 | 2 | [GGIRread](https://github.com/wadpac/GGIRread) | **Apache-2.0** |
| `accelerometer/gt3x/` | ActiGraph | 1 | [agcounts](https://github.com/bhelsel/agcounts) (University of Kansas) | **MIT** |
| `AnimalTA/` | AnimalTA | 2 | [Violette Chiara](https://orcid.org/0000-0002-3442-5336) | CC BY 4.0 |
| `AnimalTA/` (`detailed/`, `head_tail_*`) | AnimalTA (synthetic) | 7 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `bonsai/` | Bonsai | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `c3d/` (`example.c3d`) | Qualisys (C3D) | 1 | [pyomeca/ezc3d-testFiles](https://github.com/pyomeca/ezc3d-testFiles), via [c3dr](https://github.com/ropensci/c3dr) | **GPL-3.0** |
| `c3d/` (`Sample_Static.c3d`) | Vicon Nexus (C3D) | 1 | [pyCGM](https://github.com/cadop/pyCGM) | **MIT** |
| `deeplabcut/` | DeepLabCut | 1 | Mackenzie W. Mathis ([Leaf_Ant_Analysis](https://github.com/AdaptiveMotorControlLab/Leaf_Ant_Analysis)), via [CatalystNeuro's GIN](https://gin.g-node.org/CatalystNeuro/behavior_testing_data) | **Apache-2.0** |
| `ethovision/` | EthoVision XT | 1 | [Castiblanco, Cristaldo, Paiva and DeSouza](https://doi.org/10.5281/zenodo.3628061) | CC BY 4.0 |
| `fasttrack/` | FastTrack | 2 | [FastTrack](https://github.com/FastTrackOrg/FastTrack) (Benjamin Gallois) | **GPL-3.0** |
| `fictrac/` | FicTrac | 1 | [Chi-Yu Lee](https://orcid.org/0000-0001-6440-3050) | CC BY 4.0 |
| `freemocap/` (`freemocap_star-jump_*`) | FreeMoCap | 4 | Max Staras, via [movement's GIN](https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data) | CC BY 4.0 |
| `freemocap/` (`freemocap_test_data_by_frame.csv`) | FreeMoCap | 1 | The FreeMoCap developers — **exact source to confirm**; superseded | — |
| `idtrackerai/` | idtracker.ai | 4 | [Jordi Torrents](https://orcid.org/0009-0006-6353-4079) | CC BY 4.0 |
| `idtrackerai/` (`trajectories_csv_no_fps/`) | idtracker.ai (synthetic) | 2 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `lightningpose/` | Lightning Pose | 2 | [paninski-lab/eks](https://github.com/paninski-lab/eks) | **MIT** |
| `motive/` (`motive_sample.csv`) | OptiTrack Motive | 1 | **To confirm** | — |
| `motive/` (`V4_throw_003.csv`) | OptiTrack Motive | 1 | [basfora/gliderstudio](https://github.com/basfora/gliderstudio) | **MIT** |
| `movement/` | movement | 2 | [Mehul Rastogi](https://orcid.org/0000-0002-5315-3188), [Chunyu A. Duan](https://orcid.org/0000-0002-3095-8653) | CC BY 4.0 |
| `movement/` (`synthetic_3d.nc`) | movement (synthetic) | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `nwb/` | NWB (ndx-pose) | 1 | [ndx-pose](https://github.com/rly/ndx-pose) | **BSD-3-Clause** |
| `octron/` | Octron | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `opensim/` | OpenSim | 2 | [opensim-core](https://github.com/opensim-org/opensim-core) | **Apache-2.0** |
| `sleap/` (`SLEAP_three-mice_Aeon_*`) | SLEAP | 1 | Chang Huan Lo, via [movement's GIN](https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data) | CC BY 4.0 |
| `sleap/` (`new_video.v002.*`) | SLEAP | 2 | Talmo Lab ([cosyne-tutorial-data](https://github.com/talmolab/cosyne-tutorial-data)) | **BSD-3-Clause** |
| `trackball/` | trackball rigs | 10 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `trackmate/` (`ExampleTrackMateData.xml`) | TrackMate | 1 | [Stephen J. Royle](https://orcid.org/0000-0001-8927-6967) | **MIT** |
| `trackmate/` (the other three) | TrackMate | 3 | [Jean-Yves Tinevez](https://orcid.org/0000-0002-0998-4718), Simon van Vliet and Annina Winkler, [Ines Saenz de Santa Maria](https://orcid.org/0000-0002-1868-3001), via Zenodo | CC BY 4.0 |
| `trex/` | TRex | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |

Full attribution, including what was modified and what to cite, is in
[`LICENSING.md`](LICENSING.md).

`metadata.yaml` carries one block per file with its checksum, the software and version
that wrote it, the export variant it exercises, who shared it, and what was modified.

## Relationship to the GIN server

The [neuroinformatics/movement-sample-data](https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data)
repository on G-Node GIN is the sample-data home of the
[movement](https://movement.neuroinformatics.dev/) Python package. It is well curated
and well documented, and this repository deliberately does not duplicate it.

Anything GIN already serves is fetched from GIN. `aniread::get_sample_data()` points
its Anipose, DeepLabCut, LightningPose, SLEAP and TRex-locusts entries straight at GIN
URLs. This repository holds only formats and export variants GIN does not cover,
plus files derived from GIN data that GIN serves only in another form: the two
SLEAP-octagon files in `movement/`, and the Aeon analysis CSV in `sleap/`, made from
the SLEAP `.h5`. The SLEAP, DeepLabCut and Lightning Pose files that are not derived
from GIN cover variants GIN lacks: SLEAP's own analysis CSV, multi-animal tracklets
with unique bodyparts, and one CSV per camera view.

Local copies of GIN files were removed in August 2026. If you need them, take them
from GIN, and credit the people named in its `metadata.yaml`.

### Where the schemas differ

`metadata.yaml` follows GIN's schema so the two stay comparable, and adds three fields:

- **`version`** — GIN records no version anywhere. That is fine for a library built
  around one canonical format, but this repository exists to test *readers*, and export
  layouts drift between releases. FreeMoCap, AnimalTA and TRex have all changed theirs.
  A fixture is only meaningful if you know which variant it exercises, so each entry
  records `source_version`, `format_version`, a `variant` name, and — importantly —
  `determined_by`, which says whether the version was read out of the file (`file`),
  deduced from its column layout (`inferred`), or is simply not recoverable (`unknown`).
  Only some formats here record a version at all: TrackMate XML (`7.0.0` to `7.13.2`),
  idtracker.ai (`6.0.0a0`), C3D from Vicon Nexus (`1.8.5`), NWB (its namespace
  versions), ActiGraph GT3X (device firmware) and Motive, which is the one format that
  versions its *export* separately from the application (`Format Version,1.23` and
  `1.24`).
- **`upstream`** — where a file came from, when it was not produced for this repository.
- **`modification`** — what was changed relative to that upstream.

## Licensing

The collection is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
see `LICENSE`. Some files carry their own terms, which govern where they are stricter:
GPL-3.0, MIT, BSD-3-Clause or Apache-2.0, shown in bold in the table above and recorded
per file in `metadata.yaml`, with each notice in `LICENSES/`.

**[`LICENSING.md`](LICENSING.md) is the attribution record**: who shared each dataset,
under what terms, what was modified, and the references to cite. It also lists the two
files whose origin is still unresolved. Per-file metadata is in `metadata.yaml`.

## Maintaining this repository

Adding a file means adding its `metadata.yaml` block in the same commit. At minimum:
`sha256sum`, `source_software`, `version`, `shared_by`, `upstream` and `modification`.
A file whose origin you cannot state is a file that should not be committed.

Run `python3 update_hashes.py` to refresh the checksums after changing any data file;
it rewrites `sha256sum` in place and reports files missing a metadata block.

Scripts that regenerate derived files from their upstream are in `scripts/`, named in
the files' `modification` field.
