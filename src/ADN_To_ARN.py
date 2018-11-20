import sys
from os import listdir
from os.path import isfile, join

def main():
 directory = sys.argv[1]

 fna = [filename for filename in listdir(directory) if filename[-4:] == ".fna"]  
 
 for fnafile in fna:
  
  fileName =  directory + '/' + fnafile
  print "File: " + fileName
  f = open(fileName, 'r')
  res = open('../res.fna', 'w')

  f.close()   
  res.close()

if __name__ =='__main__':
 main()
