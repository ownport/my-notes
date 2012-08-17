## virtualenv

### Working in virtual environment

 * Activate environment 'test-env'

    ```$ source bin/activate```
    
    You should see (test-env) $ at your prompt, letting you know that you're running 
    under the 'env' virtualenv install. 
    
    ```(test-env)$ _```

 * At any time, just type:
 
    ```(test-env)$ deactivate```
    
    to stop using virtualenv.
    
    ```$ _```

 * [Virtualenv Tutorial](http://simononsoftware.com/virtualenv-tutorial/)

### virtualenvwrapper

 -  [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/)
 - Rich Leland has created a [short screencast](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/) showing off the features of virtualenvwrapper. 
 - User and developer [documentation](http://virtualenvwrapper.readthedocs.org/)


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

### Git repository for codes


### Links

 * [Setting up a Django environment and project structure](http://www.gyford.com/phil/writing/2010/09/29/django-environment.php)
 
 
