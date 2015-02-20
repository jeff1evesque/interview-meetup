interview-meetup
================

A coding [exercise](https://github.com/jeff1evesque/interview-meetup/blob/master/data/exercise.md) was given to me when I interviewed for a *Software Engineer* (Tools) position at [Meetup](http://meetup.com/).  Using the supplied [starter-package](https://github.com/jeff1evesque/interview-meetup/releases/tag/0.1), and Meetup API, the exercise was restricted to 3 hours.

This repository provides three [releases](https://github.com/jeff1evesque/interview-meetup/releases):

- Original Starter Package (0.1)
- Submitted Code (1.0)
- Working Code (2.0)

**Note:** the exercise markdown can be found in the [`data/`](https://github.com/jeff1evesque/interview-meetup/blob/master/data/) subdirectory.

## Installation

###Linux Packages

The following packages are needed to be installed:

```
# General Packages:
sudo apt-get install python-pip
sudo pip install Flask
sudo pip install requests
sudo pip install jsonschema
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system. If another system is preferred, simply download the above requirements, with respect to the systems *package manager* equivalent.

## Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/www/html/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/interview-meetup.git
```

Then, change the *file permissions* for the entire project by issuing the command:

```
cd /var/www/html/
sudo chown -R jeffrey:www-data interview-meetup
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /var/www/html/interview-meetup/
git remote add upstream https://github.com/[YOUR-USERNAME]/interview-meetup.git
```

###Flask

Python's [Flask](http://flask.pocoo.org/), is a microframework based on [Werkzeug](http://werkzeug.pocoo.org/).  Specifically, it is a [web framework](http://en.wikipedia.org/wiki/Web_application_framework), which includes, a development server, integrated support for [unit testing](http://en.wikipedia.org/wiki/Unit_testing), [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API, and [Jinja2](http://jinja.pocoo.org/) templating.

This project implements flask, by requiring [`app.py`](https://github.com/jeff1evesque/interview-meetup/blob/master/app.py) to be running:

```
cd /var/www/html/interview-meetup/
python app.py
```

**Note:** the [`run()`](http://flask.pocoo.org/docs/0.10/api/#flask.Flask.run) method within `app.py`, runs the local developement server, and has the ability of defining the host, port, debug feature, and several other options. If none of these attributes are passed into the method, the server will default to running `localhost` on port `5000`, with no [`debug`](http://flask.pocoo.org/docs/0.10/quickstart/#debug-mode) features enabled.

**Note:** when running the above `app.py`, ensure that the terminal window is not used for any other processes, while the web application is available to others.
