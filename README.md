# Rocketman: A Wagtail for Beginners Course

View the production website at [rocketman.learnwagtail.com](http://rocketman.learnwagtail.com)

View the course at [https://learnwagtail.com/wagtail-for-beginners/](https://learnwagtail.com/wagtail-for-beginners/)

> The purpose of this repository is to provide code support form the [Wagtail for Beginners course](https://learnwagtail.com/wagtail-for-beginners/).

## Installation
There are several installation methods. For local development, you have three main options that are used in this course:

#### venv
```bash
python3 -m venv rocketmanvenv
source rocketmanvenv/bin/activate
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

#### pipenv
```bash
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

#### virtualenv
```bash
virtualenv rocketmanvenv
source rocketmanvenv/bin/activate
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Launching your site
Make sure you watch the video on launching your Wagtail CMS site on [Digital Ocean](https://m.do.co/c/7598914bd459). If you decide to clone this project as a test, make sure you update the `@todo`s in `production.py`.

There's also a sample nginx config, and a gunicorn files in the `conf/` directory. That will show you how rocketman.learnwagtail.com is setup.

## Digital Ocean Hosting Perks
If you [use this link](https://m.do.co/c/7598914bd459), you'll get $100 in credit over the first 60 days to setup your Wagtail website using [Digital Ocean](https://m.do.co/c/7598914bd459)

## General dev support
If you have questions about adapting this source code to your project, there are two primary places to turn to:

1. [Slack](https://wagtail.io/slack) — join us in the #support channel.
2. [Learn Wagtail Tutorials](https://wagtail.io/course) — Over 50 free helpful videos on various subjects

## Frontend development
Wagtail for Beginners does _not_ cover any of the frontend build. This was a conscious decision so the course can focus entirely on Wagtail and Django.

But if you want to extend the frontend you can get it setup with `npm i` and run any of the commands in the `package.json` file.
