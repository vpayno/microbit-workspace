# dioxus-rust-workspace

[![rust](https://github.com/vpayno/dioxus-rust-workspace/actions/workflows/rust.yml/badge.svg?branch=main)](https://github.com/vpayno/dioxus-rust-workspace/actions/workflows/rust.yml)
[![actionlint](https://github.com/vpayno/dioxus-rust-workspace/actions/workflows/gh-actions.yml/badge.svg?branch=main)](https://github.com/vpayno/dioxus-rust-workspace/actions/workflows/gh-actions.yml)
[![spellcheck](https://github.com/vpayno/dioxus-rust-workspace/actions/workflows/spellcheck.yml/badge.svg?branch=main)](https://github.com/vpayno/dioxus-rust-workspace/actions/workflows/spellcheck.yml)

Personal workspace for learning Dioxus & Rust.

## Links

- [Dioxus GitHub](https://github.com/DioxusLabs/dioxus)
- [Dioxus Website](https://dioxuslabs.com/)
- [Rust](https://www.rust-lang.org/)

## [RunMe Playbook](https://runme.dev)

This and other readme files in this repo are RunMe Plabooks.

Use this playbook step/task to update the RunMe cli.

If you don't have runme installed, you'll need to copy/paste the command. :)

```bash { background=false category=runme closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-runme promptEnv=true terminalRows=10 }
go install github.com/stateful/runme/v3@v3
```

## Installing Tools

- Install [Dioxus CLI](https://github.com/DioxusLabs/dioxus/tree/main/packages/cli)

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-tools promptEnv=true terminalRows=10 }
# install tool dependencies

set -e

cargo install dioxus-cli
cargo install cargo-make
cargo install wasm-pack

printf "\n"
set -x

dx --version
cargo make --version
wasm-pack --version

set +x
```
