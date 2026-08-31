# movement-data

Sample data for testing the [animovement](https://github.com/animovement) R packages,
served to users through `aniread::get_sample_data()`.

Every file here is small on purpose. These are fixtures for exercising readers, not
datasets for analysis — most are excerpts of a longer recording, kept just long enough
to cover the format variant they represent.

## What is here

| Directory | Software | Files | Provenance |
| --- | --- | --- | --- |
| `AnimalTA/` | AnimalTA | 2 | Shared by the AnimalTA developer |
| `bonsai/` | Bonsai | 1 | Recorded in-house |
| `c3d/` | Qualisys (C3D) | 1 | ezc3d-testFiles via c3dr, **GPL-3.0** |
| `fictrac/` | FicTrac | 1 | Shared by Chiyu Lee |
| `freemocap/` | FreeMoCap | 1 | **To confirm** |
| `idtrackerai/` | idtracker.ai | 4 | Shared by Jordi Torrents |
| `motive/` | OptiTrack Motive | 1 | **To confirm** |
| `movement/` | movement | 1 | Derived from GIN, CC BY 4.0 |
| `octron/` | Octron | 1 | Recorded in-house |
| `trackball/` | trackball rigs | 10 | Recorded in-house |
| `trackmate/` | TrackMate | 1 | TrackMateR, **MIT** |
| `trex/` | TRex | 1 | Recorded in-house |

`metadata.yaml` carries one block per file with its checksum, the software and version
that wrote it, the export variant it exercises, who shared it, and what was modified.

## Relationship to the GIN server

The [neuroinformatics/movement-test-data](https://gin.g-node.org/neuroinformatics/movement-test-data)
repository on G-Node GIN is the sample-data home of the
[movement](https://movement.neuroinformatics.dev/) Python package. It is well curated
and well documented, and this repository deliberately does not duplicate it.

Anything GIN already serves is fetched from GIN. `aniread::get_sample_data()` points
its Anipose, DeepLabCut, LightningPose, SLEAP and TRex-locusts entries straight at GIN
URLs. This repository holds only formats GIN does not cover, plus one file
(`movement/`) that is derived from GIN data but exists there only in its pre-export
form.

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
  Only three formats here record a version at all: TrackMate XML (`7.7.1`), idtracker.ai
  (`6.0.0a0`) and Motive, which is the one format that versions its *export* separately
  from the application (`Format Version,1.23`).
- **`upstream`** — where a file came from, when it was not produced for this repository.
- **`modification`** — what was changed relative to that upstream.

## Licensing information

The collection is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
see `LICENSE`. Individual files carry their own terms where the upstream requires it,
recorded per file in `metadata.yaml` and detailed below. Where a file's terms are
stricter than CC BY 4.0, those terms govern.

### TrackMate example data

`data/trackmate/ExampleTrackMateData.xml` is redistributed unmodified from the
[TrackMateR](https://github.com/quantixed/TrackMateR) R package, where it is
`inst/extdata/ExampleTrackMateData.xml`. Copyright (c) 2022 Stephen J. Royle, released
under the MIT licence; the full notice is in `LICENSES/TrackMateR-MIT.txt`. It was
written by TrackMate 7.7.1 [1, 2]. `aniread::read_trackmate()` is itself adapted from
the TrackMateR reader, with thanks to [@quantixed](https://github.com/quantixed).

### movement netCDF export

`data/movement/SLEAP_two-mice_octagon.analysis-1768334869096.nc` was produced by loading
`poses/SLEAP_two-mice_octagon.analysis.h5` from
[movement-test-data](https://gin.g-node.org/neuroinformatics/movement-test-data) with the
movement Python package and saving it to netCDF. The source data is licensed
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and was shared by Mehul Rastogi
and Chunyu Ann Duan (Sainsbury Wellcome Centre, UCL): two mice competing for rewards in
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
[Chiyu Lee](https://github.com/chiyu1203) on 2025-02-26 in
[rjdmoore/fictrac#32](https://github.com/rjdmoore/fictrac/issues/32), in direct response
to a request for sample data to develop an R reader against. No licence was stated, so
the file sits outside the collection licence until Chiyu Lee confirms terms.

### Octron sample

`data/octron/sample-data.csv` is an in-house recording. Both the tracked label and the
video name were changed to `worm` before sharing, to avoid disclosing unpublished work,
so `worm` and `my_cool_video_of_a_worm.mp4` are placeholders — do not cite this file as
an example of any particular species.

### idtracker.ai trajectories

The files in `data/idtrackerai/` were shared freely by Jordi Torrents, one of the
idtracker.ai developers. They were tracked with idtracker.ai 6.0.0a0 [4] from
`test_B.avi`, the project's own installation-test video: 8 individuals at 28 fps.

### AnimalTA coordinates

The files in `data/AnimalTA/` were shared freely by Vincent Chiara, lead developer of
AnimalTA [5]. The two files cover AnimalTA's two export layouts — one wide column pair
per arena, and one long format with explicit arena and individual columns.

## Provenance to be confirmed

The following files predate this repository's record-keeping and their origin has not
been established. They are marked `PROVENANCE UNCONFIRMED` in `metadata.yaml`. Until
each is resolved, do not assume the collection licence covers it.

| File(s) | What is known | What is needed |
| --- | --- | --- |
| `freemocap/…by_frame.csv` | Tidy `by_frame` export, 8 columns, 222 frames | Who supplied it (see the version note below) |
| `motive/motive_sample.csv` | Real take `sept-18_mixed-group_16-30`, 2019-09-18, 100 Hz, 190,951 frames | Whose recording it is |

### Known coverage gap: FreeMoCap

`freemocap_test_data_by_frame.csv` has 8 columns. FreeMoCap 1.8.2's
`DataSaver.save_to_tidy_csv()` writes a 9th, `reprojection_error`, so nothing here
exercises the current layout. FreeMoCap ships no ready-made `by_frame.csv` sample —
GIN's session-folder fixtures contain the per-model wide CSVs
(`mediapipe_body_3d_xyz.csv` and friends), which `read_freemocap()` rejects by design —
so refreshing this fixture means running the FreeMoCap pipeline, not downloading
anything.

## Maintaining this repository

Adding a file means adding its `metadata.yaml` block in the same commit. At minimum:
`sha256sum`, `source_software`, `version`, `shared_by`, `upstream` and `modification`.
A file whose origin you cannot state is a file that should not be committed.

Run `python3 update_hashes.py` to refresh the checksums after changing any data file;
it rewrites `sha256sum` in place and reports files missing a metadata block.

## References

1. Ershov, D., Phan, M.-S., Pylvänäinen, J. W., Rigaud, S. U., et al. (2022). "TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines". *Nature Methods*. [doi: 10.1038/s41592-022-01507-1](https://doi.org/10.1038/s41592-022-01507-1)
2. Tinevez, J.-Y., Perry, N., Schindelin, J., et al. (2017). "TrackMate: An open and extensible platform for single-particle tracking". *Methods* 115: 80–90. [doi: 10.1016/j.ymeth.2016.09.016](https://doi.org/10.1016/j.ymeth.2016.09.016)
3. Rastogi, M., Duan, C. A., et al. (2025). Preprint. [doi: 10.1101/2025.02.14.638359](https://doi.org/10.1101/2025.02.14.638359)
4. Romero-Ferrero, F., Bergomi, M. G., Hinz, R. C., Heras, F. J. H., & de Polavieja, G. G. (2019). "idtracker.ai: tracking all individuals in small or large collectives of unmarked animals". *Nature Methods* 16: 179–182. [doi: 10.1038/s41592-018-0295-5](https://doi.org/10.1038/s41592-018-0295-5)
5. Chiara, V., & Kim, S.-Y. (2023). "AnimalTA: A highly flexible and easy-to-use program for tracking and analysing animal movement in different environments". *Methods in Ecology and Evolution* 14: 1699–1707. [doi: 10.1111/2041-210X.14115](https://doi.org/10.1111/2041-210X.14115)
