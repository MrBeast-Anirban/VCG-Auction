import json

# Function to run the alternative auction mechanism
def alternative_mechanism(bidders):
    if not bidders:
        print("Error: No valid bids found in the input file.")
        return 0, ""

    # Sort bidders by value and allocate both slots to the highest bidder
    sorted_bidders = sorted(bidders, key=lambda x: x['value'], reverse=True)

    highest_bidder = sorted_bidders[0]
    second_highest_value = sorted_bidders[1]['value'] if len(sorted_bidders) > 1 else 0

    # Create the detailed output for the winning bidder
    winner_info = f"Highest bidder wins with bid: {highest_bidder['value']}\n"
    winner_info += f"Amount paid (second-highest bid): {second_highest_value}\n"
    
    print(winner_info)

    return second_highest_value, winner_info

# Read bids from JSON file
def read_bids(file_path):
    bidders = []
    try:
        with open(file_path, 'r') as file:
            bidders = json.load(file)  # Load the JSON data
    except FileNotFoundError:
        print(f"Error: Input file {file_path} not found.")
    except ValueError:
        print("Error: Invalid data format in input file.")
    return bidders

if __name__ == "__main__":
    # Read the bids from the JSON input file
    bidders = read_bids('input/bids.json')

    # Run the alternative auction mechanism
    total_revenue, winner_info = alternative_mechanism(bidders)
    print(f"Total Revenue under Alternative Mechanism: {total_revenue}")
    
    # Write the result to the output file
    with open('output/alt_mechanism.txt', 'w') as f:
        f.write(f"{winner_info}\n")
        f.write(f"Total Revenue under Alternative Mechanism: {total_revenue}\n")
