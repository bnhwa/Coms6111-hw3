# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:20:33 2021

@author: bb339
apriori algorithm for association rules extractor,
algorithm implemented is the variant in 
Section 2.1 of the Agrawal and Srikant paper in VLDB 1994 
"""

from functools import reduce


def get_candidates(itemset, Lk):
    """
    given an itemset and Lk, generate candidates:
    This is the vanilla methodology of doing so.
    See get_candidates_variant() for the methodology 
    in the Agrawal and Srikant paper in VLDB 1994 
    """
    
    k_candidates = []
    for l in Lk:
        #prevent reduncancy in candidate list
        k_candidates += [i for i in \
            list(map(lambda x: l.union(set([x])),itemset.difference(l)))\
            if i not in k_candidates]
    return k_candidates

def get_candidates_variant(itemset,Lk):
    """
    variant of get candidates based on the Agrawal and Srikant paper in VLDB 1994 
    get all the sets of size k possible with Lk,
    then prune those which have a subset of size k-1 which is not in Lk
    """ 
    if Lk == [set()]: # case k = 1
        return [set([i]) for i in itemset]
        
    k_candidates = []
    #get all the sets of size k possible with Lk   
    for a in Lk:
        for b in Lk:
            if not set(b).issubset(a):
                pot_set = set(b).union(a)
                if not pot_set in k_candidates: 
                    k_candidates+=[pot_set]
    # cut candidates which have a subset of size k-1 and is not in L_k
    for c in k_candidates:
        if any(j not in Lk for j in [c.difference([i]) for i in c]):
            k_candidates.remove(c)
    return k_candidates


def get_supports(transactions_in, candidates,verbose = False):
    """
    get supports given transactions and candidates
    """
    if verbose:
        print('computing supports')
    candidate_supports = {frozenset(c): 0 for c in candidates}
    for idx, t in enumerate(transactions_in):
       #maybe print progress if apriori has lots of items to process
        for c in candidates:
            if c.issubset(t):
                candidate_supports[frozenset(c)] += 1

    return {c: candidate_supports[c]/len(transactions_in) for c in candidate_supports}


def apriori(transactions_in, min_support_level,verbose=True):
    """
    args:
        transactions_in: list of transaction sets, e.g.,  [set(1,2,5), set(1,2)]
        min_support_level: minimum support level [0-1]
    outputs:
        (
        result itemset,
        relationships passing minimum threshold
        )
    """
    print("Calculating a-priori algorithn")
    # generate itemset from transactions
    itemset = reduce(lambda x,y: x.union(y), transactions_in)
    # initialize  Lk, k, supports, and return itemset
    Lk, k, supports, return_itemset = [set()], 0, dict(), set()
    while Lk:
        k +=1
        # get candidates
        k_candidates = get_candidates_variant(itemset,Lk)
        # get supports of generated candidates:
        candidate_supports =get_supports(transactions_in, k_candidates,verbose=verbose)
                
        # filter candidates based on confidence:
        Lk = [frozenset(c) for c in k_candidates if candidate_supports[frozenset(c)] >= min_support_level]
       
        # update return itemset
        return_itemset = return_itemset.union(Lk)
        
        #update current supports
        supports.update(candidate_supports)
        

    return return_itemset, supports


def select_rules(itemset_in,supports,min_confidence_level):
    """
    select high confidence-rules given
    input itemset,
    supports,
    minimum confidence level
    
    returns list of tuples of:
        (rule_left,rule_right,confidence,support)
        
 
    """
    #filter out itemset to only process the ones with more than 1 element
    itemset_in = set([i for i in itemset_in if len(i)>1])
    ret_rules = []
    
    for i in itemset_in:
        #get rule splits, then get support and confidence of each
        for (left,right) in [(i.difference([j]), set([j])) for j in i]:
            supp = supports[i]
            conf = supp/supports[left]
            # add rule if confidence passes thresh
            if conf >= min_confidence_level:
                ret_rules+=[(left,right,conf,supp)]
            
            pass
    return ret_rules
if __name__ == '__main__':
    pass
    #test values using http://www.codeding.com/articles/apriori-algorithm
    t_in = [
        set([1,2,5]),
        set([2,4]),
        set([2,3]),
        set([1,2,4]),
        set([1,3]),
        set([2,3]),
        set([1,3]),
        set([1,2,3,5]),
        set([1,2,3]),

        ]
    t_in1= [
    set(["bread", "beer","umbrella"]),
    set(["bread", "beer", "water", "detergent"]),
    set(["beer", "umbrella", "bread"]),
    set(["water", "detergent", "beer", "cheese"]),
    set(["beer"])
        
        ]
    #class example
    t_in2 = [
        set(["pen","ink","diary","soap"]),
        set(["pen","ink","diary"]),
        set(["pen","diary"]),
        set(["pen","ink","soap"]),
        
        ]
    # itemset = reduce(lambda x,y: x.union(y), transactions_in)
    # print(itemset)
    min_support = 0.7
    min_confidence = 0.8
    #get itemsets and supports
    itemset,support = apriori(t_in2,min_support)
    #extract rules
    rules = select_rules(itemset,support,min_confidence)

    #print results
    print("=====Frequent itemsets (min_sup={})=====".format(min_support))
    for i in itemset:
        print("{},{}".format(list(i),support[i]))
    # print(itemset)
    print("=====High-confidence association rules (min_conf={})=====".format(min_confidence))
    # print(rules)
    for left,right,conf,supp in rules:
        print("{}=>{}(Conf:{},Supp:{})".format(list(left),list(right),conf,supp))
    
