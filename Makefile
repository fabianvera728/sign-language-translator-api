# Define the name of the virtual environment
VENV_NAME := venv

# Define the path to the requirements file
REQUIREMENTS_FILE := requirements.txt

# Define the command to activate the virtual environment
ACTIVATE_VENV := . $(VENV_NAME)/bin/activate

# Define the command to install the dependencies
INSTALL_DEPS := pip install -r $(REQUIREMENTS_FILE)

# Define the command to run the API
RUN_API := uvicorn main:app --port 8000

# Define the default target
.PHONY: build
build: install run

# Define the target to create the virtual environment
.PHONY: venv
venv:
	python3 -m venv $(VENV_NAME)

# Define the target to install the dependencies
.PHONY: install
install: venv
	$(ACTIVATE_VENV) && $(INSTALL_DEPS)

# Define the target to run the API
.PHONY: run
run:
	$(ACTIVATE_VENV) && $(RUN_API) --reload
