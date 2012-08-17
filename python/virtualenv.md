## virtualenv

### Working in virtual environment

virtualenv is a tool to create isolated Python environments.

 * Activate environment 'test-env'

    ```$ source bin/activate```
    
    You should see (test-env) $ at your prompt, letting you know that you're running 
    under the 'env' virtualenv install. 
    
    ```(test-env)$ _```

 * At any time, just type:
 
    ```(test-env)$ deactivate```
    
    to stop using virtualenv.
    
    ```$ _```

 - [virtualenv documentation](http://www.virtualenv.org/en/latest/index.html)
 - [Virtualenv Tutorial](http://simononsoftware.com/virtualenv-tutorial/)

### virtualenvwrapper

virtualenvwrapper is a set of extensions to Ian Bicking’s virtualenv tool. The extensions include wrappers for creating and deleting virtual environments and otherwise managing your development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies.

#### Wrappers

The wrappers provided by virtualenvwrapper are:

 - mkvirtualenv (create a new virtualenv)
 - rmvirtualenv (remove an existing virtualenv)
 - workon (change the current virtualenv)
 - add2virtualenv (add external packages in a .pth file to current virtualenv)
 - cdsitepackages (cd into the site-packages directory of current virtualenv)
 - cdvirtualenv (cd into the root of the current virtualenv)
 - deactivate (deactivate virtualenv, which calls several hooks)

#### Hooks

Hook files can be placed in ENV/bin/ and are simply plain-text files with shell commands. 
virtualenvwrapper provides the following hooks:

 - postmkvirtualenv
 - prermvirtualenv
 - postrmvirtualenv
 - postactivate
 - predeactivate
 - postdeactivate

Add two lines to your .bashrc to set the location where the virtual environments should live 
and the location of the script installed with this package:

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper_bashrc
```

#### Links

 - [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
 - [virtualenvwrapper](http://www.doughellmann.com/articles/pythonmagazine/completely-different/2008-05-virtualenvwrapper/index.html)
 - Rich Leland has created a [short screencast](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/) showing off the features of virtualenvwrapper. 
 - User and developer [documentation](http://virtualenvwrapper.readthedocs.org/)


### pip

Pip stands for pip installs Python packages. It is a replacement for easy_install that provides some great improvements including requirements files and support for version control systems. Requirements files are plain text files that contain a list of packages to be installed. These text files allow you to create repeatable installations.
```
argparse==1.2.1
distribute==0.6.24
wsgiref==0.1.2
```
Once you have a requirements file, Installing a package using pip is as simple as the following command:
```
pip install -r /path/to/requirements.txt
```

To make requirements file
```
pip freeze > /path/to/requirements.txt
```
This will inspect the current environment and generate a requirements files that contains explicit version number for each of the installed packages.

#### Links

 - [Documentation for pip](http://www.pip-installer.org/en/latest/)
 

### Checking what is installed

For listing all installed Python packages we can use yolk. This is a simple console program 
which can list installed packages.

Installation under virtualenv is quite simple:

```(test-env)$ pip install yolk```

Usage is even simpler:

```
(test-env)$ yolk -l
Python          - 2.7.3        - active development (/usr/lib/python2.7/lib-dynload)
argparse        - 1.2.1        - active development (/usr/lib/python2.7)
distribute      - 0.6.24       - active 
pip             - 1.1          - active 
wsgiref         - 0.1.2        - active development (/usr/lib/python2.7)
yolk            - 0.4.3        - active 
```

### Default directory structure after creation virtual environment

```
 (virtualenv)/bin
 (virtualenv)/include
 (virtualenv)/lib
 (virtualenv)/lib/python2.7/
 (virtualenv)/lib/python2.7/distutils
 (virtualenv)/lib/python2.7/site-packages
 (virtualenv)/local
 (virtualenv)/local/bin
 (virtualenv)/local/include
 (virtualenv)/local/lib
```

### Additional directories 

 - (virtualenv)/src is used for all python sources
 - (virtualenv)/run for all runtime data
 - (virtualenv)/log for logs
 - (virtualenv)/data for databases, data files
 - (virtualenv)/etc contains project configuration files, links
 - (virtualenv)/tests contains tests for whole project

### Git repository for sources

Make the ignore file .gitignore. See example below

```
*.py[co]

# Packages
*.egg
*.egg-info
dist
build
eggs
parts
bin
var
sdist
develop-eggs
.installed.cfg

# Installer logs
pip-log.txt

# Unit test / coverage reports
.coverage
.tox

#Translations
*.mo

#Mr Developer
.mr.developer.cfg

# Log files
*.log
```

Create GIT repository in (virtualenv)/src

```
(test-env)$ git init
(test-env)$ git add .
(test-env)$ git commit -m "Initial commit"
```
Adding new files:
```
(test-env)$ git add file_or_folder_name
```
Committing more work:
```
(test-env)$ git commit -m 'commit details'
```

### Links

 - [Setting up a Django environment and project structure](http://www.gyford.com/phil/writing/2010/09/29/django-environment.php)
 
 
