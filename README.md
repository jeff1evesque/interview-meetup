interview-meetup
================

A coding [exercise](https://github.com/jeff1evesque/interview-meetup/blob/master/data/exercise.md) was given to me when I interviewed for a *Software Engineer* (Tools) position at [Meetup](http://meetup.com/).  Using the supplied [starter-package](https://github.com/jeff1evesque/interview-meetup/releases/tag/0.1), Meetup API, the exercise was restricted to 3 hours.

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

####GIT Submodule

We need to initialize our git *submodules*:

```
sudo git submodule init
sudo git submodule update
```

The above two commands will update submodules within the cloned repository, according to the versioned master branch. If they are already initialized in the cloned repository, then the latter command will suffice.

The following updates submodule(s):

```
cd /var/www/htmls/interview-meetup/
git checkout -b NEW_BRANCH master
cd [YOUR_SUBMODULE]/
git checkout master
git pull
cd ../
git status
```

to the latest code-base, within the cloned repository branch, `NEW_BRANCH`.
