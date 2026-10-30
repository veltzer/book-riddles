# Releases of the book

Every successful build of master makes a GitHub release, by
`.github/workflows/release.yml`. Each release carries one asset: riddling.pdf,
the book as committed in docs/riddling.pdf at the commit that was built, which
is the same file GitHub Pages serves (Pages here serves master:/docs).

- Tags are the build run's UTC creation time, YYYYMMDD-HHMMSS, since the book
  has no version number and there can be several builds a day. Re-running a
  build finds its release already there and makes no second one. (The first
  release, 20261030, was made by hand, before this workflow existed.)
- The release is a workflow of its own, triggered by the build finishing,
  because build.yml is byte-identical across the fleet. book-openbook releases
  its books the same way.
- The title page of each release's PDF shows the commit it was built from,
  usually the one before the released commit, since the PDF is built before
  it is committed.

## How many releases are kept

`pygitpub cleanup` deletes all but the 4 newest releases of every repo, and
that applies to the book too. Decided 2026-10-30: this is fine for the book, so
the release cleanup needs no exception for this repo and older editions are
not kept as releases.
Deleting a release leaves its tag in place, so any old edition can still be
rebuilt from its tag.
