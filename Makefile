setup:
	python -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt && \
	pip install -e .

kernel:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Virtual environment is not activated. Activating..."; \
		source venv/bin/activate; \
	fi; \
	pip install ipykernel && \
	python -m ipykernel install --user --name financial-report-analyzer

database:
	docker pull postgres && \
	docker run --name some-postgres -e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) -p 5432:5432 -d postgres

lint:
	pre-commit run --all-files

filings:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Virtual environment is not activated. Activating..."; \
		source venv/bin/activate; \
	fi; \
	python scripts/sec_filings_loader.py
