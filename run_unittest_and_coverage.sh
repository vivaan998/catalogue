echo "Unit test and code coverage"
coverage run -m unittest discover -s src -v
coverage report --skip-empty --omit="venv*,*test*"
coverage xml --skip-empty --omit="venv*,*test*"