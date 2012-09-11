# Testing

## python-coverage

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
dummy          12      9    75%   6, 9-10 
test_dummy      9      9   100% 
-----------------------------------------
TOTAL          21     18    86% 
```
coverage.py measures things at the statement level. Thus, even if you get full 100% coverage, it still doesn't test everything. For example, you might test only the first part of code, never the second part, and the second part might be buggy and show up in real life.

On the whole, unit tests are clearer and more reliable if they try to test only a single class at a time. Testing each class is hard to achieve, but a module at a time is easy, and for most projects that's pretty near to testing each class separately.

If you write your code so that each code module has a corresponding test module, then you can run that test module and verify that every line in the code module gets tested.

The code module might use other modules while tested, but only the lines in the code module itself are included in the coverage measurement.

## Links
 
 - [Using coverage.py with Python unittests to ensure good test coverage](http://blog.liw.fi/posts/unittest-coverage/)
