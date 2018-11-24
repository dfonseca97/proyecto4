import sys
from mpi4py import MPI
from os import listdir
from os.path import isfile, join
from datetime import datetime

def main():

 directory = sys.argv[1]
 fna = [filename for filename in listdir(directory) if filename[-3:] == ".fa"]
 comm = MPI.COMM_WORLD
 rank = comm.Get_rank()
 
 if rank == 0:
  print(rank)
  adn_to_arn(fna[0], directory)
 elif rank == 1:
  print(rank)
  adn_to_arn(fna[1], directory)
 elif rank == 2:
  print(rank)
  adn_to_arn(fna[2], directory)
 
def adn_to_arn(fna, directory):
 
 sys.stdout.flush()
 f = open(directory + fna, 'r')
 res = open('/opt/dna/results/' + fna + '.result', 'w')
 print(directory + fna)
 sys.stdout.flush()
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

start = datetime.now()  
print(MPI.Get_processor_name())
sys.stdout.flush()
main()
end = datetime.now()
total = end - start
total_time = total.seconds
print("Processor: " + MPI.Get_processor_name() + ', Time:' + str(total_time) + "s")
sys.stdout.flush()
