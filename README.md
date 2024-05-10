# microbit-rust-workspace

[![rust](https://github.com/vpayno/microbit-rust-workspace/actions/workflows/rust.yml/badge.svg?branch=main)](https://github.com/vpayno/microbit-rust-workspace/actions/workflows/rust.yml)
[![actionlint](https://github.com/vpayno/microbit-rust-workspace/actions/workflows/gh-actions.yml/badge.svg?branch=main)](https://github.com/vpayno/microbit-rust-workspace/actions/workflows/gh-actions.yml)
[![spellcheck](https://github.com/vpayno/microbit-rust-workspace/actions/workflows/spellcheck.yml/badge.svg?branch=main)](https://github.com/vpayno/microbit-rust-workspace/actions/workflows/spellcheck.yml)

Personal workspace for learning to use the Microbit with Rust, TinyGo and Python.

## Links

- [Microbit GitHub](https://github.com/bbcmicrobit)
- [Microbit Adafruit](https://learn.adafruit.com/category/micro-bit)
- [Rust](https://github.com/nrf-rs/microbit)
- [TinyGo](https://tinygo.org/docs/reference/microcontrollers/microbit/)
- [MicroPython](https://github.com/bbcmicrobit/micropython)

## RunMe Playbook

This and other readme files in this repo are RunMe Plabooks.

Use this playbook step/task to update the [RunMe](https://runme.dev) cli.

If you don't have runme installed, you'll need to copy/paste the command. :)

```bash { background=false category=runme closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-runme promptEnv=true terminalRows=10 }
go install github.com/stateful/runme/v3@v3
```

Install Playbook dependencies:

```bash { background=false category=runme closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-runme-deps promptEnv=true terminalRows=10 }
go install github.com/charmbracelet/gum@latest
```

## Installing Tools

Install generic tools dependencies.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-tools-generic promptEnv=true terminalRows=10 }
# install generic tool dependencies

set -e
set -x

printf "\n"

sudo nala install --no-autoremove -y gcc-arm-none-eabi

set +x
```

Install Rust language dependencies.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-tools-rust promptEnv=true terminalRows=10 }
# install rust language dependencies

set -e
set -x

printf "\n"

sudo nala install --no-autoremove -y gcc-arm-none-eabi

cargo install probe-rs
cargo install flip-link

set +x
```

Install TinyGo language dependencies.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-tools-tinygo promptEnv=true terminalRows=10 }
# install tinygo language dependencies

set -e
set -x

printf "\n"

sudo nala install --no-autoremove -y gcc-arm-none-eabi

go install github.com/tinygo-org/tinygo@latest

set +x
```
