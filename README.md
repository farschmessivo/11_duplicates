# Anti-Duplicator

The script is going to receive a folder to scan, 
then is going to traverse the directories given and find the duplicated files in the folders.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python3 duplicates.py test
Scanning test...
The following files are identical.
The name could differ, but the content is identical
___________________
Duplicates Found:
		test/malware.jpg
		test/test/malware.jpg
		test/test copy/malware.jpg
___________________


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
