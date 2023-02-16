import os
import sys

query = "insert into table where shit is eqoal to v1 v2 v3 v4"
replace_index = 9

with open ('input.txt') as fd:
    for line in fd:
        updated_query = query.replace('v2', line.strip())
        print (f'{updated_query}')
