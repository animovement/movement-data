# movement-data

Sample data for testing the [animovement](https://github.com/animovement) R packages,
served to users through `aniread::get_sample_data()`.

Every file here is small on purpose. These are fixtures for exercising readers, not
datasets for analysis — most are excerpts of a longer recording, kept just long enough
to cover the format variant they represent.

## What is here

| Directory | Software | Files | Shared by | Terms |
| --- | --- | --- | --- | --- |
| `AnimalTA/` | AnimalTA | 2 | [Violette Chiara](https://orcid.org/0000-0002-3442-5336) | CC BY 4.0 |
| `bonsai/` | Bonsai | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `c3d/` | Qualisys (C3D) | 1 | [pyomeca/ezc3d-testFiles](https://github.com/pyomeca/ezc3d-testFiles), via [c3dr](https://github.com/ropensci/c3dr) | **GPL-3.0** |
| `fictrac/` | FicTrac | 1 | [Chi-Yu Lee](https://orcid.org/0000-0001-6440-3050) | CC BY 4.0 |
| `freemocap/` | FreeMoCap | 1 | The FreeMoCap developers — **exact source to confirm** | — |
| `idtrackerai/` | idtracker.ai | 4 | [Jordi Torrents](https://orcid.org/0009-0006-6353-4079) | CC BY 4.0 |
| `motive/` | OptiTrack Motive | 1 | **To confirm** | — |
| `movement/` | movement | 1 | [Mehul Rastogi](https://orcid.org/0000-0002-5315-3188), [Chunyu A. Duan](https://orcid.org/0000-0002-3095-8653) | CC BY 4.0 |
| `octron/` | Octron | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `trackball/` | trackball rigs | 10 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |
| `trackmate/` | TrackMate | 1 | [Stephen J. Royle](https://orcid.org/0000-0001-8927-6967) | **MIT** |
| `trex/` | TRex | 1 | [Mikkel Roald-Arbøl](https://orcid.org/0000-0002-9998-0058) | CC BY 4.0 |

Full attribution, including what was modified and what to cite, is in
[`LICENSING.md`](LICENSING.md).

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

## Licensing

The collection is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
see `LICENSE`. Some files carry their own terms, which govern where they are stricter —
`data/c3d/example.c3d` is GPL-3.0 and `data/trackmate/ExampleTrackMateData.xml` is MIT,
with the notices in `LICENSES/`.

**[`LICENSING.md`](LICENSING.md) is the attribution record**: who shared each dataset,
under what terms, what was modified, and the references to cite. It also lists the two
files whose origin is still unresolved. Per-file metadata is in `metadata.yaml`.

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
