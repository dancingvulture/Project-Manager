function aliases() {
    echo "+==============================================+"
    echo "|                   GENERAL                    |"
    echo "+=====+========================================+"
    echo "| gte | gnome-text-editor                      |"
    echo "| cls | clear                                  |"
    echo "+=====+========================================+"
    echo "|                   PYTHON                     |"
    echo "+========+=====================================+"
    echo "| py     | python3                             |"
    echo "| rn     | py main.py                          |"
    echo "| ts     | py test.py                          |"
    echo "| ipy    | ipython                             |"
    echo "| venv   | source .venv/bin/activate           |"
    echo "| mkvenv | py -m vemv --prompt venv .venv;     |"
    echo "|        | venv; pipr; pipd                    |"
    echo "+========+=====================================+"
    echo "|                     PIP                      |"
    echo "+======+=======================================+"
    echo "| pipi | py -m pip install <module>            |"
    echo "| pipg | pipi --upgrade pip                    |"
    echo "| pipu | py -m pip uninstall <module>          |"
    echo "| pipl | py -m pip list                        |"
    echo "| pipr | py -m pip install -r requirements.txt |"
    echo "| pipd | pipg; pipi ipython                    |"
    echo "+======+=======================================+"
    echo "|                     GIT                      |"
    echo "+======+=======================================+"
    echo "| gi   | git init                              |"
    echo "| gcfi | git config                            |"
    echo "| gb   | git branch                            |"
    echo "| gs   | git status                            |"
    echo "| gl   | git log                               |"
    echo "| ga   | git add                               |"
    echo "| gc   | git commit -m                         |"
    echo "| gcf  | git commit -F                         |"
    echo "| gcfc | git commit -F changes.txt             |"
    echo "| gr   | git remote                            |"
    echo "| grao | git remote add origin <url>           |"
    echo "| gf   | git fetch                             |"
    echo "| gfo  | git fetch origin                      |"
    echo "| gpl  | git pull                              |"
    echo "| gplo | git pull origin <branch>              |"
    echo "| gpu  | git push                              |"
    echo "| gpuo | git push origin <branch>              |"
    echo "| gch  | git checkout <branch>                 |"
    echo "| gchn | git checkout -b <branch>              |"
    echo "| gsw  | git switch <branch>                   |"
    echo "| grmu | git rm -r --cached .; ga .;           |" 
    echo "|      | ggc 'removing unused files.'          |"
    echo "| gtr  | git ls-tree -r <branch> --name-only   |"
    echo "+==============================================+"
}

# General
alias gte='gnome-text-editor'
alias cle='clear'

# Python
alias py='python3'
alias rn='py main.py'
alias ts='py test.py'
alias ipy='ipython'

# Pip
alias pipi='py -m pip install'
alias pipg='pipi --upgrade pip'
alias pipu='py -m pip uninstall'
alias pipl='py -m pip list'
alias pipr='py -m pip install -r requirements.txt'
alias pipd='pipg; pipi ipython'
alias venv='source .venv/bin/activate'
function mkvenv() {
    py -m venv --prompt venv .venv
    venv
    pipg
    pipd
    if [ -f "requirements.txt" ]; then
        pipr
    fi
}

# Git
alias gi='git init'
alias gfc='git config'
alias gb='git branch'
alias gs='git status'
alias gl='git log'
alias ga='git add'
alias gc='git commit -m'
alias gcf='git commit -F'
alias gcfc='git commit -F changes.txt'
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
alias grmu='git rm -r --cached .; ga .; ggc "removing unused files."'
function gtr() {
    local branch="$1"
    eval "git ls-tree -r $branch --name-only"
}


