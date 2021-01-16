venv: requirements.txt
	test -d venv || python3 -m venv venv
	venv/bin/pip3 install --upgrade pip setuptools
	venv/bin/pip3 install -Ur requirements.txt
	touch venv/bin/activate