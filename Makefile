SHELL := /bin/bash
create-env:
	mkdir .env && cd .env && python -m venv qna-service && source ./qna-service/bin/activate

activate-env:
	cd .env/qna-service && source bin/activate

create-req:
	pip freeze > requirements.txt


