if [ ! -d "/opt/dna/results" ]; then
  mkdir /opt/dna/results
fi
mpiexec -f ../hosts_mpi -np 3 /opt/anaconda3/bin/python3 ADN_To_ARN_Parallel.py /opt/dna/
