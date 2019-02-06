============================================
File transfer
============================================

.. image:: https://travis-ci.com/alynnefs/FileTransfer.svg?branch=master
    :target: https://travis-ci.com/alynnefs/FileTransfer
    :alt: Test Status

This project transfers files based on their name.

Installation
=======

Firstly, clone the project. 

If you don't have, install Python3. This project uses only standard Python libraries.

Requirements
=======

- Python 3.6.7

Configuration file (config_file.yaml)
=======

.. code-block:: yaml
   
   source: str
   # files folder path 

   target: str
   # target path

   mode: int
   # 1 to transfer all files matched
   # 2 to transfer the most recent or the oldest file that matched

   recent: boolean
   # Mode 1:
   #     Indifferent. You may erase this line.
   # Mode 2:
   #     True to the most recent
   #     False to the oldest

   period: int
   # time in seconds

   regex: str
   # example '(.*.txt)'
   # regex to search files

Execution
=======

.. code-block:: console
   
   python3 script.py
   
Examples of execution
=======

- Mode 1: This mode moves all file matches in each period

"Consider two directories, A and B. We have the files 'coolFile.zip' and 'uglyFile.zip' on the directory A and nothing on directory B. Our program will check at each 60 seconds for files on directory A, and will look for files that match a **'cool' prefix**. After 60 seconds, it will transfer 'coolFile.zip' to directory B. After that, it will keep looking for files under
directory A until it is killed."

config_file.yaml

.. code-block:: yaml
   
   source: 'a/'
   target: 'b/'
   mode: 1
   period: 60
   regex: '(cool.*)'

- Mode 2 (the most recent): This mode moves the most recent file match in each period

"This mode would also transfer files based on the filename, but only **the most recent** file available on the source directory. This second mode of operation should be configured through the configuration file with a tag, enabling easyswitch between modes of operation through a simple tag."

config_file.yaml

.. code-block:: yaml
   
   source: 'a/'
   target: 'b/'
   mode: 2
   recent: True # True to the most recent
   period: 60
   regex: '(.*.zip)'
   
- Mode 2 (the oldest): This mode moves the oldest file match in each period

"This mode would also transfer files based on the filename, but only **the oldest** file available on the source directory. This second mode of operation should be configured through the configuration file with a tag, enabling easyswitch between modes of operation through a simple tag."

config_file.yaml

.. code-block:: yaml
   
   source: 'a/'
   target: 'b/'
   mode: 2
   recent: False # False to the oldest
   period: 60
   regex: '(.*.zip)'
   
Tests
=======

.. code-block:: console
   
   python3 tests.py
