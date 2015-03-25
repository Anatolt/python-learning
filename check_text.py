import urllib
import os

def read_txt():
	quotes = open("quotes.txt")
	content_of_file = quotes.read()
	print(content_of_file)
	quotes.close()
	check_profanity(content_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()

read_txt()
