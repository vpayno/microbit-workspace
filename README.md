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

## Experiments

- [MicroPython](./python/README.md)

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

For [MicroPython Package Management](https://docs.micropython.org/en/latest/reference/packages.html), learing to use `mip` and `mpremote`.

Adafruit MicroPython tutorials:

- [Firmware Loading](https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board)

Install Python/MicroPython language dependencies.

```bash { background=false category=setup closeTerminalOnSuccess=true excludeFromRunAll=true interactive=true interpreter=bash name=setup-install-tools-micropython promptEnv=true terminalRows=10 }
# install python/micropython language dependencies

set -e
set -x

printf "\n"

sudo nala install --no-autoremove -y gcc-arm-none-eabi cmake ninja-build srecord libssl-dev yotta
printf "\n"

python --version
pip install --upgrade mpremote

if [[ ! -d .venv ]]; then
    latest_python_version="$(pyenv versions --bare | grep '^3[.]' | sort -V | tail -n 1)"
    pyenv local "${latest_python_version}"
    pyenv local
    printf "\n"

    latest_mp_version="$(pyenv versions --bare | grep micropython | sort -V)"
    if ! pyenv versions | grep -q "${latest_mp_version}"; then
        pyenv install "${latest_mp_version}"
        pyenv versions
    fi
    printf "\n"

    # can't use pdm with micropython
    # pyenv local "${latest_mp_version}"
    # pyenv local
    # printf "\n"

    pyenv versions
    printf "\n"

    # instead of pip use
    # micropython -m mip install pkgname

    pdm venv create -w virtualenv --with-pip python
    printf "\n"

    pdm use python
    printf "\n"
fi

# create lock file
pdm lock
printf "\n"

# use lock file to update .venv
pdm sync
printf "\n"

set +x
```
