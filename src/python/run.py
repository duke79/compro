import os
import subprocess
import sys

src = os.path.dirname(__file__)

site = sys.argv[1]  # eg. "codechef"
contest = sys.argv[2]  # eg. "JAN19B"

site_dir = os.path.join(src, site)
contest_dir = os.path.join(site_dir, contest)


def most_recent(directory=".", extension=".py"):
    ret = ""
    max_mtime = 0
    for dirname, subdirs, files in os.walk(directory):
        for fname in files:
            full_path = os.path.join(dirname, fname)
            mtime = os.stat(full_path).st_mtime
            if mtime > max_mtime and fname.endswith(extension):
                max_mtime = mtime
                ret = os.path.join(dirname, fname)
    return ret


problem_script = most_recent(contest_dir)
problem_tests_dir = os.path.splitext(problem_script)[0]

for test in os.listdir(problem_tests_dir):
    test_path = os.path.join(problem_tests_dir, test)
    p = subprocess.Popen("python " + problem_script, stdin=open(test_path), stdout=sys.stdout)
    p.wait()
