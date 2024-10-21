import json

# Function to calculate VCG revenue
def vcg_revenue(bidders):
    # Extract highest and second-highest bids for each slot
    t_bids = sorted([bid['value'] for bid in bidders if bid['slot'] == 't'], reverse=True)
    s_bids = sorted([bid['value'] for bid in bidders if bid['slot'] == 's'], reverse=True)
    b_bids = sorted([bid['value'] for bid in bidders if bid['slot'] == 'b'], reverse=True)

    # Set the highest and second-highest bids for each slot, adding 0 if there are not enough bids
    v1t, v2t = (t_bids + [0, 0])[:2]
    v1s, v2s = (s_bids + [0, 0])[:2]
    v1b, v2b = (b_bids + [0, 0])[:2]

    # Initialize total revenue
    revenue = 0

    # Track the winner
    winner = ""

    # Case 1: Bidder for both slots wins if combined bid is higher
    if v1b > max(v1t + v1s, v1t, v1s):
        print("Bidder who wants both slots wins")
        print(f"Winning bid for both slots: {v1b}")
        winner = f"Both slots won with bid: {v1b}"
        revenue += v2b  # The revenue is the second-highest combined bid for both slots
    else:
        # Separate bidders win top banner and sidebar
        print("Separate bidders win top banner and sidebar")
        if v1t > 0:
            print(f"Winning bid for top banner: {v1t}")
            winner += f"Top banner won with bid: {v1t}\n"
            revenue += v2t  # Winner of top banner pays second-highest bid for top banner
        if v1s > 0:
            print(f"Winning bid for sidebar: {v1s}")
            winner += f"Sidebar won with bid: {v1s}\n"
            revenue += v2s  # Winner of sidebar pays second-highest bid for sidebar

    return revenue, winner

# Read bids from JSON file
def read_bids(file_path):
    with open(file_path, 'r') as file:
        bidders = json.load(file)  # Load JSON data
    return bidders

if __name__ == "__main__":
    # Read the bids from the JSON input file
    bidders = read_bids('input/bids.json')
    
    # Calculate the VCG revenue and winning bids
    total_revenue, winner_info = vcg_revenue(bidders)
    print(f"Total VCG Revenue: {total_revenue}")
    print(f"Winning Bids Information:\n{winner_info}")
    
    # Write the result to the output file
    with open('output/vcg_results.txt', 'w') as f:
        f.write(f"Total VCG Revenue: {total_revenue}\n")
        f.write(f"Winning Bids Information:\n{winner_info}")
