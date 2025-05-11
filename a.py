import os
from datetime import datetime, timedelta

start_date = datetime(2025, 3, 1)
days = 65
commits_per_day = 3

for i in range(days):
    date = start_date + timedelta(days = i)
    date_str = date.strftime("%y-%m-%dT12:00:00")

    for j in range(commits_per_day):
        with open("file.txt", "a") as f:
            f.write(f"{date} - commit {j}\n")
        os.system("git add file.txt")
        os.system(f'set GIT_AUTHOR_DATE={date_str}&& set GIT_COMMITER_DATE={date_str} && git commit -m "Commit {i}-{j}"')

print("Commits done...........")