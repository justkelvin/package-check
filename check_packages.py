#!/usr/bin/env python3
# -*- coding: utf-8 -*-

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from shutil import which

# Check if specific packages is installed before running a code.
# Add the packages to check in the list pkgs = []

print(G + '[+]' + C + ' Checking Dependencies...' + W)
pkgs = ['python', 'pip3', 'testpackage']
installed = True
for pkg in pkgs:
	present = which(pkg)
	if present == None:
		print(R + '[-] ' + W + pkg + ' is not Installed!')
		installed = False
	else:
		print(G + '[+] ' + W + pkg + W + ' already installed')

if not installed:
	print("\nPlease install missing dependancies!")
	exit(1)

print("Dependancies satisfied!")


# The rest of your code goes here