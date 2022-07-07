.PHONY: build
.DEFAULT_GOAL := build

help: ## Display callable targets.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

build: ## build pdf file
	@latexmk resume.tex

clean: ## Remove auxillary build files
	@latexmk -c

clean-all: ## Clean build directory
	@latexmk -C

preview: ## Preview pdf file
	@xdg-open build/resume.pdf &> /dev/null
