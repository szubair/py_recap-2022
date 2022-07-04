#!/usr/bin/python3
#https://stackoverflow.com/questions/71324781/python-split-dictionary-into-smaller-dictionaries-by-threshold-value
# create a list of dicts
# print the list onebyone

dict01 = {'app01':'0.01', 'app02':'0.5', 'app03':'0.10', 'app04':'0.1', 'app05':'0.02'}
print(dict01)

dicts = [{},{},{}]
dlist = len(dicts)
print('size:', dlist)

dsize = len(dict01) / 3
print('dict items:', round(dsize))

i = 0 
counter = 0
for k,v in dict01.items():
    for i in range(len(dict01)):
        if counter <= dsize:
            print(counter, '-', k, ':', v, '>>', i)
            counter+=1
    i+=1
