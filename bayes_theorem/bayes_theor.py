'''
Created on Oct 3, 2012

@author: Joseph Lee
'''
from math import ceil

class BayesTheorem(object):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
    def calc_by_value(self, a):
        total = self._calc_total_val(a)
        b = []
        index = 0
        for x in a:
            category = x[0]
            cat_total = self._get_cat_total(x[2])
            cat_prob = cat_total / total
            b.append((category, cat_prob, []))
            for y in x[2]:
                sub = y[0]
                b[index][2].append((sub, y[1] / cat_total))
            index += 1
        self.add_prob(a, total)
        self.prob_tree(b)
        self.calc_bayes(b)
        
    def calc_by_prob(self, a):
        self.prob_tree(a)
        print()
        print("---------Addition Probability---------------")
        for x in a:
            category = x[0]
            catValue = x[1]
            for y in x[2]:
                print(str.format(
                    "Probability of being from {0} AND {1}: {2}%",
                    category, y[0], ceil(y[1] * catValue * 100)))
        self.calc_bayes(a)
    
    def add_prob(self, a, total):
        print()
        print("---------Addition Probability---------------")
        for x in a:
            category = x[0]
            for y in x[2]:
                print(str.format(
                    "Probability of being from {0} AND {1}: {2}%",
                    category, y[0], ceil(y[1] / total * 100)))
                
                
        
    def calc_bayes(self, a):
        print()
        print("-----------------Bayes Theorem-------------------")
        for i in range(len(a[0][2])):
            denom = self._calc_denom(a, i)
            for x in a:
                category = x[0]
                catProb = x[1]
                sub = x[2][i][0]
                subProb = x[2][i][1]
                print(str.format(
                    "Probability subject is from {0} given from sub-category {1} is: {2}%",
                    category, sub, ceil((catProb * subProb / denom) *100)))
        
    def _calc_denom(self, a, i):
        total = 0
        for x in a:
            total += x[1] * x[2][i][1]
        return total
    
    def _calc_total_val(self, a):
        total = 0
        for x in a:
            for y in x[2]:
                total += y[1]
        return total
    
    def _get_cat_total(self, a):
        total = 0
        for x in a:
            total += x[1]
        return total
    
    def prob_tree(self, a):
        print()
        print("--------------Probability Tree----------------")
        for x in a:
            print(str.format("Probability from Category {0} is: {1}%", x[0], ceil(x[1] * 100)))
            for y in x[2]:
                print(str.format("    Probability from subcategory {0} is: {1}%", y[0], ceil(y[1] * 100)))
    
