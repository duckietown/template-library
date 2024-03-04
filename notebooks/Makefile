all_notebooks=$(wildcard *.ipynb)
targets_html=$(patsubst %.ipynb,%.html,$(all_notebooks))
targets_pdf=$(patsubst %.ipynb,%.pdf,$(all_notebooks))

all: $(targets_html)

pdf: $(targets_pdf)

clean: cleanup
	rm -f $(targets_html)  $(targets_pdf)

%.html: %.ipynb
	jupyter nbconvert --to html --execute "$*"

%.pdf: %.html
	wkhtmltopdf $< $@

fatten:
	jupyter nbconvert --inplace --execute *.ipynb

cleanup:
	jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb
