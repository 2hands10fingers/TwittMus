from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'Xwk45yibY06n7wHFHuoI2KVhi'
csecret = 'uWbOJZdRTmLDFKIxJKoR3huDwprOqefpwctEMIfE3gXfwruN5H'
atoken = '3096677539-t2d26ZLh1YbciYRub7TtGfEvrhF5MxhRTsNjuIb'
asecret = 'N4sSNMBw0TLG8yEwcGRAL15bSSeK1oO8SBZG63B8WiE9s'

""" MIDI NOTES ASSIGN nos harps or flats

c = E4 = 64
d = F4 = 65 
e = G4 = 67
f = A4 = 69
g = B4 = 71

h = C5 = 72
i = E5 = 75
j = F5 = 76
k = G5 = 77
l = A5 = 79
m = B5 = 83

n = C6 = 84
o = D6 = 86
p = E6 = 88
q = F6 = 89
r = G6 = 91
s = A6 = 93
t = B6 = 95

u = C7 = 96
v = D7 = 98
w = E7 = 100
x = F7 = 101
y = G7 = 103
z = A7 = 105
"""

""" SAVING TO CSV ????

class listener(StreamListener):
	def on_data (self, data)
	try:
		print data
		saveFile = open('twitDB.csv', 'a')
		saveFile.write(data)
		saveFile.write('\n')
		saveFile.close()
		return True
	except BaseException, e:
		print 'failed ondata,', str(e)
		time.sleep(5)

"""

""" class listener(StreamListener):
	def on_dataa(self, data):
		#print data
		tweet = data.split(',"text":"')[1].split('","source')[0]
		time.sleep(5)
		print tweet
		return True
	
	def on_error(self, status):
		print status """

class Listener(StreamListener):
	def on_data (self, data):
		tweet = data.split(',"text":"')[1].split('","Liksource')[0]
		for letter in tweet:
			number = ord(letter)
			print (letter)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["keyword"])
