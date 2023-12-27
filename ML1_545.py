import csv
numofattributes = 6
a = [] 
print("\n The Given Training Data Set \n")
with open('/content/sample_data/Find S dataset - Find S dataset.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        a.append (i)
        print(i)

h = [0] * numofattributes
print(h)

for j in range(0,numofattributes):
    h[j] = a[0][j] 
    
for i in range(0,len(a)):
    if a[i][numofattributes]=='Yes':
        for j in range(0,numofattributes):
            if a[i][j]!=h[j]:
                h[j]='?'
            else :
                h[j]= a[i][j] 
    
print(h)
