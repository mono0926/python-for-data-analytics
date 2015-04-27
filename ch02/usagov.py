__author__ = 'mono'

import json
from collections import defaultdict, Counter

path = 'usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]
print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]


def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

# counts = get_counts(time_zones)
counts = Counter(time_zones)
counts.most_common(10)
print(counts)

def top_counts(count_dict, n=10):
    ck = [(count, tz) for tz, count in count_dict.items()]
    ck.sort()
    return ck[-n:]

print(top_counts(counts))

from pandas import DataFrame, Series
import pandas as pd

frame = DataFrame(records)
# print(frame['tz'].value_counts())

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()

# print(tz_counts)

tz_counts[:10].plot(kind='barh', rot=0)
import matplotlib.pyplot as plt
plt.show()

results = Series([x.split()[0] for x in frame.a.dropna()])
print(results.value_counts()[:8])

cframe = frame[frame.a.notnull()]

import numpy as np

op_systems = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windwos')
print(op_systems[:5])

by_tz_os = cframe.groupby(['tz', op_systems])
print(by_tz_os)

agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts)

indexer = agg_counts.sum(1).argsort()
print(indexer)