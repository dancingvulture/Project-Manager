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
    # git ls-tree -r <branch> --name-only
    local branch="$1"
    eval "git ls-tree -r $branch --name-only"
}
function gcl() {
    # git clone <url> .
    local url="$1"
    eval "git clone $url ."
}
