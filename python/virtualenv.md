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

```
 (virtualenv)/src
 (virtualenv)/var
 (virtualenv)/var/run
 (virtualenv)/var/log
```

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


### Links

 * [Virtualenv Tutorial](http://simononsoftware.com/virtualenv-tutorial/)
 
