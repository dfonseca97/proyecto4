if [ ! -d "/opt/dna/results" ]; then
  mkdir /opt/dna/results
fi
python ADN_To_ARN.py /opt/dna/
