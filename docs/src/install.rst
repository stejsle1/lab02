.. _install-label:

INSTALL
=======

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

For running commands type (for more information ses :ref:`use-manual`):  
  
.. code:: Python
 
  python3 -m labelord [command options]
  # or
  labelord [command options]


For details about configuration see :ref:`config-manual`.     