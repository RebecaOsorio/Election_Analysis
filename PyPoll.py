# Count the votes of an election:
# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

#################### READ THE DATA ####################

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'


# Open the election results and read the file.

# ## Method 1
# election_data = open(file_to_load, 'r')

# # Close the file.
# election_data.close()

# ## Method 2
# # Open with 'with' statement
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

# ## Method 3
import csv
import os

# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)


#################### WRITE DATA ####################


# ## Method 1

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")

# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# ## Method 2

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

# #     # Write some data to the file.
# #     txt_file.write("Hello World")

#      # Write three counties to the file.
#      txt_file.write("Counties in the Election\n")
#      txt_file.write("-----------------------------\n")
#      txt_file.write("Arapahoe\nDenver\nJefferson")


#################### READ DATA ##################### 
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a Vote Counter
total_vote_counter = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

##### To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # Print the header row.
     headers = next(file_reader)
     
     # Print each row in the CSV file.
     for row in file_reader:
          # 2. Add to the total vote count.
          total_vote_counter += 1

# 3. Print the total votes.
print(f"Total Votes Counted: {total_vote_counter:,}")