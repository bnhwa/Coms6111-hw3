# COMS 6111 HW3

**Team:**

Bailey Nozomu Hwa <bnh2128@columbia.edu>

Nigel Schuster <ns3158@columbia.edu>

## Submitted Files

```
README.md
association_extractor/
	apriori.py
	cli.py
	make_dataset.py
	example-run.txt
	INTEGRATED-DATASET (dataset)
```

## Running the Programs

To generate the dataset, use:

```
python3 make_dataset.py input.csv "CMPLNT_FR_DT" "STATION_NAME" INTEGRATED-DATASET
```

To do the association rule extraction:

```
python3 cli.py INTEGRATED-DATASET <minimum_support> <minimum_confidence>
```



## Internal Design

#### Files used to generate the dataset

**make_dataset.py**: This is the code used to generate our dataset (the **NYPD complaint** dataset described in the "Dataset and Running the Program ")



#### Files used for association rule extraction

**cli.py**: Entry point of the code used for association extraction. `cli.py` takes in as arguments: The CSV formatted dataset, the minimum support, minimum confidence level. `cli.py` calls `apriori.py` which is described below:

**apriori.py**: this files contains the apriori algorithm `apriori()`and association rule extraction `select_rules()` algorithms. Our implementation of the apriori algorithm is the same as that outlined in Section 2.1 of the Agrawal and Srikant paper in VLDB 1994 (our algorithm generates candidates using `get_candidates_variant()` by getting all the sets of size k possible with Lk (Set of large k-itemsets), then cuts those which have a subset of size k-1 which is not in Lk). We also have the vanilla apriori implemented `get_candidates()` just for our own reference; but we do not use this in any way.



## Dataset

In this project we selected a dataset from the public datasets that the city of New York provides and extract association rules using the a-priori algorithm.

We choose the NYPD complaint dataset (https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i). To generate data that we can explore with the a-priori algorithm we chose to consider each date as a basket and consider the station name for which the complaint was made as the item. Entries without a station name are discarded.

To generate the resulting dataset (INTEGRATED-DATASET) use [python3 make_dataset.py input.csv "CMPLNT_FR_DT" "STATION_NAME" INTEGRATED-DATASET].

## Results

We experimented with various cli arguments. [python3 cli.py INTEGRATED-DATASET 0.1 0.5] produced interesting results that we stored in [example-run.txt].

We do see that the algorithm extracts relationships between different subway stations.

Upon examining the correlated stations, we notice that they are usually on the same train line, so that we could attempt to construct a subway map based on this correlation. However, we must also notice that most correlating stations are along the 1/2/3 train. This prompts two possible hypothesis:
- Subway performers are usually a source of nuisance. It could mean that subway performers are more likely to frequent the 1/2/3 train. This does provide an explanation why we observe complaints for long stretches along the same line.
- Analogous to subway performers the explanation could also be theft. Some of the correlations we observed are centered around Columbia University. It seems possible that thieves target Columbia students when they ride the subway.
- The other possibility we considered is that overcrowding could lead to complaints to the NYPD. However, in that case we would have expected to observe similar complaints on other lines (such as the 7 between Grand Central and Court Street)
