function mkmc() {
    # alias mkmc='Make main <file.c> file'
    local filename="$1"

    if [[ -a "$filename" ]]; then
        echo "$filename already exists"
        return 1

    elif [[ -z "$filename" ]]; then
        echo "you must provide a filename"
        return 1
    fi
    touch "$filename"
    printf "/* comment */\n\n" > "$filename"
    printf "#include <stdio.h>\n\n\n" >> "$filename"
    printf "int main(void) {\n" >> "$filename"
    printf "    \n" >> "$filename"
    printf "    return 0;\n" >> "$filename"
    printf "}\n" >> "$filename"
}
function mkmcv() {
    # alias mkmcv='mkmc && vim <file.c>'
    local filename="$1"
    mkmc $filename && vim $filename
}
alias bcc="gcc -Wall -Wextra -std=c2x -pedantic"
function bcrn() {
    # alias bcrn='bcc <file.c> && ./a.out'
    local filename="$1"
    bcc $filename && ./a.out
}
function vbcrn() {
    # alias vbcrn='vim <file.c> && bcrn <file.c>'
    local filename="$1"
    vim $filename && bcrn $filename
}
function mkvbcrn() {
    # alias mkvbcrn='mkmc <file.c> && vbcrn <file.c>
    local filename="$1"
    mkmc $filename && vbcrn $filename
}
function lbcrn() {
    # alias lbcrn="ls <file.c> | entr -r -s "[DISPLAY] && $bcc $filename && ./a.out <args>""
    local filename="$1"
    shift
    local args="$@"
    local bcc="${BASH_ALIASES[bcc]}"

    local show_date="_date=\$(date +%H:%M:%S) && printf \"\$_date\""
    local bookend="##################"
    local lside="#    "
    local rside="    #"
    local ldisplay="printf '$bookend\n$lside'"
    local rdisplay="printf '$rside\n$bookend\n'"

    ls $filename | entr -s -r "$ldisplay && $show_date && $rdisplay && $bcc $filename && ./a.out $@"
}

