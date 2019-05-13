


## Setup dev env

https://github.com/pyenv/pyenv

Brew install pyenv
pyenv local (need to create file .python-version )
pyenv install 3.6.5
pyenv install -l
CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install 3.6.5
pip install virtualenv


### Setting up virtual env

```
virtualenv .virtualenv
source .virtualenv/bin/activate
```

### Install Dependency

```
 pip install -r requirements.txt

```

### Run tests

```
 ./scripts/run_tests.sh 

```

### Nosetest cli

```
https://nose.readthedocs.io/en/latest/usage.html

```
