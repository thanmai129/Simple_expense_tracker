#!/usr/bin/env python

Django's command-line utility for administrative tasks.

import os

import sys

def main():

os.environ.setdefault('DJANGO SETTINGS MODULE", "ExpenseTracker.settings")

try: from django.core.management import execute_from_command_line

except ImportError as exc:

raise ImportError(

"Couldn't import Django. Are you sure it's installed and "available on your PYTHONPATH environment variable? Did you

"forget to activate's virtual environment?"

) from exc

execute_from_command_line(sys.argv)

if name='main': main()