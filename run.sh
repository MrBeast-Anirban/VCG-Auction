#!/bin/bash

# Run VCG auction experiment
echo "Running VCG auction experiment..."
python3 src/vcgAuction.py input/bids.json > output/vcg_results.txt

# Run collusion experiment
echo "Running collusion experiment..."
python3 src/collusionExperiment.py input/bidsCollusion.json > output/collusion_results.txt

# Run alternative mechanism experiment
echo "Running alternative mechanism experiment..."
python3 src/alternativeMechanism.py input/bids.json > output/alt_mechanism.txt

echo "All experiments completed! Check the output folder for results."
