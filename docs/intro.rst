INTRO
=====

This is a command-line application with Flask web interface. It allows to manage labels from GitHub issues. Goal of project is to make it easy to manage labels for multiple repositories and not to create same labels for all repositories. 

Application can list all repositories or all labels of issues in given repository. Application can update or replace labels with labels from another source. Finally application can run a Flask web interface.

Application is :ref:`installed<install-label>` as Python module. For examples how to run commands see :ref:`use-manual` or :ref:`test-manual`.

Application need a GitHub API token for connection to GitHub. This token can be used to access the GitHub API and allows you to see some details of repositories. Manual for obtaining this token is in section :ref:`use-label-token`. Web interface need a webhook for connection to GitHub. Manual for obtaining this webhook is in section :ref:`use-label-webhook`. 

Part of application can be set by configuration file or options. Config file is writen in INI format. See more details in :ref:`use-label-config`. Details about options are in :ref:`use-label-options`. 
