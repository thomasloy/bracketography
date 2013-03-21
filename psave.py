import urllib2

response = urllib2.urlopen("http://www.cbssports.com/collegebasketball/ncaa-tournament/brackets/viewable_men/collegebasketball/teams/")
page_source = response.read()
f = open('pagesave.txt','w')
f.write(page_source)
f.close()