# TwittMus - Tweet to Midi Conversion

Track any word or hashtag into Twitter and have each tweet converted into MIDI, or musical information, that is sent to a port on your computer which can then be read by any program reading MIDI information that port number.


# Installation

<strong>1. Download</strong>

You can download this repository directly from GitHub and place the files where you want to run the program from.

<strong>2. Tweepy</strong>

TwittMus uses the Tweepy library to execute to scan for and stream tweets to the program. You must also install the <strong>Tweepy</strong> module. See available instructions on how to install <a href="https://github.com/tweepy/tweepy/tree/v3.5.0">here</a>.

<strong>3. Obtaining Twitter Access</strong>

API authentication is required. Twitter doesn't like anonymous people taking their stuff, so you will need to get special credentials by creating your own app using a Twitter acccount you have accces to. This allow you to fill in the values assigned to the variables <i>ckey</i>, <i>csecret</i>, <i>atoken</i>, and <i>asecret</i> to the file. You can create an using your Twitter account <a href="https://apps.twitter.com/">here</a>.

<strong>3. Opening up a port to receive MIDI</strong>

There are number of ways to accomplish this. Refer to Ableton's guide for Mac and Windows<a href="https://help.ableton.com/hc/en-us/articles/209774225-Using-virtual-MIDI-buses-in-Live">here</a>

# Notes

TwittMus is programmatically set to play the notes assigned to each character in a one-by-one fashion. See the code's comments to learn where you can edit parameters to make your own use of how MIDI information is set.

