import json

# Function to calculate VCG revenue with collusion
def vcg_revenue_with_collusion(bidders, alpha):
    revenue, winner_info = vcg_revenue(bidders)  # Perform VCG auction without collusion
    return revenue + alpha, winner_info  # Add small cost for multi-identity creation and return updated info

# Function to calculate VCG revenue
def vcg_revenue(bidders):
    # Sort bids for each slot, adding 0s to handle cases where fewer than two bids exist
    t_bids = sorted([bid['value'] for bid in bidders if bid['slot'] == 't'], reverse=True)
    s_bids = sorted([bid['value'] for bid in bidders if bid['slot'] == 's'], reverse=True)
    b_bids = sorted([bid['value'] for bid in bidders if bid['slot'] == 'b'], reverse=True)

    # Set the highest and second-highest bids for each slot, appending 0 to avoid errors
    v1t, v2t = (t_bids + [0, 0])[:2]
    v1s, v2s = (s_bids + [0, 0])[:2]
    v1b, v2b = (b_bids + [0, 0])[:2]

    # Initialize total revenue
    revenue = 0
    winner_info = ""

    # Case 1: Bidder for both slots wins if combined bid is higher
    if v1b > max(v1t + v1s, v1t, v1s):
        winner_info = f"Bidder who wants both slots wins\nWinning bid for both slots: {v1b}\n"
        revenue += v2b  # The revenue is the second-highest combined bid for both slots
    else:
        # Separate bidders win top banner and sidebar
        winner_info = f"Separate bidders win top banner and sidebar\n"
        winner_info += f"Winning bid for top banner: {v1t}\n"
        winner_info += f"Winning bid for sidebar: {v1s}\n"
        revenue += v2t  # Winner of top banner pays second-highest bid for top banner
        revenue += v2s  # Winner of sidebar pays second-highest bid for sidebar

    return revenue, winner_info

# Read bids from JSON file
def read_bids(file_path):
    with open(file_path, 'r') as file:
        bidders = json.load(file)  # Load JSON data into a list of bidders
    return bidders

if __name__ == "__main__":
    alpha = 0.1  # Small cost for collusion

    # Read bids with collusion from JSON input file
    bidders = read_bids('input/bids_collusion.json')
    
    # Calculate VCG revenue with collusion
    total_revenue, winner_info = vcg_revenue_with_collusion(bidders, alpha)
    
    # Print the detailed winning information and total revenue
    print(winner_info)
    print(f"Total VCG Revenue: {total_revenue}\n")
    print("Winning Bids Information:")
    print(winner_info)

    # Write the result to the output file
    with open('output/collusion_results.txt', 'w') as f:
        f.write(f"{winner_info}\n")
        f.write(f"Total VCG Revenue: {total_revenue}\n")
