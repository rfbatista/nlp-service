SHELL := /bin/bash
create-env:
	mkdir .env && cd .env && python3 -m venv qna-service && source ./qna-service/bin/activate

activate-env:
	source .env/qna-service/bin/activate

create-req:
	pip freeze > requirements.txt

start:
	python ./src/main.py

