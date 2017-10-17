

from googletrans import Translator
import csv
import time

file=open( "gender_refine-csv.csv", "r",encoding='utf-8')
reader = csv.reader(file)
translator = Translator()

with open('translated.csv','w',encoding='utf-8') as file:
    for line in reader:
        line[0]=line[0].replace("'","")
        line[0]=line[0].replace("-"," ")
        #line[0]=line[0].replace("/","")
        if len(line[0]) > 1 and '.' not in line[0]:
            file.write(translator.translate(line[0],dest='ur').text+','+line[1]+','+line[2])
            file.write('\n')
        time.sleep(2)


#for line in reader:
   # t=line[0]
    #if '@' or "w/o" or "d/o" in t:
    #    print(t)
    #writer.writerow(t)


#print(translator.translate('श्रीमती इन्‍द्रा',dest='en'))