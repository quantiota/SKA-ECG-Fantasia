#!/usr/bin/env bash
# Download the Fantasia records listed in records.txt into data/ (header and signal files).
set -euo pipefail
cd "$(dirname "$0")"
BASE=https://physionet-open.s3.amazonaws.com/fantasia/1.0.0   # PhysioNet open-data mirror (physionet.org is slow)
mkdir -p data
grep -v '^#' records.txt | awk 'NF {print $1}' | while read -r rec; do
    for ext in hea dat; do
        [ -f "data/$rec.$ext" ] || curl -sfo "data/$rec.$ext" "$BASE/$rec.$ext"
    done
    echo "$rec"
done
