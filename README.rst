Labelord
========

Labelord is command-line application with Flask web interface allowing manage labels from GitHub issues.

Intro
-----

This is a command-line application with Flask web interface. It allows to manage labels from GitHub issues. Goal of project is to make it easy to manage labels for multiple repositories and not to create same labels for all repositories. 

Application can list all repositories or all labels of issues in given repository. Application can update or replace labels with labels from another source. Finally application can run a Flask web interface.

Install
-------

Labelord application is install as Python module. Module can be downloaded from PyPi ``https://test.pypi.org/project/labelord-stejsle1/`` or from GitHub repository ``https://github.com/stejsle1/labelord/releases`` as latest release.

After you download it you can install it.

Move to folder with extract files. To make a module from file run:

.. code:: Python
 
  python3 setup.py sdist
  
It will make a dist folder with distribution. To install module run:

.. code:: Python

  python3 -m pip install dist/Labelord-Version.tar
  
Command will automatically install required modules.

Now the Labelord module is install and you can run application:

.. code:: Python
  
  # For help type:
  python3 -m labelord
  # or
  labelord

For running commands type:  
  
.. code:: Python
 
  python3 -m labelord [command options]
  # or
  labelord [command options]
  
Documentation
-------------

Documentation is save in ``docs`` folder in module. To set documentation into HTML format run:

.. code::
   
   cd docs
   make html
   
Now in ``docs`` folder is placed file ``'index.html'`` with documentation.   

Documentation also contains tests. Tests can be checked be running command:

.. code::
   
   make doctest  


License
-------

This project is licensed under the CCO License - see LICENSE file for more information.