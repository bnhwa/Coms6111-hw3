import argparse
from apriori import apriori, select_rules
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Engine to query pages and extract relations")
    parser.add_argument('dataset', help="The CSV formatted dataset")
    parser.add_argument('min_sup', help="The minimum needed support", type=float)
    parser.add_argument('min_conf', help="The minimum confidence needed", type=float)
    args = parser.parse_args()

    with open(args.dataset) as inp:
        data = csv.reader(inp)
        data = [set(list(d)) for d in data]

        #get itemsets and supports
        itemset,support = apriori(data,args.min_sup)
        #extract rules
        rules = select_rules(itemset,support,args.min_conf)

    print("=====Frequent itemsets (min_sup={})=====".format(args.min_sup))
    for i in itemset:
        print("{},{}".format(list(i),support[i]))
    # print(itemset)
    print("=====High-confidence association rules (min_conf={})=====".format(args.min_conf))
    # print(rules)
    for left,right,conf,supp in rules:
        print("{}=>{}(Conf:{},Supp:{})".format(list(left),list(right),conf,supp))
