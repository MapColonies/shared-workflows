#!/usr/bin/env python3
import os
import re
import subprocess

def git(args):
    return subprocess.run(["git"] + args, stdout=subprocess.PIPE, text=True).stdout.strip()

def main():
    try:
        tag = git(["describe", "--tags", "--match", "v*-rc*", "--abbrev=0"])
        if not tag: return

        logs = git(["log", f"{tag}..HEAD", "--pretty=format:%B"])

        is_feat = re.search(r"^feat(\(.*\))?:\s", logs, re.MULTILINE)

        m = re.match(r"^v(\d+)\.(\d+)\.(\d+)-rc\.(\d+)$", tag)
        if not m: return
        
        major, minor, patch, rc = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        next_ver = ""

        if is_feat:
            if patch > 0:
                next_ver = f"{major}.{minor + 1}.0-rc.1"
            else:
                next_ver = f"{major}.{minor}.{patch}-rc.{rc + 1}"
        else:
            next_ver = f"{major}.{minor}.{patch}-rc.{rc + 1}"
        
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"next_version={next_ver}\n")
            
    except Exception as e:
        print(f"Error: {e}")
        pass

if __name__ == "__main__":
    main()
