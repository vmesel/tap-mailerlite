
TARGETVENV=.target-venv
ACTIVATE_TARGET=. .target-venv/bin/activate
TARGETPYTHON=$(TARGETVENV)/bin/python3

DISCVENV=.disc-venv
ACTIVATE_DISC=. .disc-venv/bin/activate
DISCPYTHON=$(DISCVENV)/bin/python3

.PHONY: load-sample-data

.PHONY: discovery-prep
discovery-prep:
	echo "\n\nCreating the environment for singer-discovery\n\n"
	python -m venv $(DISCVENV)
	@$(ACTIVATE_DISC)
	$(DISCPYTHON) -m pip install -r requirements-discovery.txt


load-sample-data:
	echo "\n\nThis command will use Poetry as the Python venv\n\n"
	mkdir -p output/txts/
	poetry run tap-mailerlite --config .secrets/config.json --catalog catalogs/subscribers_catalog.json > output/txts/subscribers_output.txt
	poetry run tap-mailerlite --config .secrets/config.json --catalog catalogs/groups_catalog.json > output/txts/groups_output.txt
	poetry run tap-mailerlite --config .secrets/config.json --catalog catalogs/campaigns_catalog.json > output/txts/campaigns_output.txt


.PHONY: targetcsvenv-prep
targetcsvenv-prep:
	echo "\n\nCreating the environment for target-csv\n\n"
	python -m venv $(TARGETVENV)
	@$(ACTIVATE_TARGET)
	$(TARGETPYTHON) -m pip install -r requirements-target.txt


.PHONY: process-sample-data

process-sample-data:
	echo "\n\nMake sure you are on the environment that target-csv is installed at\n\n"
	cat output/txts/subscribers_output.txt | target-csv
	cat output/txts/groups_output.txt | target-csv
	cat output/txts/campaigns_output.txt | target-csv