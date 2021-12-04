#!/bin/bash
FILENAME="$(echo $2 | sed 's/\.[^.]*$//')"
python3 $1 < $2 | diff "$FILENAME.output" -
