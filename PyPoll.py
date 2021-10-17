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


#################### ANALYZE DATA ##################### 
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

### Initialize Variables
# Initialize a Vote Counter
total_vote_counter = 0

# Declare a new list of candidates
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Declare Winning Candidate and Winning Count Tracker -empty-
winning_candidate = ""
winning_count = 0
winning_percentage = 0

######### Read and Analyze the data here.
with open(file_to_load) as election_data:
     
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     # Skip Header
     next(file_reader)

     # Go over each Row.
     for row in file_reader:
          # Add to the total vote count.
          total_vote_counter += 1

          # Get the candidate's name
          candidate_name = row[2]

          # Add the candidate_name to the candidate_options list using the append() method
          # only if it isn't in the list
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               # Initialize the Counter for each candidate
               candidate_votes[candidate_name] = 0
          
          # Add to each candidate it's vote
          candidate_votes[candidate_name] += 1

######### Save the results.
with open(file_to_save, "w") as txt_file:
     election_results = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes: {total_vote_counter:,}\n"
        f"-------------------------------\n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)

     # Iterate through the candidate list.
     for candidate_name in candidate_votes:

          # Determine the percentage of votes for each candidate by looping through the counts.
          # Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_vote_counter) * 100

          # Print the candidate name and percentage of votes.
          candidate_results = ( 
               f"{candidate_name}: {vote_percentage: .1f}% ({votes:,}).")
          # Print each candidate, their voter count, and percentage to the terminal.
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results + "\n")
     
          # Determine winning vote count and candidate
          # Determine if the votes are greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If True, storage the count and percentage values
               winning_count = votes
               winning_percentage = vote_percentage
               # And Storage the candidate_name
               winning_candidate = candidate_name

     # Storage the Winning Summary
     winning_candidate_summary = (
     f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")
     # Print the Winning Summary.
     print(winning_candidate_summary)
     #  Save the Winning Summary.
     txt_file.write(winning_candidate_summary)
