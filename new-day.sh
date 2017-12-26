#!/usr/bin/env bash

set -euo pipefail

if [[ ! $# -eq 1 ]]; then
  echo "usage: ./new-day.sh <day-number>"
  exit 1
fi

DAY="${1}"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
NEW_DIR="${DIR}/${DAY}"
NEW_FILENAME="day-${DAY}.py"
NEW_FILE="${NEW_DIR}/${NEW_FILENAME}"

mkdir ${NEW_DIR}
cp "${DIR}/template.py" ${NEW_FILE}
chmod +x ${NEW_FILE}

cat <<HEREDOC > "${NEW_DIR}/README.md"
# Advent of Code: Day ${DAY}
---

For answers, run \`${NEW_FILENAME}\`.

Program input is in \`input.txt\`.
HEREDOC
