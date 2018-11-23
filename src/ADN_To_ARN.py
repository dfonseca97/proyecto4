import sys
from os import listdir
from os.path import isfile, join

def main():
 directory = sys.argv[1]

 fna = [filename for filename in listdir(directory) if filename[-4:] == ".fna"]  
 
 for fnafile in fna:
  
  fileName =  directory + '/' + fnafile
  #print "File: " + fileName
  f = open(fileName, 'r')
  res = open('../results/' + fnafile + '.result', 'w')
  
  for line in f:

   if line[0] == '>': continue
   resLine = ""

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
   res.write(resLine)

  f.close()   
  res.close()

if __name__ =='__main__':
 main()
