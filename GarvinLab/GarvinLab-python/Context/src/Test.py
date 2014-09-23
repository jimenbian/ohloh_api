import csv

def Achieve_csv():
#     fr = open('/Users/hakuri/Desktop/result.txt')
    csvf=open('/Users/hakuri/Desktop/test.csv','wb')
    writer=csv.writer(csvf)
    writer.writerow(['userid','newsid'])
    for i in range(1,3000):
        a=int('14521')
        b=int('2563')
        writer.writerow([a,b])
  
   
Achieve_csv()       