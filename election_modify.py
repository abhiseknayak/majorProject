file = open('elction_imp.tsv', 'r')
l=[]
import csv
for each in file:
    l.append(each)
print(len(l))

l=l[1:]
print(l)

l1=[]
for i in range(0,len(l)):
    if l[i]!='\n':
        a=l[i][:-1]
        l1.append(float(a))
print(len(l1))

for i in range(0,len(l1)):
    if(l1[i]==1.0):
        l1[i]=4.0
    elif(l1[i]==2.0):
        l1[i]=3.0
    elif(l1[i]==3.0):
        l1[i]=2.0
    else:
        l1[i]=1.0
print(len(l1))
print(l1)

with open('elction_imp_final.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['value'])
    for i in range(0,len(l1)):
        tsv_writer.writerow([l1[i]])
        
        
