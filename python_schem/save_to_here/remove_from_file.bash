phrase_to_look_for="$2"
cat "$1" | sed "s/$phrase_to_look_for//" #> temp
#mv temp "$1"
