#!/usr/bin/env python3

"""
23rd Jan 2021. #507: Easy

This problem was asked by Uber.

On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. 
Write a program that reads this file as a stream and returns the top 3 candidates at any given time. 
If you find a voter voting more than once, report this as fraud.

"""

"""
Solution: We first use file.open() to process the stream of information. For every line, we check with dictionaries of voter and 
candidate IDs. If a voter ID has been seen before, an error is reported. Candidate votes are added. Finally, the dictionary is 
sorted and the top three are selected and returned.

"""

from operator import itemgetter

def top_three_candidates(filepath):
    voters = []                                             # List of voter IDs seen already in the counting
    candidates = {}                                         # Candidate IDs and their corresponding vote count

    with open(filepath, 'r') as f:                          # Reads as stream from text file location
        for line in f:                                      # Reads one line at a time
            [voter_id, candidate_id] = line.split(', ')     # Splits line into voter and candidate ID

            if voter_id in voters:                          # If voter has voted already, report fraud
                return ("Voter fraud reported against id:", voter_id)
            voters.append(voter_id)                         # Add voter to list of already voted IDs

            if candidate_id not in candidates.keys():       # Add candidate to dictionary if not already done
                candidates[candidate_id] = 0
            candidates[candidate_id] += 1                   # Count current vote

    # Sorts dictionary into a list of tuples in descending order based on votes (itemgetter(1) returns values of dict)
    sorted_candidates = sorted(candidates.items(), key=itemgetter(1), reverse=True)

    results = "Candidate votes: Candidate id\n"
    for i in range(3):                                      # Loop picks out first three candidates.
        results += str(sorted_candidates[i][1]) + ": " + sorted_candidates[i][0]

    return results



def main():
    filepath = r"path/to/file"                              # Insert file's path here
    print(top_three_candidates(filepath))

    return

if __name__ == "__main__":
    main()
