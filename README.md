# Building an API test automation framework with Python

## Setup

Please ensure you have python3 installed on your machine. If not already installed, you can go to python.org and download the latest version of python for your OS and run the installer

Alternatively if you are on mac/linux and have homebrew/linuxbrew already installed then you can install python using below command
```zsh
brew install python
```

Let’s test to make sure python is installed and available from the command line

```zsh
python3 --version
```

Next, Install pipenv:
#### Windows
Open a terminal and write the following command:
```zsh
pip install pipenv
```

#### Mac/Linux
To install pipenv, you can use homebrew on mac/linux
```zsh
brew install pipenv
```
Or, Alternatively, You can also use pip directly with a user installation to install pipenv
```zsh
pip install --user pipenv
```

## Setting up virtualenv
With python setup. The next step that we need to take care of is to set up a virtualenv in which we can install all the required packages. You can just install modules directly on your base python installation but its an accepted best practice to use virtualenvs

```zsh
# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install
```

## Swagger Petstore API
https://petstore.swagger.io/


