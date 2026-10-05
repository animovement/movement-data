# Licensing and attribution

Per-file provenance, in machine-readable form, is in `metadata.yaml`. This file is the
prose version: who shared each dataset, under what terms, and what was changed.

## Licensing information

The collection is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
see `LICENSE`. Individual files carry their own terms where the upstream requires it,
recorded per file in `metadata.yaml` and detailed below. Where a file's terms are
stricter than CC BY 4.0, those terms govern.

### TrackMate example data

`data/trackmate/ExampleTrackMateData.xml` is redistributed unmodified from the
[TrackMateR](https://github.com/quantixed/TrackMateR) R package, where it is
`inst/extdata/ExampleTrackMateData.xml`. Copyright (c) 2022 [Stephen J. Royle](https://orcid.org/0000-0001-8927-6967), released
under the MIT licence; the full notice is in `LICENSES/TrackMateR-MIT.txt`. It was
written by TrackMate 7.7.1 [1, 2]. `aniread::read_trackmate()` is itself adapted from
the TrackMateR reader, with thanks to [@quantixed](https://github.com/quantixed).

### movement netCDF export

`data/movement/SLEAP_two-mice_octagon.analysis-1768334869096.nc` was produced by loading
`poses/SLEAP_two-mice_octagon.analysis.h5` from
[movement-sample-data](https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data) with the
movement Python package and saving it to netCDF. The source data is licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and was shared by
[Mehul Rastogi](https://orcid.org/0000-0002-5315-3188) and
[Chunyu A. Duan](https://orcid.org/0000-0002-3095-8653) (Sainsbury Wellcome Centre, UCL): two mice competing for rewards in
an octagonal arena [3]. It is kept here rather than fetched from GIN because GIN serves
the SLEAP form, not the movement netCDF form.

### C3D example

`data/c3d/example.c3d` is redistributed unmodified from
[pyomeca/ezc3d-testFiles](https://github.com/pyomeca/ezc3d-testFiles), released there
under **GPL-3.0**; the full notice is in `LICENSES/ezc3d-testFiles-GPL-3.0.txt`. It
reached this repository via the [c3dr](https://github.com/ropensci/c3dr) R package,
where it is `inst/extdata/example.c3d`, returned by `c3d_example()` and documented in
`?c3d_example`. c3dr itself is MIT — that covers the package code, not this file, which
remains GPL-3.0. The recording is human walking with a full-body model, analog channels
(e.g. EMG) and two force platforms, captured on a Qualisys system.

### FicTrac sample

`data/fictrac/fictrac_sample.dat` was shared freely by
[Chi-Yu Lee](https://orcid.org/0000-0001-6440-3050)
([@chiyu1203](https://github.com/chiyu1203)) on 2025-02-26 in
[rjdmoore/fictrac#32](https://github.com/rjdmoore/fictrac/issues/32), in direct response
to a request for sample data to develop an R reader against. They confirmed on
2026-08-31, in the same thread, that the file may sit under the collection's CC BY 4.0
licence with attribution to them.

### Octron sample

`data/octron/sample-data.csv` is an in-house recording by
[Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058). Both the tracked label and the
video name were changed to `worm` before sharing, to avoid disclosing unpublished work,
so `worm` and `my_cool_video_of_a_worm.mp4` are placeholders — do not cite this file as
an example of any particular species.

### idtracker.ai trajectories

The files in `data/idtrackerai/` were shared freely by
[Jordi Torrents](https://orcid.org/0009-0006-6353-4079), one of the idtracker.ai
developers (Champalimaud Foundation). They were tracked with idtracker.ai 6.0.0a0 [4] from
`test_B.avi`, the project's own installation-test video: 8 individuals at 28 fps.

### AnimalTA coordinates

The files in `data/AnimalTA/` were shared freely by
[Violette Chiara](https://orcid.org/0000-0002-3442-5336), lead developer of AnimalTA
and first author of its paper [5]. The two files cover AnimalTA's two export layouts — one wide column pair
per arena, and one long format with explicit arena and individual columns.

### Fixtures generated for aniread

These files were made for the readers in [aniread](https://github.com/animovement/aniread)
by [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058), and are released under
the collection's CC BY 4.0 unless they derive from a file with other terms, in which
case they inherit those. Synthetic files hold made-up values; where possible they were
written by the producing software's own writer code, copied from its source, so their
layout is the software's rather than a guess at it.

- `data/AnimalTA/detailed/` (5 files), `head_tail_two_arenas.csv` and
  `head_tail_two_arenas_corrected.csv`: synthetic, written with AnimalTA's own export
  and coordinates code (AnimalTA is MIT; [GitHub](https://github.com/VioletteChiara/AnimalTA)
  commit 840af1b, nine commits after v4.2.0). They cover AnimalTA's real detailed data
  (one file per target), head and tail columns, and the `part0`/`part1` identities a
  corrected head-and-tail file gets. Used by
  [aniread#162](https://github.com/animovement/aniread/pull/162).
- `data/idtrackerai/trajectories_csv_no_fps/`: synthetic, written by idtracker.ai
  6.0.15's own `_save_array_to_csv()` with no frame rate, so with no time column. Used
  by [aniread#163](https://github.com/animovement/aniread/pull/163).
- `data/movement/two-mice_frames.nc`: derived, the first four frames of the octagon
  sample above, cut with rhdf5 and given the root attributes movement writes without a
  frame rate. It inherits CC BY 4.0 and the attribution to Mehul Rastogi and Chunyu A.
  Duan [3]. Used by [aniread#158](https://github.com/animovement/aniread/pull/158).
- `data/movement/synthetic_3d.nc`: synthetic, a 3D poses file in movement's on-disk
  layout, written with rhdf5. Used by
  [aniread#161](https://github.com/animovement/aniread/pull/161).
- `data/sleap/SLEAP_three-mice_Aeon_mixed-labels.analysis.csv`: derived, the first 20
  frames of `poses/SLEAP_three-mice_Aeon_mixed-labels.analysis.h5` from
  [movement's GIN](https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data)
  (CC BY 4.0, shared by Chang Huan Lo, Sainsbury Wellcome Centre), written in SLEAP's
  analysis CSV layout as sleap-io defines it. Made for
  [aniread#124](https://github.com/animovement/aniread/pull/124).

### FreeMoCap star jumps

`data/freemocap/freemocap_star-jump_by_frame.csv`, `freemocap_star-jump_by_frame_v1.7.csv`,
`freemocap_star-jump_by_trajectory.csv` and `freemocap_star-jump_mediapipe_body_3d_xyz.csv`
are derived from `poses/FreeMoCap_star-jump_session-folder.zip` in
[movement's sample data](https://gin.swc.ucl.ac.uk/neuroinformatics/movement-sample-data),
released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and shared by
Max Staras (Sainsbury Wellcome Centre, UCL): one person doing four star jumps, recorded
with FreeMoCap and two cameras, 216 frames at 30 fps. They inherit CC BY 4.0; credit
Max Staras and the movement project.

They were written by FreeMoCap's own code from the recording's saved arrays (the
post-processed skeleton, centres of mass and reprojection errors) with
`scripts/freemocap_star_jump.py`, which runs FreeMoCap's `split_and_save()` and
`DataSaver.save_all()` taken unchanged from its v1.8.2 tag (the 9-column `by_frame`
file, the `by_trajectory` file and the wide body file) and its v1.7.3 tag (the 8-column
`by_frame` file). No values were changed or filled. The face mesh is left out to keep
the files small, and the timestamps are empty because the zip holds no videos folder.
They replace `freemocap_test_data_by_frame.csv` as aniread's FreeMoCap sample
([#10](https://github.com/animovement/movement-data/issues/10)).

### TrackMate examples from Zenodo

Three TrackMate XML files are redistributed unmodified from Zenodo records released
under CC BY 4.0. `CelegansEarly_MIP.xml`
([10.5281/zenodo.5132918](https://doi.org/10.5281/zenodo.5132918)) is by
[Jean-Yves Tinevez](https://orcid.org/0000-0002-0998-4718) (Institut Pasteur), written
by TrackMate 7.0.4. `trpL_150310-11.xml`
([10.5281/zenodo.12600359](https://doi.org/10.5281/zenodo.12600359)) is by Simon van
Vliet and Annina Winkler (ETH Zurich), written by TrackMate 7.13.2 from images of
van Vliet et al. [15]. `U251_mitoRED_lifeAct670_3-MIP.xml`
([10.5281/zenodo.12784611](https://doi.org/10.5281/zenodo.12784611)) is by
[Ines Saenz de Santa Maria](https://orcid.org/0000-0002-1868-3001) and Jean-Yves
Tinevez (Institut Pasteur), written by TrackMate 7.0.0. Cite TrackMate [1, 2].

### FastTrack test result

`data/fasttrack/tracking.txt` and `tracking.db` are redistributed unmodified from
[FastTrack](https://github.com/FastTrackOrg/FastTrack)'s own accuracy test
(`test/dataSet/images/Groundtruth/Tracking_Result/`), by Benjamin Gallois, under
**GPL-3.0**; the notice is in `LICENSES/FastTrack-GPL-3.0.txt`. The two hold the same
tracking, as text and as FastTrack's SQLite database. Cite [8].

### SLEAP tutorial results

`data/sleap/new_video.v002.000_mice_new.analysis.h5` and `.analysis.csv` come from
`new_data/results.zip` in
[talmolab/cosyne-tutorial-data](https://github.com/talmolab/cosyne-tutorial-data), the
data for the SLEAP tutorial at Cosyne 2024, released under **BSD-3-Clause**, Copyright
(c) 2024, Talmo Lab at the Salk Institute; the notice is in
`LICENSES/cosyne-tutorial-data-BSD-3-Clause.txt`. The `.h5` is unmodified; the `.csv`
is cut to its first 200 frames. The video and `.slp` in the zip are not included.
Cite SLEAP [9].

### Lightning Pose predictions

`data/lightningpose/180607_004.train_frames=75.rng=0.top.csv` and `.bot.csv` are
redistributed unmodified from the
[Ensemble Kalman Smoother](https://github.com/paninski-lab/eks) repository
(`data/mirror-mouse-separate/`), released under **MIT**, Copyright (c) 2023 Cole
Hurwitz; the notice is in `LICENSES/eks-MIT.txt`. Lightning Pose predictions of one
mirror-mouse video, one file per camera view. Cite Lightning Pose [10].

### DeepLabCut leafcutter ant tracklets

`data/deeplabcut/ant_video_5DLC_dlcrnetms5_AntsFeb11shuffle1_100000_el.h5` is
redistributed unmodified from CatalystNeuro's
[behavior_testing_data](https://gin.g-node.org/CatalystNeuro/behavior_testing_data) on
GIN (`DLC/multi_subject_h5/landmarks_and_subject_keypoints/`). That folder carries its
own LICENSE, **Apache-2.0**, which overrides the repository's ODbL and CC BY-SA 4.0
default; no other file is taken from that repository. The notice is in
`LICENSES/Leaf_Ant_Analysis-Apache-2.0.txt`. The GIN file is a 300-frame excerpt of
the tracking in
[AdaptiveMotorControlLab/Leaf_Ant_Analysis](https://github.com/AdaptiveMotorControlLab/Leaf_Ant_Analysis),
also Apache-2.0, by Mackenzie W. Mathis, from Gilbert, Glastad et al. [11].

### Motive glider throw

`data/motive/V4_throw_003.csv` is redistributed unmodified from
[basfora/gliderstudio](https://github.com/basfora/gliderstudio)
(`data/mydata/V4_throw_003.csv`), released under **MIT**, Copyright (c) 2024 basfora;
the notice is in `LICENSES/gliderstudio-MIT.txt`. A Motive CSV, format version 1.24, of
a thrown glider.

### Vicon Nexus C3D

`data/c3d/Sample_Static.c3d` is redistributed unmodified from
[pyCGM](https://github.com/cadop/pyCGM) (`SampleData/ROM/Sample_Static.c3d`), released
under **MIT**, Copyright (c) 2015 cadop (Mathew Schwartz); the notice is in
`LICENSES/pyCGM-MIT.txt`. Written by Vicon Nexus 1.8.5; pyCGM does not state who
recorded it. Cite pyCGM [12].

### Accelerometer samples

- `data/accelerometer/cwa/ax3_testfile.cwa` and `ax6_testfile.cwa` are redistributed
  unmodified from [GGIRread](https://github.com/wadpac/GGIRread)
  (`inst/testfiles/`), released under **Apache-2.0**; GGIRread names the Medical
  Research Council UK and Accelting as copyright holders. The notice is in
  `LICENSES/GGIRread-Apache-2.0.txt`.
- `data/accelerometer/gt3x/example.gt3x` is redistributed unmodified from
  [agcounts](https://github.com/bhelsel/agcounts) (`inst/extdata/example.gt3x`, also on
  CRAN), released under **MIT**, Copyright (c) 2024 University of Kansas; the notice is
  in `LICENSES/agcounts-MIT.txt`.
- `data/accelerometer/bebe/CRAT_ACT_TrainingDataset_2016-2018IMRS.csv` is the first
  2,000 rows of the rattlesnake data in `raw_desantis_rattlesnakes.zip` of the
  Bio-logger Ethogram Benchmark ([10.5281/zenodo.7947104](https://doi.org/10.5281/zenodo.7947104)).
  The dataset's own licence file states CC BY 4.0, by Dominic L. DeSantis, Vicente
  Mata-Silva, Jerry D. Johnson and Amy E. Wagler, and asks that [7] be cited; cite the
  benchmark [6] too.

### Formats for future readers

These are formats aniread cannot read yet, kept so readers can be written against real
files.

- `data/ethovision/S22-Track-Cupim02SeptTarde-Trial.txt` is redistributed unmodified
  from [10.5281/zenodo.3628061](https://doi.org/10.5281/zenodo.3628061), CC BY 4.0, by
  Julieth Castiblanco, Paulo Fellipe Cristaldo, Leticia Ribeiro Paiva and Og DeSouza: an
  EthoVision XT track export of one focal termite (*Cornitermes cumulans*). The dataset
  is documented at <https://osf.io/r5vaq>.
- `data/nwb/0.3.0_poseestimation_one_camera.nwb` is redistributed unmodified from
  [ndx-pose](https://github.com/rly/ndx-pose)
  (`src/pynwb/tests/back_compat/`), released under **BSD-3-Clause**; the notice is in
  `LICENSES/ndx-pose-BSD-3-Clause.txt`. A synthetic test file in ndx-pose 0.3.0.
- `data/opensim/gait10dof18musc_walk_CRLF_line_ending.trc` and
  `subject01_walk1_ik.mot` are redistributed from
  [opensim-core](https://github.com/opensim-org/opensim-core), released under
  **Apache-2.0**; the licence and OpenSim's NOTICE are in
  `LICENSES/opensim-core-Apache-2.0.txt`. A marker TRC and an inverse kinematics MOT
  of one walking trial. OpenSim asks that [13, 14] be cited.

## Provenance to be confirmed

The following files predate this repository's record-keeping and their origin has not
been established. They are marked `PROVENANCE UNCONFIRMED` in `metadata.yaml`. Until
each is resolved, do not assume the collection licence covers it.

| File(s) | What is known | What is needed |
| --- | --- | --- |
| `freemocap/freemocap_test_data_by_frame.csv` | Tidy `by_frame` export, 8 columns, 222 frames; FreeMoCap's own test recording, shared by their developers. Superseded by the star-jump files above | Which release it came from, and who supplied it |
| `motive/motive_sample.csv` | Real take `sept-18_mixed-group_16-30`, 2019-09-18, 100 Hz, 190,951 frames | Whose recording it is |

## References

1. Ershov, D., Phan, M.-S., Pylvänäinen, J. W., Rigaud, S. U., et al. (2022). "TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines". *Nature Methods*. [doi: 10.1038/s41592-022-01507-1](https://doi.org/10.1038/s41592-022-01507-1)
2. Tinevez, J.-Y., Perry, N., Schindelin, J., et al. (2017). "TrackMate: An open and extensible platform for single-particle tracking". *Methods* 115: 80–90. [doi: 10.1016/j.ymeth.2016.09.016](https://doi.org/10.1016/j.ymeth.2016.09.016)
3. Rastogi, M., Duan, C. A., et al. (2025). Preprint. [doi: 10.1101/2025.02.14.638359](https://doi.org/10.1101/2025.02.14.638359)
4. Romero-Ferrero, F., Bergomi, M. G., Hinz, R. C., Heras, F. J. H., & de Polavieja, G. G. (2019). "idtracker.ai: tracking all individuals in small or large collectives of unmarked animals". *Nature Methods* 16: 179–182. [doi: 10.1038/s41592-018-0295-5](https://doi.org/10.1038/s41592-018-0295-5)
5. Chiara, V., & Kim, S.-Y. (2023). "AnimalTA: A highly flexible and easy-to-use program for tracking and analysing animal movement in different environments". *Methods in Ecology and Evolution* 14: 1699–1707. [doi: 10.1111/2041-210X.14115](https://doi.org/10.1111/2041-210X.14115)
6. Hoffman, B., Cusimano, M., Baglione, V., Canestrari, D., et al. (2024). "A benchmark for computational analysis of animal behavior, using animal-borne tags". *Movement Ecology* 12: 78. [doi: 10.1186/s40462-024-00511-8](https://doi.org/10.1186/s40462-024-00511-8)
7. DeSantis, D. L., Mata-Silva, V., Johnson, J. D., & Wagler, A. E. (2020). "Integrative Framework for Long-Term Activity Monitoring of Small and Secretive Animals: Validation With a Cryptic Pitviper". *Frontiers in Ecology and Evolution* 8: 169. [doi: 10.3389/fevo.2020.00169](https://doi.org/10.3389/fevo.2020.00169)
8. Gallois, B., & Candelier, R. (2021). "FastTrack: An open-source software for tracking varying numbers of deformable objects". *PLOS Computational Biology* 17: e1008697. [doi: 10.1371/journal.pcbi.1008697](https://doi.org/10.1371/journal.pcbi.1008697)
9. Pereira, T. D., Tabris, N., Matsliah, A., Turner, D. M., et al. (2022). "SLEAP: A deep learning system for multi-animal pose tracking". *Nature Methods* 19: 486-495. [doi: 10.1038/s41592-022-01426-1](https://doi.org/10.1038/s41592-022-01426-1)
10. Biderman, D., Whiteway, M. R., Hurwitz, C., Greenspan, N., et al. (2024). "Lightning Pose: improved animal pose estimation via semi-supervised learning, Bayesian ensembling and cloud-native open-source tools". *Nature Methods* 21: 1316-1328. [doi: 10.1038/s41592-024-02319-1](https://doi.org/10.1038/s41592-024-02319-1)
11. Gilbert, M. B., Glastad, K. M., Fioriti, M., Sorek, M., et al. (2024). "Neuropeptides specify and reprogram division of labor in the leafcutter ant *Atta cephalotes*". Preprint. [doi: 10.1101/2024.11.07.622473](https://doi.org/10.1101/2024.11.07.622473)
12. Schwartz, M., & Dixon, P. C. (2018). "The effect of subject measurement error on joint kinematics in the conventional gait model: Insights from the open-source pyCGM tool using high performance computing methods". *PLOS ONE* 13: e0189984. [doi: 10.1371/journal.pone.0189984](https://doi.org/10.1371/journal.pone.0189984)
13. Delp, S. L., Anderson, F. C., Arnold, A. S., Loan, P., et al. (2007). "OpenSim: Open-Source Software to Create and Analyze Dynamic Simulations of Movement". *IEEE Transactions on Biomedical Engineering* 54: 1940-1950. [doi: 10.1109/TBME.2007.901024](https://doi.org/10.1109/TBME.2007.901024)
14. Seth, A., Hicks, J. L., Uchida, T. K., Habib, A., et al. (2018). "OpenSim: Simulating musculoskeletal dynamics and neuromuscular control to study human and animal movement". *PLOS Computational Biology* 14: e1006223. [doi: 10.1371/journal.pcbi.1006223](https://doi.org/10.1371/journal.pcbi.1006223)
15. van Vliet, S., Dal Co, A., Winkler, A. R., Spriewald, S., et al. (2018). "Spatially Correlated Gene Expression in Bacterial Groups: The Role of Lineage History, Spatial Gradients, and Cell-Cell Interactions". *Cell Systems* 6: 496-507. [doi: 10.1016/j.cels.2018.03.009](https://doi.org/10.1016/j.cels.2018.03.009)
