phrase_to_look_for="$1"
dir_location="./saved_boards/"

removed_left_brackets=$(echo "$1" |sed 's/\[/\\[/g')
removed_all_brackets=$(echo "$removed_left_brackets" |sed 's/\]/\\]/g')
echo "the boards we have that have those parts are "
cd $dir_location
for i in *; do cat "$i"|grep -rl -i "$removed_all_brackets"|sort|uniq ; done
