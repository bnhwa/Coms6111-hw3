import argparse
import csv
from collections import defaultdict
from tqdm import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Engine to query pages and extract relations")
    parser.add_argument('dataset', help="The CSV formatted dataset")
    parser.add_argument('group_by_col', help="")
    parser.add_argument('output_col', help="")
    parser.add_argument('output')
    args = parser.parse_args()

    with open(args.dataset) as inp, open(args.output, 'w') as out:
        data = csv.reader(inp)
        out = csv.writer(out)
        grouped = defaultdict(list)
        headers = next(data, None)
        group_col_idx = headers.index(args.group_by_col)
        output_col_idx = headers.index(args.output_col)
        for row in tqdm(data):
            grouped[row[group_col_idx]].append(row[output_col_idx])
        for row in tqdm( grouped.values() ):
            out.writerow(row)
