deploy:
	python setup.py sdist;
	twine upload dist/*;
	rm -rf dist;
