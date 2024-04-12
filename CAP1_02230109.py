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
# solution Score:
#50267
# number = 9
################################
## Read the input_9_CAP1.txt file


# Function to read input from a file and return a list of shape-outcome pairs
def read_input(file_data):
    with open(file_data, 'r') as file: 
        game_data = [line.strip().split() for line in file]  # Split each line into shape-outcome pair
    return game_data

# Function to calculate the entire score based on game_data
def calculate_score(game_data):
    entire_score = 0  
    for option, player_score in game_data:  
        if option == 'A' and player_score == 'X': #rock, have to lose(0)
            entire_score += 3  # scissor(3)+0
        elif option == 'A' and player_score == 'Y': # rock, have to tie(3)
            entire_score += 4  # rock(1)+3
        elif option == 'A' and player_score == 'Z': #rock, have to win (6)
            entire_score+= 8  # paper(2)+6
        elif option == 'B' and player_score == 'X':#paper, have to lose
            entire_score += 1  # rock(1)+0
        elif option == 'B' and player_score == 'Y':# paper, tie
            entire_score += 5  # paper(2)+3
        elif option == 'B' and player_score == 'Z': # paper, have to win
            entire_score += 9  # scissor(3) + 6
        elif option == 'C' and player_score == 'X': #scissor, have to lose
            entire_score += 2  # paper(2) + 0
        elif option == 'C' and player_score == 'Y': # scissor, tie
            entire_score += 6  # scissor(3) + 3
        elif option == 'C' and player_score == 'Z': # scissor, have to win
            entire_score += 7  # rock(1) + 6
    return entire_score  # Return the entire score

file_data = "CSF101CAP/input_9_cap1.txt" 

# Read combinations from the file
game_data = read_input(file_data) 

entire_score = calculate_score(game_data)  
print("Entire_score:", entire_score ) 