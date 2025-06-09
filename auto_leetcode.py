import os
import random
import requests
from datetime import datetime
import subprocess

# One-time folder
folder = "problems"
os.makedirs(folder, exist_ok=True)

# Today's date for file names
today = datetime.today().strftime('%Y-%m-%d')

# Fetch problems from LeetCode
url = 'https://leetcode.com/api/problems/all/'
response = requests.get(url)
problems = response.json()['stat_status_pairs']

# Filter only Easy level problems
easy_problems = [p for p in problems if p['difficulty']['level'] == 1]
selected = random.sample(easy_problems, random.randint(3, 4))

# Generate problem stubs
for p in selected:
    title_slug = p['stat']['question__title_slug']
    title = p['stat']['question__title']
    id = p['stat']['frontend_question_id']
    filename = f"{today}__{id}-{title_slug}.py"
    filepath = os.path.join(folder, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title} (https://leetcode.com/problems/{title_slug}/)\n\n")
        f.write("class Solution:\n    def TODO(self):\n        pass\n")

# Auto Git commit and push
subprocess.run(["git", "config", "--global", "user.email", "rj1342627@gmail.com"])
subprocess.run(["git", "config", "--global", "user.name", "Rahuljoshi07"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Auto LeetCode commit for {today}"])
subprocess.run(["git", "push"])
