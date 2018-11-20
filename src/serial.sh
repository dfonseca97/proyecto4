if [ ! -d "../results" ]; then
  mkdir ../results
fi
python ADN_To_ARN.py ../dataset
