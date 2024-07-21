.PHONY: run-app
run-app:
	cd ./app && \
	PYTHONDONTWRITEBYTECODE=1 python3 main.py

.PHONY: install-dependencies
install-dependencies:
	pip install -r requirements.txt

.PHONY: run-test
run-test:
	PYTHONDONTWRITEBYTECODE=1 pytest --cov=./ --cov-report=html:./test/result --cov-report=xml:./test/result/coverage.xml
	genbadge coverage -i ./test/result/coverage.xml -o ./test/coverage-badge.svg