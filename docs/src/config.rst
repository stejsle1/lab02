.. _config-manual:

CONFIG
======

Configuration can be set by :ref:`configuration file<use-label-config>` or :ref:`options<use-label-options>`.


.. _use-label-config:

Configuration file
------------------

General input to application is configuration file. This file is written in INI format. File is set by option *-c/--config*. Default value is *'./config.cfg'*.

File have to contain section *'github'*, where is placed :ref:`GitHub token<use-label-token>` and :ref:`webhook secret<use-label-webhook>`.

.. code:: 
  
  [github]
  token = YourToken
  webhook_secret = YourWebhook
  
Next acceptable sections are *'repos'*, *'labels'* and *'others'*. Section *'repos'* defines repositories which will be changed. In section will be list of repositories and flag *'on/off'* for making or not making changes on this repository. List of repositories can be empty.

.. code:: 
  
  [repos]
  stejsle1/lab01 = on
  stejsle1/labelord = on
  stejsle1/wator = off
  
Section *'labels'* defines list of labels which will be insert in repository. Every line in section is a pair of name and color. List can be empty. 

.. code:: 
  
  [labels]
  Error = FF0000
  Important = 112233
  
Section *'others'* defines a template repository. This means labels will be change to be same as in template repository.

.. code::

  [others]
  template-repo = stejsle1/wator
  
.. _use-label-token:

GitHub API token
~~~~~~~~~~~~~~~~

To obtain this token log in GitHub. Open a **'Personal setting'**, click to **'Developer settings'**. In section **'Personal access tokens'** click to **'Generate new token'**. It opens a new page with form. Fill a token description and mark **'public-repo'**. This option allows to make changes with repositories. Save this token to personal secret place. 

.. warning:: Never place this token to GitHub or another public place!

.. _use-label-webhook:

GitHub webhook secret
~~~~~~~~~~~~~~~~~~~~~

To be sure a request is really from GitHub there is a option to add a secret item into webhook. Then application reads a header *'X-Hub-Signature'* and checks if this secret was used to create request header. If do then request can be trusted.

To set webhook open your repository and click on **'Settings'**. On left menu click on **'Webhooks'**. On ritgh side click on **'Add webhook'**. On new page fill a form and hit **'Add webhook'**.


.. _use-label-options:

Options
-------

For all settings in config file there is a option.

*-c/--config [name]* 

    Set config file.
    
*-t/--token [token]*

    Set token.
    
*-r/--template-repo [repo]*

    Set template repository (labels will be change to same ones as in this repository).
    
*-a/--all-repos* 

    Changes will be taken in all repos from request **'list_repos'**.
    
*-d/--dry-run*

    Set 'dry run' (application don't make real changes).
    
*-v/--verbose*

    Set verbose mode.
    
*-q/--quiet*

    Set quiet mode (no output).
    
*-h/--host [host]*

    Set hostname for web interface (default 127.0.0.1).
    
*-p/--port [port]*

    Set port for web interface (default 5000).
        
*-d/--debug*

    Set debug mode.
    
    
Environment variables
---------------------  

Last option to set configuration is by environment variables. There is a few variables which are supported.

*GITHUB_TOKEN*

    Set token. Example: GITHUB_TOKEN='YourToken' 

*LABELORD_CONFIG*

    Set config file for web interface. Example: LABELORD_CONFIG='./config.cfg'
    
*FLASK_DEBUG*    

    Set debug mode for web interface. Exaplme: FLASK_DEBUG=true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

