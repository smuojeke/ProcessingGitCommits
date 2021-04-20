from github import Github
import datetime
import collections
import copy
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

print("Please enter or paste the access token from your github account: ")
github_access_token = input()
g = Github(github_access_token)
#g = Github("xxx_xxxxxxxxxxxxxxxxxxxxx")
g.get_user().login
print("Enter the name of the github repo using the format: repo_owner/repo_name e.g openstack/nova: ")
github_repo = input()
print("Enter the number of top active contributors you would like to see: ")
top_n_contrib = input()
#top_n_contrib = 15
repo = g.get_repo(github_repo)
#repo = g.get_repo("openstack/nova")
print("Name of repository: " + repo.name)
print("Pulling data from repository... Please wait...")

commit_authorLoginList = []
commit_authorNameList = []
NumOfCommitsInRepo = 0
NumOfCommitsInRepoWithAuthor = 0
NumOfCommitsInRepoWithAuthorAndLogin = 0
NumOfCommitsInRepoWithAuthorAndName = 0
for commit in repo.get_commits(since=datetime.datetime(2020, 4, 16), until=datetime.datetime(2021, 4, 16)):
    NumOfCommitsInRepo += 1
    if (commit.author != None):
        NumOfCommitsInRepoWithAuthor += 1
        if (commit.author.login != None):
            NumOfCommitsInRepoWithAuthorAndLogin += 1
            commit_authorLoginList.append(commit.author.login)
        if (commit.author.name != None):
            NumOfCommitsInRepoWithAuthorAndName += 1
            commit_authorNameList.append(commit.author.name)

print("Num Of Commits In Repo: " + str(NumOfCommitsInRepo))
print("Num Of Commits In Repo With Author: " + str(NumOfCommitsInRepoWithAuthor))
print("Num Of Commits In Repo With Author And Login: " + str(NumOfCommitsInRepoWithAuthorAndLogin))
print("Num Of Commits In Repo With Author And Name: " + str(NumOfCommitsInRepoWithAuthorAndName))


#my_list = copy.deepcopy(commit_authorNameList)
ctr = collections.Counter(commit_authorNameList)
cmt_lords = ctr.most_common(int(top_n_contrib))
cmt_lords_name = []
cmt_lords_freq = []
for c in cmt_lords:
    cmt_lords_name.append(c[0][:20])
    cmt_lords_freq.append(c[1])
# plot the result in a bar chart
figure(figsize=(25, 9), dpi=80)
plt.xlabel('Number of commits', fontsize=20)
plt.ylabel('Contributor\'s name', fontsize=20)
plt.title(str(top_n_contrib) + ' most active contributors to the ' + github_repo + ' repository in last 12 months', fontsize=25)
for i, x in enumerate(cmt_lords_freq):
    plt.text(x, i - 0.1, str(x), fontsize=12)
y_pos = np.arange(len(cmt_lords_name))
plt.barh(y_pos, cmt_lords_freq)
plt.yticks(y_pos, cmt_lords_name, fontsize=15)
plt.xticks(fontsize=15)
plt.show()

# Print list of most active contributors
print("Most Active Contributors list")
pos = 0
for x in cmt_lords:
    #print(x)
    pos += 1
    print("Position " + str(pos) + ": " + str(x[0]) + " --- Number of commits: " + str(x[1]))


    
