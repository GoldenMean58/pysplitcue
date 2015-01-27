#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# First release: Monday, July 7 10:00:47 2014
# 
#########################################################
# Name: setup.py
# Porpose: script for building Videomass.app and package for install
# Platform: Mac OsX, Gnu/Linux
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2014 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev (01) September 24 2014
# Rev (02) January 21 2015
#########################################################

from distutils.core import setup
from setuptools import setup
import platform
from glob import glob
import sys
import os

VERSION = '0.6.1'
LICENSE = 'Gnu GPL3 (See LICENSE)'
DESCRIPTION = 'cue splitting audio files tool'

LONG_DESCRIPTION = """Small and useful command line program for cue 
splitting audio files when ripped on one track
(with cue-file) to preserve fidelity to original 
CompactDisk.
This work with Wav, Flac and Ape audio formats and 
if need its enable to decode / encode audio-tracks.
Requires the presence of the * .cue file in the same 
directory music track
"""
URL = 'https://github.com/jeanslack/pysplitcue'

 
def glob_files(pattern):
	"""
	this is a simple function for globbing that iterate 
	for list files in dir
	"""
	
	return [f for f in glob(pattern) if os.path.isfile(f)]



def LINUX_SLACKWARE(id_distro, id_version):
	
	
	setup(name = 'pysplitcue',
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		scripts = ['pysplitcue']
		)

def LINUX_DEBIAN_UBUNTU(id_distro, id_version):
	"""
		------------------------------------------------
		setup build videomass debian package
		------------------------------------------------
		
		TOOLS: 
		apt-get install python-all python-stdeb fakeroot

		USAGE: 
		- for generate both source and binary packages :
			python setup.py --command-packages=stdeb.command bdist_deb
			
		- Or you can generate source packages only :
			python setup.py --command-packages=stdeb.command sdist_dsc
			
		RESOURCES:
		- look at there for major info:
			https://pypi.python.org/pypi/stdeb
			http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html
	"""
	
	# this is DATA_FILE structure: 
	# ('dir/file destination of the data', ['dir/file on current place sources']
	# even path must be relative-path
	DATA_FILES = [
		('share/man/man1', ['man/pysplitcue.1.gz']),
				]
	
	DEPENDENCIES = ['python >=2.6']
	EXTRA_DEPEND = {'cuetools':  ["cuetools"],'shntool':  ["shntool"],
					'flac':  ["flac"], 'monkeys-audio':  ["monkeys-audio"], 
					'wavpack':  ["wavpack"]}
	
	setup(name = 'pysplitcue',
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		scripts = ['pysplitcue'],
		data_files = DATA_FILES,
		install_requires = DEPENDENCIES,
		extras_require = EXTRA_DEPEND
		)

	
##################################################

if sys.platform.startswith('linux2'):
	
	dist_name = platform.linux_distribution()[0]
	dist_version = platform.linux_distribution()[1]
	
	if dist_name == 'Slackware ':
		LINUX_SLACKWARE(dist_name, dist_version)
		
	elif dist_name == 'debian' or dist_name == 'Ubuntu':
		LINUX_DEBIAN_UBUNTU(dist_name, dist_version)
		
	else:
		print 'this platform is not yet implemented: %s %s' % (dist_name, dist_version)
		

else:
	print 'OS not supported'
###################################################
