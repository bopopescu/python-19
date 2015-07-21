from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

import re

WORD_RE = re.compile(r"[\w']+")

class ReviewWordCount(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper1_extract_words(self, _, record):
        """Extract words using a regular expression.  Normalize the text to
        ignore capitalization."""
        for word in WORD_RE.findall(record['text']):
            ###
            # TODO: for each word in the review, yield the correct key,value
            # pair:
            # yield [ ___ , ___ ]
            ##/
            yield [word.lower(), 1]

    def reducer1_count_words(self, word, counts):
        """Summarize all the counts by taking the sum."""
        ###
        # TODO: for each word comes in, yield the aggregate count of list of counts
        # 
        # yield [___, ___ ]
        #
        ##/
        yield [word, sum(counts)]

    def mapper2_bind_words(self, word, total):
        """Binding all words and their counts into the same key. """
        ###
        # TODO: for each word, try to bind them together by assigning them the same key
        #
        # yield [___, [___,___]]
        #
        ##/
        yield ["any", [total, word]] #FIRST WHAT YOU WANT SORTED

    def reducer2_select_word(self, stat, words_counts):
        """ Selecting the top 10 words that are most used in all reviews. """
        ###
        # TODO: try to sort the list of words_counts, and select only the top 10 [word, count] pair
        # finally yield them to screen.
        # 
        # Hint1: 
        #   using sorted(words_count, reverse = True ) to get the sorted list with descending word count 
        # Hint2: 
        #   finally yield each of the word in the sorted list. 
        ##/
        top10_words = sorted(words_counts, reverse=True)[0:10]
        for i in range(len(top10_words)):
            yield [top10_words[i][0], top10_words[i][1]]

    def steps(self):
        return [
            self.mr(self.mapper1_extract_words, self.reducer1_count_words),
            self.mr(self.mapper2_bind_words, self.reducer2_select_word)
        ]


if __name__ == '__main__':
    ReviewWordCount.run()