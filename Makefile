
.PHONY: talks publications ALL

ALL: talks publications

%:: bibtex/%.bib bibtex/%.mustache FORCE
	scripts/bib2ap -f $@ $<

FORCE:
