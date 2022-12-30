########################################################################################

.DEFAULT_GOAL := help
.PHONY = test

########################################################################################

test: ## Run shellcheck tests
	shellcheck SOURCES/rbbuild SOURCES/libexec/*.shx
	shellcheck SOURCES/rbdef

help: ## Show this info
	@echo -e '\nSupported targets:\n'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[33m%-18s\033[0m %s\n", $$1, $$2}'
	@echo -e ''

########################################################################################