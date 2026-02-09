import argparse
import os
import subprocess
import sys
import time
from datetime import datetime
from uuid import uuid4


def run_git(args, cwd, env=None):
    return subprocess.run(["git"] + args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def is_git_repo(path):
    p = run_git(["rev-parse", "--is-inside-work-tree"], cwd=path)
    return p.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Create a file and make many small git commits.")
    parser.add_argument("--repo", default=".", help="Path to the git repository (default: current dir)")
    parser.add_argument("--file", default="commit_file.txt", help="File to edit for commits")
    parser.add_argument("--count", type=int, default=25, help="Number of commits to create")
    parser.add_argument("--delay", type=float, default=0.0, help="Seconds to wait between commits")
    parser.add_argument("--author-name", default=None, help="Git author name to use for commits")
    parser.add_argument("--author-email", default=None, help="Git author email to use for commits (must match GitHub account to affect contributions)")
    parser.add_argument("--init", action="store_true", help="Init a git repo if none exists in --repo")
    parser.add_argument("--push", action="store_true", help="Push to the remote after committing (use with care)")
    parser.add_argument("--message-prefix", default="chore: update", help="Prefix for the commit messages")

    args = parser.parse_args()

    repo = os.path.abspath(args.repo)
    os.makedirs(repo, exist_ok=True)

    if not is_git_repo(repo):
        if args.init:
            r = run_git(["init"], cwd=repo)
            if r.returncode != 0:
                print("Failed to init git repo:", r.stderr)
                sys.exit(1)
            print("Initialized empty git repository in", repo)
        else:
            print("No git repository found at", repo)
            print("Run with --init to initialize, or run inside an existing repo.")
            sys.exit(1)

    target_file = os.path.join(repo, args.file)

    for i in range(1, args.count + 1):
        # Append a short unique line so each commit changes the file
        line = f"{datetime.utcnow().isoformat()} {i} {uuid4()}\n"
        with open(target_file, "a", encoding="utf-8") as f:
            f.write(line)

        # Stage the file
        r = run_git(["add", args.file], cwd=repo)
        if r.returncode != 0:
            print("git add failed:", r.stderr)
            sys.exit(1)

        # Prepare environment for commit author (optional)
        env = os.environ.copy()
        if args.author_name:
            env["GIT_AUTHOR_NAME"] = args.author_name
            env["GIT_COMMITTER_NAME"] = args.author_name
        if args.author_email:
            env["GIT_AUTHOR_EMAIL"] = args.author_email
            env["GIT_COMMITTER_EMAIL"] = args.author_email

        message = f"{args.message_prefix} #{i} {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}"
        r = run_git(["commit", "-m", message, "--no-verify"], cwd=repo, env=env)
        if r.returncode != 0:
            print("git commit failed:", r.stderr)
            sys.exit(1)

        print(f"Committed {i}/{args.count}: {message}")

        if args.delay:
            time.sleep(args.delay)

    if args.push:
        print("Pushing to remote (origin)...")
        r = run_git(["push", "origin", "HEAD"], cwd=repo)
        if r.returncode != 0:
            print("git push failed:", r.stderr)
            sys.exit(1)

    print("Done: created", args.count, "commits in", repo)


if __name__ == "__main__":
    main()
