function aliases() {
 printf "                                    General                                     \n+---------------------+--------------------------------------------------------+\n| alias               | definition                                             |\n+---------------------+--------------------------------------------------------+\n| gte                 | gnome-text-editor                                      |\n| cl                  | clear                                                  |\n| lsl                 | ls -lh                                                 |\n| cd..                | cd ..                                                  |\n+---------------------+--------------------------------------------------------+\n                                     Python                                     \n+----------+-------------------------------------------------------------------+\n| alias    | definition                                                        |\n+----------+-------------------------------------------------------------------+\n| py       | python3                                                           |\n| rn       | py main.py                                                        |\n| ts       | py test.py                                                        |\n| ipy      | ipython                                                           |\n| pipi     | py -m pip install                                                 |\n| pipg     | pipi --upgrade pip                                                |\n| pipu     | py -m pip uninstall                                               |\n| pipl     | py -m pip list                                                    |\n| pipr     | py -m pip install -r requirements.txt                             |\n| pipd     | pipg; pipi ipython                                                |\n| venv     | source .venv/bin/activate                                         |\n| mkvenv   | py -m venv --prompt venv .venv && venv && pipd && pipr            |\n+----------+-------------------------------------------------------------------+\n                                      Git                                       \n+---------+--------------------------------------------------------------------+\n| alias   | definition                                                         |\n+---------+--------------------------------------------------------------------+\n| gi      | git init                                                           |\n| gfc     | git config                                                         |\n| gb      | git branch                                                         |\n| gs      | git status                                                         |\n| gl      | git log                                                            |\n| ga      | git add                                                            |\n| gc      | git commit -m                                                      |\n| gcf     | git commit -F                                                      |\n| gcfc    | git commit -F changes.txt && printf \"\" > changes.txt               |\n| gr      | git remote                                                         |\n| grao    | git remote add origin                                              |\n| gf      | git fetch                                                          |\n| gfo     | git fetch origin                                                   |\n| gpl     | git pull                                                           |\n| gplo    | git pull origin                                                    |\n| gpu     | git push                                                           |\n| gpuo    | git push origin                                                    |\n| gch     | git checkout                                                       |\n| gchn    | git checkout -b                                                    |\n| gsw     | git switch                                                         |\n| grmu    | git rm -r --cached .; ga .; gc \"removing unused files.\"            |\n| gtr     | git ls-tree -r <branch> --name-only                                |\n| gcl     | git clone <url> .                                                  |\n+---------+--------------------------------------------------------------------+\n" 
}

alias gte='gnome-text-editor'
alias cl='clear'
alias lsl='ls -lh'
alias cd..="cd .."


alias py='python3'
alias rn='py main.py'
alias ts='py test.py'
alias ipy='ipython'
alias pipi='py -m pip install'
alias pipg='pipi --upgrade pip'
alias pipu='py -m pip uninstall'
alias pipl='py -m pip list'
alias pipr='py -m pip install -r requirements.txt'
alias pipd='pipg; pipi ipython'
alias venv='source .venv/bin/activate'
alias mkvenv='py -m venv --prompt venv .venv && venv && pipd && pipr'


alias gi='git init'
alias gfc='git config'
alias gb='git branch'
alias gs='git status'
alias gl='git log'
alias ga='git add'
alias gc='git commit -m'
alias gcf='git commit -F'
alias gcfc='git commit -F changes.txt && printf "" > changes.txt'
alias gr='git remote'
alias grao='git remote add origin'
alias gf='git fetch'
alias gfo='git fetch origin'
alias gpl='git pull'
alias gplo='git pull origin'
alias gpu='git push'
alias gpuo='git push origin'
alias gch='git checkout'
alias gchn='git checkout -b'
alias gsw='git switch'
alias grmu='git rm -r --cached .; ga .; gc "removing unused files."'
function gtr() {
    # alias gtr='git ls-tree -r <branch> --name-only'
    local branch="$1"
    eval "git ls-tree -r $branch --name-only"
}
function gcl() {
    # alias gcl='git clone <url> .'
    local url="$1"
    eval "git clone $url ."
}


