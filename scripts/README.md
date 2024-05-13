# Publications from bibtex

The script `bib2ap` converts a `bibtex` file to papers under `_publications`.
Run as
```
  scripts/bib2ap bibtex/publications.bib
```
This will generate one file per publication under `_publications`, using the template in `bibtex/publications.mustache`. Similarly
```
  scripts/bib2ap -f talks bibtex/talks.bib
```
will generate a list of talks under the `_talks` directory. Run
`scripts/bib2ap -h` for additional options. Options can also be given in the 
config file, `bib2aprc`.

