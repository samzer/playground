all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run: venv
	FLASK_APP=widget_svm WIDGET_SVM_SETTINGS=../settings.cfg FLASK_DEBUG=1 venv/bin/flask run

test: venv
	WIDGET_SVM_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
