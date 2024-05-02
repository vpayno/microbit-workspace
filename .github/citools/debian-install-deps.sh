#!/usr/bin/env bash

printf "\n"
printf "Installing Debian 12 project dependencies:\n"
printf "\n"

declare deb_pkg
declare -a deb_pkgs=(
	lcov llvm clang clang libclang-dev
	build-essential curl wget libssl-dev
	libwebkit2gtk-4.0-dev libgtk-3-dev libappindicator3-dev librsvg2-dev
	libsoup-3.0-dev libwebkit2gtk-4.1-dev libxdo-dev
	libjavascriptcoregtk-4.1-dev
)

# to reduce resolution conflicts, installing one at a time
time for deb_pkg in "${deb_pkgs[@]}"; do
	sudo apt install -y "${deb_pkg}"
done
