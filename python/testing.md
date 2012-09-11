# Testing

[coverage.py](http://nedbatchelder.com/code/modules/coverage.html) is a generic tool: it only reports the lines that are executed, or not executed. To make it useful for measuring test coverage, we report which lines are not executed during a test run.

```
$ rm .coverage
$ python-coverage -x tests/test_dummy.py
.
---------------------------------------
Ran 1 test in 0.000s

OK
$ python-coverage -rm -o /usr 
Name        Stmts   Exec  Cover   Missing
-----------------------------------------
dummy          12      9    75%   6, 14-15 
test_dummy      9      9   100% 
-----------------------------------------
TOTAL          21     18    86% 
```

## Links
 
 - [Using coverage.py with Python unittests to ensure good test coverage](http://blog.liw.fi/posts/unittest-coverage/)
