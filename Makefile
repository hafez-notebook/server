all:
	virtualenv venv && source venv/bin/activate
	pip install -r requirements.txt
	mv core/settings.py.sample core/settings.py
