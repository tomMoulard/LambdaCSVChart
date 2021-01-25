ZIP = python.zip
SRC = lambdapythonfunction/

all: zip
all: plan
all: apply
all: clean

test:
	python lambdapythonfunction/lambdapythonfunction.py

install: init
install: all

env:
	export ${shell cat .env}

zip:
	cd ${SRC} && zip -r ${ZIP} . && mv ${ZIP} ..

init:
	terraform init

plan:
	terraform plan

apply:
	terraform apply -auto-approve

destroy:
	terraform destroy

clean:
	$(RM) ${ZIP}

down: destroy
down: clean
up: plan
up: apply
