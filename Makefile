WORKFLOWS_DIR := ~/Library/Application\ Support/Alfred/Alfred.alfredpreferences/workflows
BUNDLE_ID := dk.sniarn.alfred-duckduckgo-suggest-workflow

all:

clean-pyc:
	find $(CURDIR)/src -name '*.pyc' -delete

link:
	ln -sFhv $(CURDIR)/src $(WORKFLOWS_DIR)/$(BUNDLE_ID)

unlink:
	rm $(WORKFLOWS_DIR)/$(BUNDLE_ID)

update-lib:
	/usr/bin/python -m pip install --target $(CURDIR)/src --no-compile --upgrade Alfred-Workflow

.PHONY: clean-pyc link unlink update-lib
