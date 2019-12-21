#import os and csv so this works on all devices and can read csv files
import os
import pandas as pd
#set file path
file = os.path.join("Resources" ,"election_data.csv")
output_path = os.path.join("election_stats.txt")

#set data frame
election_df = pd.read_csv(file)
vote_total = election_df["Candidate"].count()

Khan_df = election_df.loc[election_df["Candidate"] == "Khan",:]
Khan_votes = Khan_df["Voter ID"].count()
Khan_pct = (Khan_votes / vote_total) * 100

Correy_df = election_df.loc[election_df["Candidate"] == "Correy",:]
Correy_votes = Correy_df["Voter ID"].count()
Correy_pct = (Correy_votes / vote_total) * 100

Li_df = election_df.loc[election_df["Candidate"] == "Li",:]
Li_votes = Li_df["Voter ID"].count()
Li_pct = (Li_votes / vote_total) * 100

OTooley_df = election_df.loc[election_df["Candidate"] == "O'Tooley",:]
OTooley_votes = OTooley_df["Voter ID"].count()
OTooley_pct = (OTooley_votes / vote_total) * 100

results_df = pd.DataFrame({"Candidates":["Khan", "Correy", "Li", "O'Tooley"],
                            "Vote Totals":[Khan_votes, Correy_votes, Li_votes, OTooley_votes]})

winner =results_df.iloc[results_df['Vote Totals'].idxmax()]

#print output
print("Election Results")
print("---------------------")
print("Total Votes: " + str(vote_total))
print("---------------------")
print('Khan: ' + '{:,.2f}'.format(Khan_pct) + " (" +str(Khan_votes) + ")")
print('Correy: ' + '{:,.2f}'.format(Correy_pct) + " (" +str(Correy_votes) + ")")
print('Li: ' + '{:,.2f}'.format(Li_pct) + " (" +str(Li_votes) + ")")
print("O'Tooley: " + '{:,.2f}'.format(OTooley_pct) + " (" +str(OTooley_votes) + ")")
print("---------------------")
print("Winner: " + winner["Candidates"])


with open(output_path, 'w') as txtfile:
        txtfile.write("Election Results"+ 
         "---------------------"+ 
        "Total Votes: " + str(vote_total)+
        "---------------------"+
        'Khan: ' + '{:,.2f}'.format(Khan_pct) + " (" +str(Khan_votes) + ")"+
        'Correy: ' + '{:,.2f}'.format(Correy_pct) + " (" +str(Correy_votes) + ")"+
        'Li: ' + '{:,.2f}'.format(Li_pct) + " (" +str(Li_votes) + ")"+
        "O'Tooley: " + '{:,.2f}'.format(OTooley_pct) + " (" +str(OTooley_votes) + ")"+
        "---------------------"+
        "Winner: " + winner["Candidates"]
)
