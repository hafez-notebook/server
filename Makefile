all:
	virtualenv venv && source venv/bin/activate
	pip install -r requirements.txt
	mv core/settings.py.sample core/settings.py

fish:
	virtualenv venv && source venv/bin/activate.fish
	pip install -r requirements.txt
	mv core/settings.py.sample core/settings.py