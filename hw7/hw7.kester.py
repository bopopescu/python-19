#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #7
# October 19, 2014
# Webscraping
#---------------------------------------------------------
import sys
import urllib
from bs4 import BeautifulSoup
import codecs
import re

#Clean up, return string
def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

def main():
    f = codecs.open("restaurants.txt", "a", "utf-8")
    count = 1
    myList = []
    
    urls = ['http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&start=0#', 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco%2C+CA&sortby=rating&start=10', 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco%2C+CA&sortby=rating&start=20', 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco%2C+CA&sortby=rating&start=30']
    
    #Run urllib for each url
    for url in urls:
        try: content = urllib.urlopen(url).read()
        except (ValueError,urllib2.URLError):
            print "Problem fetching URL"
            print "Goodbye!"
            sys.exit()
        content = preprocess_yelp_page(content)
        soup = BeautifulSoup(content)
        soup.prettify()
        results = soup.find_all(class_="biz-name")
        
        for match in results:
            restaurant = match.string
            reviews = match.find_next(class_="review-count rating-qualifier").string

            p = re.compile('(\s*)reviews(\s*)')
            reviewsShort = p.sub('', reviews)

            myList.append([int(reviewsShort),unicode(restaurant)])
           
    #Sort and remove dup listings
    sortedMyList = sorted(set(map(tuple, myList)), reverse=True)
    
    #Write list in sorted order
    for i in enumerate(sortedMyList):
        j = i[1]
        reviews = j[0]
        restaurant = j[1]
        row = str(count) + " " + unicode(restaurant) + ", " + str(reviews) + "\n"
        count += 1
    
        f.write(row)
    
    f.close()

if __name__ == "__main__":
    main()