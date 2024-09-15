build:
	gunicorn -b localhost:8000 -w 4 app.core:omega

black:
	isort app/auth/emails.py
	isort app/auth/forms.py
	isort app/auth/routes.py
	isort app/conf/boost.py
	isort app/conf/setup.py
	isort app/core.py
	isort app/data/load.py
	isort app/home/routes.py
	isort app/mold/models.py
	isort app/user/emails.py
	isort app/user/forms.py
	isort app/user/routes.py
	black -l 79 app/auth/emails.py
	black -l 79 app/auth/forms.py
	black -l 79 app/auth/routes.py
	black -l 79 app/conf/boost.py
	black -l 79 app/conf/setup.py
	black -l 79 app/core.py
	black -l 79 app/data/load.py
	black -l 79 app/home/routes.py
	black -l 79 app/mold/models.py
	black -l 79 app/user/emails.py
	black -l 79 app/user/forms.py
	black -l 79 app/user/routes.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf

tests:
	python3 -m app.tests.test_CPF
	python3 -m app.tests.test_DATE

ready:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -U pip; \
	pip install -r requirements.txt; \
	deactivate

.PHONY: build black clean tests ready
