l=[]

import csv
for i in range(2011,2021):
    for j in range(1,13):
        print(i," ",j)
        val=float(input("enter 1 for national+state /2 for national only/3 for state only /4 for no election"))
        l.append(val)

with open('elction_imp.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['value'])
    for i in range(0,len(l)):
        tsv_writer.writerow([l[i]])
