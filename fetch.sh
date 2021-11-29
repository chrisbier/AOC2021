#!/bin/bash
# By: Brad King
# Modified by me

DAY=$( date +%d )
OUTPUT="./$DAY/input.txt"
URL="https://adventofcode.com/2021/day/$DAY/input"
SESSION=${AOC_SESSION}

mkdir $DAY
echo "Pulling input for day $DAY"
echo "Writing to file: $OUTPUT"

curl --location --request GET "$URL" --header "Cookie: session=$SESSION" -o "$OUTPUT"
