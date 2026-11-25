import Levenshtein
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from jarowinkler import jarowinkler_similarity

class NameMatchScorer: 
  """Interface for scoring putative name matches"""

  def __init__(self, name1, name2, threshold = 0.5): 
   self.name1 = name1 
   self.name2 = name2 
   self.threshold = threshold
 
  def __str__(self):
   name1 = f'{self.name1[:30]}...'
   name2 = f'{self.name2[:30]}...'
   return f'{name1}, {name2}'

 
  def __repr__(self): 
   # !r produces python representation
   return f"{self.__class__.__name__}({self.name1!r}, {self.name2!r})"
 
  def score(self, name1, name2):
   pass

# Subclass to calculate score
class ExactMatch(NameMatchScorer):
    """Subclass for exact name to overwrite the score method from above"""

    def score(self, name1, name2):
        if name1 == name2:
          return 1
        else:
          return 0

class Jaccard(NameMatchScorer):
   """Subclass for Jaccard to overwrite the score method from above"""
   def score(self, name1, name2):
    num = len(set(name1).intersection(set(name2)))
    denom = len(set(name1).union(set(name2)))
    return num/denom


class LevenshteinScore(NameMatchScorer):
   """Subclass for Levenshtein to overwrite the score method from above"""
   def score(self, name1, name2):
      return Levenshtein.ratio(name1, name2)


class Tfidf_matcher(NameMatchScorer):
    def __init__(self, name1 = "", name2 = "", threshold=0.5, ngram_range=(1, 4)):
        super().__init__(name1, name2, threshold)
        self.ngram_range = ngram_range
        # Check the range
        min_value = self.ngram_range[0]
        max_value = self.ngram_range[1]
        
        if not(min_value >= 1 and max_value <= 4) or not(min_value <= max_value):
            raise ValueError("N-gram range must be between 1 and 4")


    def fit_vector(self, train_file):
       Tfidf_matcher.vectorizer = TfidfVectorizer(analyzer="char", ngram_range=self.ngram_range)
       X = Tfidf_matcher.vectorizer.fit_transform(train_file)
       return X

    def score(self, name1, name2):
        # Must pass through a list which is why I am using [ ]
        name1 = self.vectorizer.transform([name1])
        name2 = self.vectorizer.transform([name2])
        cos_sim = cosine_similarity(name1,name2)
        # Extract first score
        return cos_sim[0,0]


class Jarowinkler(NameMatchScorer):
   def score(self, name1, name2):
      return (jarowinkler_similarity(name1,name2))