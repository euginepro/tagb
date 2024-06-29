#!/bin/bash

# Run 5 instances of the Python script in the background
for i in {1..6}
do
    python3 a_ep_movies_clicker.py &
done

# Wait for all background jobs to complete
wait
