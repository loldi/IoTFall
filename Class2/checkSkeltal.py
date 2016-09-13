import urllib2
import untangle
 
FEED_URL = 'http://mail.google.com/mail/feed/atom/all'
 
def get_read_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='mail.google.com',
        uri='https://mail.google.com',
        user='{user}@newschool.edu'.format(user=user),
        passwd=passwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen(FEED_URL)
    return feed.read()
 
##########

if __name__ == "__main__":
    import getpass
 
    user = raw_input('Username: ')
    passwd = getpass.getpass('Password: ')
    #print get_unread_msgs(user, passwd)
    xml = get_read_msgs(user, passwd)
    o = untangle.parse(xml)
    try:
    	for e in o.feed.entry:
    		if e.title.cdata == "VERY IMPORTANT EMAIL CHECK PLS":

    			print ('VERY IMPORTANT EMAIL YOU MUST RESPOND OR FACE DIRE CONSEQUENCES')
    except IndexError:
    	pass    # no new mail