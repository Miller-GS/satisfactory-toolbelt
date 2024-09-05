local-setup:
	@echo "Creating virtual environment"
	@python -m venv satisfactory_toolbelt_env
	@echo "Activating virtual environment"
	@source satisfactory_toolbelt_env/bin/activate
	@echo "Upgrading pip"
	@pip install --upgrade pip

requirements:
	@echo "Installing requirements"
	@pip install -r requirements.txt
