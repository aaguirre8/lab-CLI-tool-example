# lab-CLI-tool-example
This is a lab practice to build a CLI tool

## Setup Project

1. Install virtualenv

```bash
pip install virtualenv
```

2. Create and activate virtualenv
```bash
virtualenv cli_example
source cli_lab/scripts/activate
```

3. Create scaffold

```bash
touch Makefile && touch requirements.txt && touch hello.py && touch test_hello.py
```

. Populate Makefile

```bash
install:
    pip install --upgrade pip &&\\
        pip install -r requirements.txt

test:
    python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
    pylint --disable==R,C hello.py hellocli.py

all: install lint test
```


