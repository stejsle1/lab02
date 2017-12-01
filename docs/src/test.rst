.. _test-manual:

TEST
====

Documentation can test some **labelord** function to see how they works. 

.. testsetup::

   
   import sys
   from labelord.setupfile import printextra
   from labelord.web import convert_time


For example it checks function *`convert_time(*string*)`' for printing link to GitHub repository:

.. doctest::

   >>> convert_time("stejsle1/lab01")
   'https://github.com/stejsle1/lab01'
   
More information about function *`convert_time(*string*)`' is in :ref:`api-label`

Next example shows how to print messages. In case application in verbose mode add label ``'Need vacation'`` with color ``'FFFFFF'`` into repository ``'stejsle1/myNewSummerRepo'``: 

.. testcode::

   printextra(2, "stejsle1/myNewSummerRepo; Need vacation; FFFFFF", "ADD", 0)

it prints: 

.. testoutput::

   [ADD][SUC] stejsle1/myNewSummerRepo; Need vacation; FFFFFF
   
In case application in normal mode update label ``'Unbreakable'`` with color ``'123456'`` to color ``'654321'`` into repository ``'stejsle1/myNewWinterRepo'`` it prints nothing because application in normal mode prints **only errors** to *stderr* and **summary** to *stdout*. 

So if same command ends with error ``422 - Validation Failed``:

.. testcode::

   printextra(1, "stejsle1/myNewWinterRepo; Unbreakable; 654321; 422 - Validation Failed", "UPD", 1)
   
it prints out:

.. testoutput::

   ERROR: UPD; stejsle1/myNewWinterRepo; Unbreakable; 654321; 422 - Validation Failed
   
In normal mode module prints out a summary (with 2 errors) message:   
   
.. doctest::

   >>> printextra(4+1, str(2) + ' error(s) in total, please check log above', '', 1) 
   SUMMARY: 2 error(s) in total, please check log above  

Flawless case of summary report in verbose mode:   
   
.. doctest::

   >>> printextra(4+2, str(3) + ' repo(s) updated successfully', '', 0) 
   [SUMMARY] 3 repo(s) updated successfully   
   
In quiet mode application prints nothing, neither summary message.   
 
   
     

