# ProcessingGitCommits
Python script for processing git commits in a repository

Executing the Python script

Prerequisites
•	This script relies on the GitHub access token for authentication. Before you run the script, login to your GitHub account, navigate to settings then developer settings and generate a token if you do not already have one. 
•	Install the following libraries: NumPy, Pandas, Matplotlib, PyGithub.

Executing in Terminal
•	Create a python virtual environment.
•	Download the python script into a folder and navigate to the folder in a terminal.
•	Open a code editor e.g., VS Code and run the python script using,
python mostActiveGitRepoContrib.py

Executing in Jupyter Notebook
•	Open the python script in a text editor and copy the contents into a running notebook environment.
•	Paste the script and run the notebook cell containing the script.

After executing the script
Upon executing the script from either the Terminal or Jupyter notebook, you will be prompted to supply some information.
•	Enter the access token when requested.
•	Enter the repository in the requested format.
•	Enter the number of top active contributors you are looking to view.
•	Wait for processing to complete and a bar chart containing the requested information will be displayed.
