
import os, sys
import hashlib


	


def menu():
	
	
	
	print "\n"
	print "\n"
	name = raw_input('Whats your name?') #ask Dr p's name 
	print "\t Menu:"
	print "\t 1) Calculate the Life sum:"
	print "\t 2) Calculate the MD5 checksum:"
	answer = input("")
	
	
	if answer == 1:
		
		print "The Life sum, young %s, is 42..." %name
		menu()
	elif answer == 2:
		print "Ok, lets get started then %s, shall we?" %name
		def get_custom_checksum(input_file_name):
			from datetime import datetime
			start = datetime.now()
			print "Starting Checksum calculation..." 
			from hashlib import md5, sha1
			
			chunk_size = 1048576 # (1024 B)^2 = 1048576 B which is 1 MB
			file_md5_checksum = md5()
			try:
				with open(input_file_name, "rb") as f:
					byte = f.read(chunk_size)
					prev_byte = byte #previous byte
					byte_size = len(byte)
					file_read_iterations = 1 
					
					while byte:
						file_md5_checksum.update(byte)
						prev_byte = byte
						byte = f.read(chunk_size)
						byte_size += len(byte)
						file_read_iterations += 1
			except IOError:
				print "File could not be opened: %s" % (input_file_name)
				return
			except:
				raise 
				
			#storage conversions:
			KB_size = byte_size/1024
			MB_size = KB_size/1024
			GB_size = MB_size/1024 
			bit_size = byte_size*8 # 8 bits in a byte
			kilo_bit_size = bit_size/1000
			mega_bit_size = kilo_bit_size/1000
			giga_bit_size = mega_bit_size/1000
			last_chunk_size = len(prev_byte)
			stop = datetime.now()
			processtime = stop-start
			custom_checksum_profile = {
				'start': start,
				'byte_size': byte_size,
				'KB_size': KB_size, #kilo byte
				'MB_size': MB_size, #Mega byte
				'GB_size': GB_size, #giga byte
				'bit_size': bit_size,
				'kilo_bit_size': kilo_bit_size,
				'mega_bit_size': mega_bit_size,
				'giga_bit_size': giga_bit_size,
				'file_read_iterations': file_read_iterations,
				'last_chunk_size': last_chunk_size,
				'md5_checksum': file_md5_checksum.hexdigest(),
				'processtime': processtime,
				}
			return custom_checksum_profile
#obtained through the following resources
# http://stackoverflow.com/questions/1035340/reading-binary-file-in-python
# http://abstracthack.wordpress.com/2007/10/19/calculating-md5-checksum/
# http://www.speedguide.net/conversion.php
		def print_custom_checksum(input_file_name):
			custom_checksum_profile = get_custom_checksum(input_file_name)
			try:
				print ('Start                 :', custom_checksum_profile['start'])
				print ('File Size (bytes)     :', custom_checksum_profile['byte_size'])
				print ('File Size (kilobytes) :', custom_checksum_profile['KB_size'])
				print ('File Size (megabytes) :', custom_checksum_profile['MB_size'])
				print ('File Size (gigabytes) :', custom_checksum_profile['GB_size'])
				print ('File Size (bits)      :', custom_checksum_profile['bit_size'])
				print ('File Size (kilobits)  :', custom_checksum_profile['kilo_bit_size'])
				print ('File Size (megabits)  :', custom_checksum_profile['mega_bit_size'])
				print ('File Size (gigabits)  :', custom_checksum_profile['giga_bit_size'])
				print ('File Read Iterations  :', custom_checksum_profile['file_read_iterations'])
				print ('Last Chunk (bytes)    :', custom_checksum_profile['last_chunk_size'])
				print ('MD5                   :', custom_checksum_profile['md5_checksum'])
				print ('Stop                  :', custom_checksum_profile['stop'])
				print ('Processing Time       :', custom_checksum_profile['processtime'])
			except TypeError: #  'NoneType' object is not subscriptable --- basically this should happen when the input file could not be opened
				pass
				#should output grrrrr not working- FIXED :DDD thats right dr p! my skillz
				
		import argparse
		script_version='0.0.2'
		parse = argparse.ArgumentParser(description='Determine an input file and its size, and calculate the MD5 checksum.',version=script_version)
		parse.add_argument('-f', '--file', metavar='in-file', action='store', dest='file_name', type=str, required=True, help='name of file to be calculated')
		args = parse.parse_args()
		print('Processing File         :', args.file_name)
		print_custom_checksum(args.file_name)
		menu()

	
def main():
	
	
	print '#' * 49
	print "# WELCOME TO THE MD5 CHECKSUM CALCULATOR        #"
	print "# AUTHOR: MICHAEL REED MCDOW                    #"
	print "# DESCRIPTION: TAKES BINARY FILE ARGUMENT AND   #"
	print "# CALCULATES THE LIFE AND MD5 SUM               #"
	print "# PROF: DR. P^2                                 #"
	print "# CLASS: MATH 3030                              #"
	print "#" * 49

	print "# DISCLAIMER:                                   #"
	print  """# PERMISSION TO USE, COPY, MODIFY, AND/ OR      #
# DISTRIBUTE THIS SOFTWARE FOR ANY PURPOSE      #
# WITH OR WITHOUT FEE IS HEREBY GRANTED,        #
# PROVIDED THAT THE ABOVE COPYRIGHT NOTICE      #
# AND THIS PERMISSION NOTICE APPEAR IN ALL      #
# COPIES.                                       #
#                                               #
# THE SOFTWARE IS PROVIDED "AS IS" AND THE      #
# AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD   #
# TO THIS SOFTWARE INCLUDING ALL IMPLIED        #
# WARRANTIES OF MERCHANTABILITY AND FITNESS.    #
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR    #
# ANY SPECIAL, DIRECT, INDIRECT, OR             #
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES          #
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA   #
# OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, #
# NEGLIGENCE OR OTHER TORTIOUS ACTION,          #
# ARISING OUT OF OR IN CONNECTION WITH THE      #
# USE OR PERFORMANCE OF THIS SOFTWARE.          #"""
	print "#" * 49
	menu()
main()