set -e
for i in $(find /transensor/source/* -type d -maxdepth 0); 
do
  coverage run --source=./ -m unittest discover -t ${i} -s ${i} -p "*_test.py"
  coverage report -m
done

