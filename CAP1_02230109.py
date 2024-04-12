################################
# Tashi Yangzom
# 1ECE
# 02230109
# REFERENCES
#
#https://youtu.be/Qcefu1jVPds?si=I_STqNw7QqUIqNcT
#https://youtu.be/fn68QNcatfo?si=YQag4cRapviwUZBD
#https://youtu.be/WexB24-_KCM?si=DES-GjXrH_UP7Hvi
#https://youtu.be/xRlN8CFJwAM?si=EGkSgX2R-V6eLpej
#https://youtu.be/k2EahPgl0ho?si=bXuI1H7jLM3O0NzZ
################################
# SOLUTION
# Solution Score:
#
# number = 9
################################
## Read the input_9_CAP1.txt file


# Function to read input from a file and return a list of shape-outcome pairs
def read_input(file_path):
    with open(file_path, 'r') as file:
        shape_outcome_pairs = [line.strip().split() for line in file]  # Split each line into shape-outcome pair
    return shape_outcome_pairs

# Function to calculate the total score based on shape-outcome pairs
def calculate_score(shape_outcome_pairs):
    total_score = 0  # Initialize total score
    # Calculate score based on the combination of shape and outcome
    for shape, players_outcome in shape_outcome_pairs:  # Iterate over each shape-outcome pair
        if shape == 'A' and players_outcome == 'X':
            total_score += 3  # Add 3 to the total score if shape is A and outcome is X
        elif shape == 'A' and players_outcome == 'Y':
            total_score += 4  # Add 4 to the total score if shape is A and outcome is Y
        elif shape == 'A' and players_outcome == 'Z':
            total_score += 8  # Add 8 to the total score if shape is A and outcome is Z
        elif shape == 'B' and players_outcome == 'X':
            total_score += 1  # Add 1 to the total score if shape is B and outcome is X
        elif shape == 'B' and players_outcome == 'Y':
            total_score += 5  # Add 5 to the total score if shape is B and outcome is Y
        elif shape == 'B' and players_outcome == 'Z':
            total_score += 9  # Add 9 to the total score if shape is B and outcome is Z
        elif shape == 'C' and players_outcome == 'X':
            total_score += 2  # Add 2 to the total score if shape is C and outcome is X
        elif shape == 'C' and players_outcome == 'Y':
            total_score += 6  # Add 6 to the total score if shape is C and outcome is Y
        elif shape == 'C' and players_outcome == 'Z':
            total_score += 7  # Add 7 to the total score if shape is C and outcome is Z
    return total_score  # Return the total score

file_path = "CSF101CAP/input_9_cap1.txt"  # Path to the input file

# Read combinations from the file
shape_outcome_pairs = read_input(file_path)  # Create a list of shape-outcome pairs

total_score = calculate_score(shape_outcome_pairs)  # Calculate total score using calculate_score function
print("Total Score:", total_score)  # Print the total score