import urllib
def read_text():
	quotes = open("/home/hemant1996/Programming/Nanodegree/check.txt")
	file_contents = quotes.read()
	print file_contents
	quotes.close()
	check_profanity(file_contents)
def check_profanity(text):
	connection = urllib.urlopen('https://www.codechef.com/APRIL16?order=desc&sortBy=successful_submissions')
	output = connection.read()
	print output
	connection.close()
read_text()