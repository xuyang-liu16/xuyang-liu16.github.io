#!/bin/bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
state_dir="$HOME/Library/Application Support/HomepageCitationUpdater"
runtime_python="$state_dir/venv/bin/python"
gh_binary="$(command -v gh)"
work_dir="$(mktemp -d "${TMPDIR:-/tmp}/homepage-citations.XXXXXX")"
trap 'rm -rf -- "$work_dir"' EXIT

export GOOGLE_SCHOLAR_ID="9VhMC1QAAAAJ"
export PYTHONDONTWRITEBYTECODE=1

cd "$work_dir"
"$runtime_python" -u "$script_dir/main.py"

git -c http.proxy= clone --quiet --depth 1 --single-branch \
    --branch google-scholar-stats \
    https://github.com/xuyang-liu16/xuyang-liu16.github.io.git data
cp results/gs_data.json results/gs_data_shieldsio.json data/
git -C data add -- gs_data.json gs_data_shieldsio.json
if git -C data diff --cached --quiet; then
    echo "No citation changes to publish."
    exit 0
fi

git -C data -c user.name="Citation updater" \
    -c user.email="xuyang-liu16@users.noreply.github.com" \
    commit --quiet -m "Updated Citation Data"
git -C data -c http.proxy= -c credential.helper= \
    -c "credential.helper=!${gh_binary} auth git-credential" \
    push origin google-scholar-stats
echo "Citation update published successfully."
