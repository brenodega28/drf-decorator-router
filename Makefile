deploy:
	python setup.py sdist;
	twine upload dist/*.tar.gz;
	rm -rf dist;
