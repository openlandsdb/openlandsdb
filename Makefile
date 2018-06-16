pwd = $(shell basename `pwd`)
ymd = $(shell date "+%Y%m%d")

all: spec docs

archive: all
	tar --exclude='.git*' --exclude='Makefile*' -cvjf $(dest)/$(pwd)-$(ymd).tar.bz2 ./bin ./data ./sources ./LICENSE.md ./CONTRIBUTING.md ./README.md

docs:
	python ./bin/docs.py

spec:
	python ./bin/compile.py > sources/spec/sources-list-`date "+%Y%m%d"`.json
	cp sources/spec/sources-list-`date "+%Y%m%d"`.json sources/spec/sources-list-master.json
