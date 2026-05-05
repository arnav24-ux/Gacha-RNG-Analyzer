import math

def calculate_pulls_needed(drop_rate_percentage, target_probability_percentage):
    drop_rate = drop_rate_percentage / 100.0
    target_prob = target_probability_percentage / 100.0
    fail_rate = 1.0 - drop_rate
    
    # Return -1 instead of a string to avoid TypeErrors later
    if fail_rate <= 0 or fail_rate >= 1:
        return -1 
        
    # Prevent math.log(0) crashes
    if target_prob >= 1.0:
        return float('inf') 
        
    pulls = math.log(1.0 - target_prob) / math.log(fail_rate)
    return math.ceil(pulls)

def main():
    print("--- Video Game RNG & Drop Rate Analyzer ---")
    try:
        drop_rate = float(input("Enter the item drop rate (e.g., 1.5 for 1.5%): "))
        cost_per_pull = int(input("Enter the in-game cost per pull (e.g., 160): "))
        
        print("\n--- Results ---")
        # FIXED: Added a list of target percentages to test
        targets = [50, 75, 90, 99] 
        
        for target in targets:
            pulls = calculate_pulls_needed(drop_rate, target)
            
            # Handle the error codes cleanly
            if pulls == -1:
                print("Invalid drop rate entered. Must be between 0.1 and 99.9.")
                break
            elif pulls == float('inf'):
                print(f"For a {target}% chance of getting the item:")
                print("  -> You need infinite pulls (100% is impossible with pure RNG).\n")
            else:
                total_cost = pulls * cost_per_pull
                print(f"For a {target}% chance of getting the item:")
                print(f"  -> You need {pulls} pulls.")
                print(f"  -> Total expected cost: {total_cost} currency.\n")
                
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()
