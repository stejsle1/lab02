.. _use-manual:

USAGE
=====

If Labelord module is :ref:`installed<install-label>` you can start to use it.

All commands can be run by typing:

.. code:: Python
 
   python3 -m labelord [command options]
   # or
   labelord [command options]
  
All commands and its options are explained below.     

List repos
----------

This :func:`command<labelord.list_repos>` print out all repositories according to given token.

.. code:: Python

   list_repos
   
This code end with error code because no GitHub token was inserted.   
   
If you want to set a configuration file, type:

.. code:: Python

   list_repos -c YourConfigFile.cfg
   # or
   list_repos --config YourConfigFile.cfg 

Token can be also insert via option:

.. code:: Python

   list_repos -t YourToken
   # or
   list_repos --token YourToken
   
.. warning::

   Be sure your token can't be copied or saved in some way by unauthorized person. Secure your confidential data.       

List labels
-----------

This :func:`command<labelord.list_labels>` print out all label from given repository.

.. code:: Python

   list_labels MyNick/MyRepository
   
This code end with error code because no GitHub token was inserted.   
   
If you want to set a configuration file, type:

.. code:: Python

   list_labels -c YourConfigFile.cfg MyNick/MyRepository
   # or
   list_labels --config YourConfigFile.cfg MyNick/MyRepository 

Token can be also insert via option:

.. code:: Python

   list_labels -t YourToken MyNick/MyRepository
   # or
   list_labels --token YourToken MyNick/MyRepository
   
.. warning::

   Be sure your token can't be copied or saved in some way by unauthorized person. Secure your confidential data. 
      
Run
---

This :func:`command<labelord.run>` run a label changes. To run it you must decided if you want to :ref:`update<use-update>` labels or :ref:`replace<use-replace>` labels.

Token can be provided same ways as in commands ``list_repos`` and ``list_labels`` - by config file and by option. To save space thid documentation will be working with configfile-way.

.. warning::

   Be sure your token can't be copied or saved in some way by unauthorized person. Secure your confidential data. 
   

.. _use-update:

Update
~~~~~~

To update label means if your changing repository missing some label, then label will be inserted. If you have some labels which are not in template repository, this labels will be keeped in. Same labels are keep in.

To update labels run:

.. code:: Python

   run update -c YourConfigFile.cfg

If repositories and labels or template repository are set in config file, then this command will make changes fine.

If repositories are not set in config file, you can set to run this changes to all repositories from command ``list_repos`` by typing option ``--all_repos``:

.. code:: Python

   run update -c YourConfigFile.cfg --all-repos
   # or
   run update -c YourConfigFile.cfg -a
   
If nor labels nor template repository are not set in config file, you can set template repository by option ``--template-repo``:

.. code:: Python

   run update -c YourConfigFile.cfg --template-repo YourRepo
   # or
   run update -c YourConfigFile.cfg -r 
   
If you don't want to make change and run it to check what would be changed, run dry_run:

.. code:: Python

   run update -c YourConfigFile.cfg --dry-run
   # or
   run update -c YourConfigFile.cfg -d
   
Command can be run in verbose or quiet mode:

.. code:: Python

   run update -c YourConfigFile.cfg --verbose
   # or
   run update -c YourConfigFile.cfg -v
   
   run update -c YourConfigFile.cfg --quiet
   # or
   run update -c YourConfigFile.cfg -q   
   

.. _use-replace:

Replace
~~~~~~~

To replace label means if your changing repository missing some label, then label will be inserted. If you have some labels which are not in template repository, this labels will be **deleted**. Same labels are keep in.

To replace labels run:

.. code:: Python

   run replace -c YourConfigFile.cfg

If repositories and labels or template repository are set in config file, then this command will make changes fine.

If repositories are not set in config file, you can set to run this changes to all repositories from command ``list_repos`` by typing option ``--all_repos``:

.. code:: Python

   run replace -c YourConfigFile.cfg --all-repos
   # or
   run replace -c YourConfigFile.cfg -a
   
If nor labels nor template repository are not set in config file, you can set template repository by option ``--template-repo``:

.. code:: Python

   run replace -c YourConfigFile.cfg --template-repo YourRepo
   # or
   run replace -c YourConfigFile.cfg -r 
   
If you don't want to make change and run it to check what would be changed, run dry_run:

.. code:: Python

   run replace -c YourConfigFile.cfg --dry-run
   # or
   run replace -c YourConfigFile.cfg -d
   
Command can be run in verbose or quiet mode:

.. code:: Python

   run replace -c YourConfigFile.cfg --verbose
   # or
   run replace -c YourConfigFile.cfg -v
   
   run replace -c YourConfigFile.cfg --quiet
   # or
   run replace -c YourConfigFile.cfg -q

Run server
----------

This :func:`command<labelord.run_server>` run a server - Flask web interface. This command need to has set an envitonment variable ``LABELORD_CONFIG``. This variable contains config file name with configuration (token, webhook secret, ...).

To run a server, type:
 
.. code:: Python

   run_server
   
In this case server will run on 127.0.0.1 on port 5000 (default values). If you want to run server on different host or port, run command:

.. code:: Python

   run_server --host 146.13.306.124 --port 5001
   # or
   run_server -h 146.13.306.124 -p 5001
   
You can run server in debug mode:

.. code:: Python

   run_server --debug
   # or
   run_server -d
   
This mode can be also triggered by environment variable ``FLASK_DEBUG`` with value ``true``.         
