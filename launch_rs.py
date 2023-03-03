# this script install necessary requirements and launchs main program in riverside_webui.py
import subprocess
import os
import sys
import importlib.util
import shlex
import platform
import argparse
import json

dir_repos = "repositories"
dir_extensions = "extensions"
python = sys.executable
git = os.environ.get('GIT', "git")
index_url = os.environ.get('INDEX_URL', "")
stored_commit_hash = None
skip_install = False


if __name__ == "__main__":
    prepare_environment()
    start()