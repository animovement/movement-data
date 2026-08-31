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
[movement-test-data](https://gin.g-node.org/neuroinformatics/movement-test-data) with the
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

## Provenance to be confirmed

The following files predate this repository's record-keeping and their origin has not
been established. They are marked `PROVENANCE UNCONFIRMED` in `metadata.yaml`. Until
each is resolved, do not assume the collection licence covers it.

| File(s) | What is known | What is needed |
| --- | --- | --- |
| `freemocap/…by_frame.csv` | Tidy `by_frame` export, 8 columns, 222 frames; FreeMoCap's own test recording, shared by their developers | Which release it came from, and who supplied it |
| `motive/motive_sample.csv` | Real take `sept-18_mixed-group_16-30`, 2019-09-18, 100 Hz, 190,951 frames | Whose recording it is |

## References

1. Ershov, D., Phan, M.-S., Pylvänäinen, J. W., Rigaud, S. U., et al. (2022). "TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines". *Nature Methods*. [doi: 10.1038/s41592-022-01507-1](https://doi.org/10.1038/s41592-022-01507-1)
2. Tinevez, J.-Y., Perry, N., Schindelin, J., et al. (2017). "TrackMate: An open and extensible platform for single-particle tracking". *Methods* 115: 80–90. [doi: 10.1016/j.ymeth.2016.09.016](https://doi.org/10.1016/j.ymeth.2016.09.016)
3. Rastogi, M., Duan, C. A., et al. (2025). Preprint. [doi: 10.1101/2025.02.14.638359](https://doi.org/10.1101/2025.02.14.638359)
4. Romero-Ferrero, F., Bergomi, M. G., Hinz, R. C., Heras, F. J. H., & de Polavieja, G. G. (2019). "idtracker.ai: tracking all individuals in small or large collectives of unmarked animals". *Nature Methods* 16: 179–182. [doi: 10.1038/s41592-018-0295-5](https://doi.org/10.1038/s41592-018-0295-5)
5. Chiara, V., & Kim, S.-Y. (2023). "AnimalTA: A highly flexible and easy-to-use program for tracking and analysing animal movement in different environments". *Methods in Ecology and Evolution* 14: 1699–1707. [doi: 10.1111/2041-210X.14115](https://doi.org/10.1111/2041-210X.14115)
