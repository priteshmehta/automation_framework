#!/bin/bash
echo "Running Tests..."

##########################################################################
# Run tests
##########################################################################

nosetests -s --verbosity=2 --logging-level=INFO --logging-format='%(message)s' -l LOG --with-xunitmp --xunitmp-file nosetests.xml ui_tests/test_case1.py 
