import re
#text = './regex_sum_42.txt'
text = 'regex_sum_1378882.txt'

numlist = list()
with open(text) as f:
    mylist = [line.rstrip('\n') for line in f]
    for i in mylist:
        #print(i)
        total = re.findall('([0-9]+)',i)
        #print('total:',total)
        #if len(total) != 1:
        #    continue
        for number in total:
            num = int(number)
            numlist.append(num)

print(sum(numlist), len(numlist))