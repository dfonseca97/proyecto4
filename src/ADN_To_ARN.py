import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime

def main():
 
 start = datetime.now()
 directory = sys.argv[1]

 fna = [filename for filename in listdir(directory) if filename[-3:] == ".fa"]  
 
 for fnafile in fna:
  
  fileName =  directory + fnafile
  print "File: " + fileName
  f = open(fileName, 'r')
  res = open('/opt/dna/results/' + fnafile + '.result', 'w')
  resLine = ""

  for line in f:

   if line[0] == '>': continue
  

   for i in line:
    if i == 'T':
     resLine += 'A'
    elif i == 'A':
     resLine += 'U'
    elif i == 'C':
     resLine += 'G'
    elif i == 'G':
     resLine += 'C'  
    else:
     resLine += i
   resLine += '\n'
  res.write(resLine)

  f.close()   
  res.close()
  
 end = datetime.now()
 total = end - start
 total_time = total.seconds
 print("Total time: " + str(total_time) + "s")

if __name__ == '__main__':
 main()
