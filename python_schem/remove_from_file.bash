echo -n "what are part are you removing? "
read  phrase_to_look_for

echo -n "from which board? "
read  board_to_remove_from
#phrase_to_look_for="$2"
dir_location="./saved_boards/"
temp="./saved_boards/temp"

removed_left_brackets=$(echo "$phrase_to_look_for" |sed 's/\[/\\[/g')
removed_all_brackets=$(echo "$removed_left_brackets" |sed 's/\]/\\]/g')
cat "$dir_location$board_to_remove_from" | sed "s/$removed_all_brackets//gI" > "$temp"
mv "$temp" "$dir_location$board_to_remove_from"
