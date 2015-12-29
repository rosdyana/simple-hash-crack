#! /usr/bin/python
# this tool is develop based on docs.python.org/2/library/hashlib.html
# this is for education purpose only
# writen by Rosdyana Kusuma - rosdyana.kusuma@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
 
import hashlib
import sys
import os
import os.path
 
from hashlib import *
 
#banner
def banner():
  print '''
						   dP		  oo   dP			oo	   dP
						   88			   88					 88
.d8888b. dP.  .dP 88d888b. 88 .d8888b. dP d8888P		  dP .d888b88
88ooood8  `8bd8'  88'  `88 88 88'  `88 88   88   88888888 88 88'  `88
88.  ...  .d88b.  88.  .88 88 88.  .88 88   88			88 88.  .88
`88888P' dP'  `dP 88Y888P' dP `88888P' dP   dP			dP `88888P8
				  88
				  dP   exploit-id.com
'''
banner()
# MD5
def RMX_md5():
	print "======= MD5 Cracking with dictionary ======="
	hash = raw_input("Hash: ")
	word_list = raw_input("Dictionary file: ")
	if os.path.isfile(word_list) and os.access(word_list, os.R_OK):
		f = open(word_list, "r")
		print "\nAttempting to crack... \n"
		checker = True
		for x in f:
			plain_text = x.rstrip('\n')
			encrypted = hashlib.md5(plain_text).hexdigest()
 
			if encrypted == hash:
				print "Hash cracked! Password is %s \n" % plain_text
				checker = False
		if checker:
			print "Your dictionary is not complete."
	else:
		print "\nWordlist file is not found"
	sys.exit()
# SHA1
def RMX_sha1():
	print "======= SHA1 Cracking with dictionary ======="
	hash = raw_input("Hash: ")
	word_list = raw_input("Dictionary file: ")
	if os.path.isfile(word_list) and os.access(word_list, os.R_OK):
		f = open(word_list, "r")
		print "\nAttempting to crack... \n"
		checker = True
		for x in f:
			plain_text = x.rstrip('\n')
			encrypted = hashlib.sha1(plain_text).hexdigest()
 
			if encrypted == hash:
				print "Hash cracked! Password is %s \n" % plain_text
				checker = False
		if checker:
			print "Your dictionary is not complete."
	else:
		print "\nWordlist file is not found"
	sys.exit()
# SHA224
def RMX_sha224():
	print "======= SHA224 Cracking with dictionary ======="
	hash = raw_input("Hash: ")
	word_list = raw_input("Dictionary file: ")
	if os.path.isfile(word_list) and os.access(word_list, os.R_OK):
		f = open(word_list, "r")
		print "\nAttempting to crack... \n"
		checker = True
		for x in f:
			plain_text = x.rstrip('\n')
			encrypted = hashlib.sha224(plain_text).hexdigest()
 
			if encrypted == hash:
				print "Hash cracked! Password is %s \n" % plain_text
				checker = False
		if checker:
			print "Your dictionary is not complete."
	else:
		print "\nWordlist file is not found"
	sys.exit()
# SHA256
def RMX_sha256():
	print "======= SHA256 Cracking with dictionary ======="
	hash = raw_input("Hash: ")
	word_list = raw_input("Dictionary file: ")
	if os.path.isfile(word_list) and os.access(word_list, os.R_OK):
		f = open(word_list, "r")
		print "\nAttempting to crack... \n"
		checker = True
		for x in f:
			plain_text = x.rstrip('\n')
			encrypted = hashlib.sha256(plain_text).hexdigest()
 
			if encrypted == hash:
				print "Hash cracked! Password is %s \n" % plain_text
				checker = False
		if checker:
			print "Your dictionary is not complete."
	else:
		print "\nWordlist file is not found"
	sys.exit()
# SHA384
def RMX_sha384():
	print "======= SHA384 Cracking with dictionary ======="
	hash = raw_input("Hash: ")
	word_list = raw_input("Dictionary file: ")
	if os.path.isfile(word_list) and os.access(word_list, os.R_OK):
		f = open(word_list, "r")
		print "\nAttempting to crack... \n"
		checker = True
		for x in f:
			plain_text = x.rstrip('\n')
			encrypted = hashlib.sha384(plain_text).hexdigest()
 
			if encrypted == hash:
				print "Hash cracked! Password is %s \n" % plain_text
				checker = False
		if checker:
			print "Your dictionary is not complete."
	else:
		print "\nWordlist file is not found"
	sys.exit()
# SHA512
def RMX_sha512():
	print "======= SHA512 Cracking with dictionary ======="
	hash = raw_input("Hash: ")
	word_list = raw_input("Dictionary file: ")
	if os.path.isfile(word_list) and os.access(word_list, os.R_OK):
		f = open(word_list, "r")
		print "\nAttempting to crack... \n"
		checker = True
		for x in f:
			plain_text = x.rstrip('\n')
			encrypted = hashlib.sha512(plain_text).hexdigest()
 
			if encrypted == hash:
				print "Hash cracked! Password is %s \n" % plain_text
				checker = False
		if checker:
			print "Your dictionary is not complete."
	else:
		print "\nWordlist file is not found"
	sys.exit()
#Menu
def Menu():
	print "====== HASH Cracker - Exploit-ID ======"
	print " [1] md5 cracker \n [2] sha1 cracker \n [3] sha224 cracker \n [4] sha256 cracker \n [5] sha384 cracker \n [6] sha512 cracker \n"
	choice = input("Select Hash type: ")
	if choice == 1:
		RMX_md5()
	elif choice == 2:
		RMX_sha1()
	elif choice == 3:
		RMX_sha224()
	elif choice == 4:
		RMX_sha256()
	elif choice == 5:
		RMX_sha384()
	elif choice == 6:
		RMX_sha512()
	else :
		print "please input correct selection"
Menu()
