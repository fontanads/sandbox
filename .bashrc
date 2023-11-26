#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

[[ -f ~/.welcome_screen ]] && . ~/.welcome_screen

_set_liveuser_PS1() {
    PS1='[\u@\h \W]\$ '
    if [ "$(whoami)" = "liveuser" ] ; then
        local iso_version="$(grep ^VERSION= /usr/lib/endeavouros-release 2>/dev/null | cut -d '=' -f 2)"
        if [ -n "$iso_version" ] ; then
            local prefix="eos-"
            local iso_info="$prefix$iso_version"
            PS1="[\u@$iso_info \W]\$ "
        fi
    fi
}
_set_liveuser_PS1
unset -f _set_liveuser_PS1

ShowInstallerIsoInfo() {
    local file=/usr/lib/endeavouros-release
    if [ -r $file ] ; then
        cat $file
    else
        echo "Sorry, installer ISO info is not available." >&2
    fi
}

alias ls='ls --color=auto'
alias ll='ls -lav --ignore=..'   # show long listing of all except ".."
alias l='ls -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."

[[ "$(whoami)" = "root" ]] && return

[[ -z "$FUNCNEST" ]] && export FUNCNEST=100          # limits recursive functions, see 'man bash'

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# Load pyenv automatically
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Created by `pipx`
export PATH="$PATH:/home/fontanads/.local/bin"

# Custom PS1 with git branch, current folder, and virtual environment
parse_git_branch() {
  local branch=$(git branch --show-current 2> /dev/null)
  if [ -n "$branch" ]; then
    echo "($branch)"
  fi
}


# Function to extract the current virtual environment name
extract_virt_env() {
  if [ -n "$VIRTUAL_ENV" ]; then
    # Extract the name of the virtual environment
    local venv_name=$(basename "$VIRTUAL_ENV")

    # Check if PS1 already contains the virtual environment name to avoid duplication
    if [[ $PS1 != *"$venv_name"* ]]; then
      echo "($venv_name)"
    fi
  fi
}

update_ps1() {
  export PS1="\[\033[33m\]\$(extract_virt_env)\[\033[00m\] [\u@\h \[\033[34m\]\W\[\033[00m\] \[\033[31m\]$(parse_git_branch)\[\033[00m\]]\$ "
}

PROMPT_COMMAND=update_ps1


