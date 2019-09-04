phrase_to_look_for="$2"
cat "$1" | sed "s/$2//" > temp
mv temp "$1"
