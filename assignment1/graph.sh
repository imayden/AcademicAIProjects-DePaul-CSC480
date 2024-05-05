
# graph.sh

#!/bin/bash
# Check if parameters are passed in
if [ "$#" -ne 1 ]; then
    echo "Invalid Command. Use command like: ./graph.sh data/ctaTrain.json (<filepath> <datapath>)"
    exit 1
fi

# run the Python program and pass in the data file as parameter
python3 src/graph.py $1
