# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# = :: =========================================================== :: =
# Filename: /home/lutherus/.zshrc
# Purpose: My personal zsh  configuration file
# Author: lutherus
# License: License? uhm, this is a config file; do with it what ever you want!
# Created: 13.08.2009 18:20 CET (+0100)
# Modified: 23 22:25:52 CET 2012
# = :: =========================================================== :: =
export TERM="xterm-256color"

if [[ "$TERM" = "rxvt-256color" ]]; then
      (~/bin/color-default &)
  fi

#=-=-=-=-=-=-=
# load stuffs
#=-=-=-=-=-=-=

autoload -U colors
autoload -U compinit
autoload -U vcs_info

zmodload zsh/complist
zmodload zsh/terminfo

# setopt
setopt autocd extendedglob
setopt prompt_subst
setopt inc_append_history

# start stuffs
colors
compinit
vcs_info


#=-=-=-=-
# zstyle
#=-=-=-=-

# vcs_info
zstyle ':vcs_info:*' enable git hg svn
zstyle ':vcs_info:*' check-for-changes true

# completion

# ignore completion to commands we don't have
zstyle ':completion:*:functions' ignored-patterns '_*'

# format autocompletion style
zstyle ':completion:*:descriptions' format "%{$fg[green]%}%d%{$reset_color%}"
zstyle ':completion:*:corrections' format "%{$fg[yellow]%}%d%{$reset_color%}"
zstyle ':completion:*:messages' format "%{$fg[red]%}%d%{$reset_color%}"
zstyle ':completion:*:warnings' format "%{$fg[red]%}%d%{$reset_color%}"

# zstyle show completion menu if 2 or more items to select
zstyle ':completion:*' menu select=2

# zstyle kill menu
zstyle ':completion:*:*:kill:*' menu yes select
zstyle ':completion:*:kill:*' force-list always
zstyle ':completion:*:*:kill:*:processes' list-colors "=(#b) #([0-9]#)*=36=31"

export HISTSIZE=1000
export SAVEHIST=1000
export HISTFILE=~/.config/zsh.d/history

bindkey -v

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Import seperate config files
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

. ~/.config/zsh.d/prompt
. ~/.config/zsh.d/aliases
. ~/.config/zsh.d/functions
. ~/.config/zsh.d/fixkeys
. ~/.config/zsh.d/envars

# Configuracion POWERLVEL9K
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(os_icon root_indicator dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status nvm node_version vi_mode time)

POWERLEVEL9K_OS_ICON_BACKGROUND="white"
POWERLEVEL9K_OS_ICON_FOREGROUND="red"
POWERLEVEL9K_DIR_HOME_FOREGROUND="white"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="white"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="white"

source  ~/powerlevel10k/powerlevel10k.zsh-theme

