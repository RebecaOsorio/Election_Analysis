#  Election_Analysis

##  Project and Challenge Overview
A Colorado Board of Elections employee asked for the following tasks:

1. Calculate the total number of votes cast.

2. Get a complete list of candidates who received votes.

3. Calculate the total number of votes each candidate received.

4. Calculate the percentage of votes each candidate won.

5. Determine the winner of the election based on popular vote.

to complete the election audit of a recent local congressional election.

Finally, the election commission has requested some additional data to complete the audit:

- A complete list of the counties that participated in the elections.

- The voter turnout for each county

- The percentage of votes from each county out of the total count

-   The county with the highest turnout


##  Resources

* Data Source: election_results.csv

* Software: Python 3.9.7, Visual Studio Code 1.38.1

##  Challenge Summary

Working from this module’s `election_results.csv` file, we used `for` loops and conditional statements with membership and logical operators to find the requested results. Then, we printed the results to the command line and save them to the `election_results.txt` file in the `analysis` directory.

### The Election-Audit showed that:

-   There were 369,711 votes cast in the election
-  County breakdown of the number of votes in the precint:
	- Jefferson had 10.5% of the vote, with 38,855 number of votes.
	- Denver had 82.8% of the vote, with 306,055 number of votes.
	- Arapahoe had 6.7% of the vote, with 24,801 number of votes.
-   Denver was the Largest County Turnout.
-  The candidate results were

	* Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.

	* Diana DeGette received 73.8% of the vote and 272,892 number of votes.

	* Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

-  The winner of the election was

	* Diana DeGette (2), who received 73.8% of the vote and 272,892 number of votes.

### Election-Audit Summary
When we made the analysis, we supposed that the file has a header and hardcoded the rows that contained the data we needed. To fix this, we came upon a couple of fixes so this script can be used to any election file.
1. **Do we have a header in the `.cvs` file?**
To set quickly if we have a header or not, we'll ask the user, so we can skip the first row if we have a header.
![Header Input](https://user-images.githubusercontent.com/90414330/137617668-93c4643c-7962-42d1-b3e2-f6424f002b24.png)
We'll skip it after opening the file.
![Skip Header](https://user-images.githubusercontent.com/90414330/137617669-bb3d5385-016a-464d-9ad2-390e1dc3c4bb.png)

3. **We'll want to make sure that we are storing correctly the names of the candidates and the counties**
*Only valid if the `.csv` file has a header*
In first input, if we have a header, we'll be asking the user the name of the columns that contain the Candidates' Names and the Counties.
![Header and Items Input](https://user-images.githubusercontent.com/90414330/137617672-e136835b-95ce-4f53-a42b-eef6c99d1fc7.png)
And then, we'll get the index from the `header` variable that remained after using `next()` function and the names specified for each Candidates and Counties Columns.
![Header and Index Items](https://user-images.githubusercontent.com/90414330/137617671-39b21f93-35b5-4587-a2a5-edde2504fa25.png)
To end with:![Storing the data](https://user-images.githubusercontent.com/90414330/137618075-7c13306c-9a6b-4b4e-afae-0347b8297dc9.png)


> Written with [StackEdit](https://stackedit.io/).
