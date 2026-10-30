# Releases of the book

Each GitHub release of this repo carries one asset: riddling.pdf, the book as
committed in docs/riddling.pdf at the tagged commit (the same file GitHub Pages
serves).

- Tags are dates, YYYYMMDD (the first release is 20261030), since the book has
no version number. This follows the embeddings repo, the other non-semver
release in the fleet.
- Releases are made by hand, from a commit that is already pushed:

    ```bash
    gh release create YYYYMMDD docs/riddling.pdf --target <commit>
    ```

  Automating it cannot go in build.yml, which is byte-identical across the fleet.

## How many releases are kept

`pygitpub cleanup` deletes all but the 4 newest releases of every repo, and
that applies to the book too. Decided 2026-10-30: this is fine for the book, so
the release cleanup needs no exception for this repo and older editions are
not kept as releases.
Deleting a release leaves its tag in place, so any old edition can still be
rebuilt from its tag.
