########################################################################################

.DEFAULT_GOAL := help
.PHONY = test

########################################################################################

get-shellcheck: ## Download and install the latest version of shellcheck (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nDownloading shellcheck…\n\e[0m"
	curl -#L -o shellcheck-latest.linux.x86_64.tar.xz https://github.com/koalaman/shellcheck/releases/download/latest/shellcheck-latest.linux.x86_64.tar.xz
	tar xf shellcheck-latest.linux.x86_64.tar.xz
	rm -f shellcheck-latest.linux.x86_64.tar.xz
	cp shellcheck-latest/shellcheck /usr/bin/shellcheck || :
	rm -rf shellcheck-latest

	@echo -e "\e[1;32;49m\nShellcheck successfully downloaded and installed!\n\e[0m"

test: ## Run shellcheck tests
	shellcheck SOURCES/rbbuild SOURCES/libexec/*.shx
	shellcheck SOURCES/rbdef
	shellcheck SOURCES/mass-builder

install: ## Install app to current system (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nInstalling app…\n\e[0m"
	install -dDm 755 /usr/libexec/rbbuild
	install -dDm 755 /usr/local/share/rbbuild
	install -pm 755 SOURCES/rbbuild /usr/bin/
	install -pm 755 SOURCES/rbdef /usr/bin/
	install -pm 644 SOURCES/libexec/* /usr/libexec/rbbuild/
	install -pm 644 SOURCES/defs/* /usr/local/share/rbbuild/

	@echo -e "\e[1;32;49m\nApp successfully installed!\n\e[0m"

uninstall: ## Uninstall app from current system (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nUninstalling app…\n\e[0m"
	rm -f /usr/bin/rbbuild || :
	rm -f /usr/bin/rbdef || :
	rm -rf /usr/libexec/rbbuild || :
	rm -rf /usr/local/share/rbbuild || :

	@echo -e "\e[1;32;49m\nApp successfully uninstalled!\n\e[0m"

help: ## Show this info
	@echo -e '\nSupported targets:\n'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[33m%-18s\033[0m %s\n", $$1, $$2}'
	@echo -e ''

########################################################################################
