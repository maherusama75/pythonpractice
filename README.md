# auto_commits.py — small automation for frequent commits

Usage notes:

- Edit or verify your Git author email is the one linked to your GitHub account so contributions appear: `git config --global user.email "you@example.com"`.
- Run the script from your repository root (or pass `--repo`):

```powershell
python auto_commits.py --count 25 --file commit_file.txt --author-name "Your Name" --author-email "you@example.com"
```

- To initialize a repository automatically: add `--init`.
- To push to remote after commits, add `--push` (be careful — this will push to `origin`).
- On Windows use Task Scheduler, on Linux/macOS use `cron` to run it daily.

Important:
- Commits only count toward GitHub contributions if the commit email is associated with your GitHub account and the repository is pushed to GitHub (and contribution rules are met).
- Use responsibly; automating commits to manipulate contribution graphs may be against expected behavior — prefer real activity.
