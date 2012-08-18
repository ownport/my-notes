# Using Fabric for Deployment

The tool perfectly suited to deployment needs. Install Fabric to our virtualenv like so:

```$ pip install fabric```

Fabric expects a file, *fabfile.py*, to define all of the actions are needed for deployment. The example of fabfile.py:
```python
from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test myapp')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branchname)
```
This will run the tests, commit your branch change, and merge them into master. At this point, a simple "git pull" in your production area becomes your deployment. Another example:
```python
from fabric.api import lcd

def deploy():
    with lcd('/path/to/prod/area/'):
        local('git pull /path/to/dev/area/')
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/command/to/restart/webserver')
```
This will pull changes from the development master branch, run any migrations which have made, run tests, and restart webserver. All in one simple command from the command line. If one of those steps fails, the script stops and reports what happened. 

Example how to use Fabric from command line
```
$ fab prepare_deployment
$ fab deploy
```

### Links

 - [Starting a Django Project the Right Way](http://www.jeffknupp.com/blog/2012/02/09/starting-a-django-project-the-right-way/)
