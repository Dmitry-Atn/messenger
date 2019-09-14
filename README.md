# messenger

Simple API for messaging service

## Warning

This system still being under development

## Installation

### Requirements
- OS Windows / *nix
- python 3.7
- pip
- git

Execute in command line
```buildoutcfg
git clone git@github.com:Dmitry-Atn/messenger.git
cd messenger
pip install requirements.txt
```

## Usage

```buildoutcfg
cd api_messenger
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Then use [Postman](https://www.getpostman.com/) with following [collection](https://www.getpostman.com/collections/0f817d6e4215eca5880d). 

## Features
- [x] Django REST framework token authentication
- [x] CRUD messages
- [x] Read/unread statuses
