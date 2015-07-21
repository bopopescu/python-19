import sys
import urllib
from bs4 import BeautifulSoup
import codecs
import re

def preprocess_yelp_page(content):
    ''' Remove extra spaces between HTML tags. '''
    content = ''.join([line.strip() for line in content.split('\n')])
    return content

#################################################################################
# Example code to illustrate the use of preprocess_yelp_page
# You may change these four lines of code


def main():
    f = codecs.open("restaurants.txt", "a", "utf-8")
    
    
    
    
    urls = ['http://www.yelp.com/search?find_desc=restaurants&find_loc=San%20Francisco%2C+CA&start=0#', 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco%2C+CA&sortby=rating&start=10', 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco%2C+CA&sortby=rating&start=20', 'http://www.yelp.com/search?find_desc=restaurants&find_loc=San+Francisco%2C+CA&sortby=rating&start=30']
    
    count = 1
    
    for url in urls:
    
    
    
    

        content = urllib.urlopen(url).read()
        content = preprocess_yelp_page(content) # Now *content* is a string containing the first page of search results, ready for processing with BeautifulSoup

        soup = BeautifulSoup(content)
        soup.prettify()
        results = soup.find_all(class_="biz-name")
        
        for match in results:
            restaurant = match.string
            reviews = match.find_next(class_="review-count rating-qualifier").string

            p = re.compile('(\s*)reviews(\s*)')
            reviewsShort = p.sub('', reviews)
            row = str(count) + " " + restaurant + ", " + reviewsShort + "\n"
            count += 1

            f.write(row)

    f.close()



if __name__ == "__main__":
    main()