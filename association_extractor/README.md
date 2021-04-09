# Extract association rules

In this project we selected a dataset from the public datasets that the city of New York provides and extract association rules using the a-priori algorithm.

We choose the NYPD complaint dataset (https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i). To generate data that we can explore with the a-priori algorithm we chose to consider each date as a basket and consider the station name for which the complaint was made as the item. Entries without a station name are discarded.

To generate the resulting dataset (out.csv) use [python3 make_dataset.py input.csv "CMPLNT_FR_DT" "STATION_NAME" out.csv].

## Results 

We experimented with various cli arguments. [python3 cli.py out.csv 0.1 0.5] produced interesting results that we stored in [out.txt].

We do see that the algorithm extracts relationships between different subway stations.

Upon examining the correllating stations, we notice that they are usually on the same train line, so that we could attempt to construct a subway map based on this correlation. However, we must also notice that most correlating stations are along the 1/2/3 train. This prompts two possible hypothesis:
- Subway performers are usually a source of nuisance. It could mean that subway performers are more likely to frequent the 1/2/3 train. This does provide an explanation why we observe complaints for long stretches along the same line.
- Analogous to subway performers the explanation could also be theft. Some of the correlations we observed are centered around Columbia University. It seems possible that thieves target Columbia students when they ride the subway.
- The other possibility we considered is that overcrowding could lead to complaints to the NYPD. However, in that case we would have expected to observe similar complaints on other lines (such as the 7 between Grand Central and Court Street)
