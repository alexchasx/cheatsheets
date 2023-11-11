
# Configuring console command aliases in Openserver

Settings path: 
console -> right mouse button -> Settings -> Startup -> Environment

```bash

alias h=history
alias c=clear
alias cd~=cd %ConEmuDir%\..\..\domains
alias cd1=cd %ConEmuDir%\..\..\domains\html
alias cd2=cd %ConEmuDir%\..\..\domains\local

# git
alias gs=git status 
alias ga=git add .
alias gc=git commit -m $* 
alias gaf=git add $* 
alias gaa=git add -A 
alias gpl=git pull 
alias gps=git push 
alias gca=git commit -a $* 
alias gcam=git commit -am $* 
alias gch=git checkout $* 
alias gchf=git checkout -f
alias gbr=git branch 
alias gl=git log
alias glpo=git log --pretty=oneline 
alias glpon=git log --pretty=oneline -n $*

# laravel
alias pa=php artisan $*  
alias paclear=php artisan cache:clear && php artisan view:clear && php artisan route:clear && php artisan config:clear && php artisan clear-compiled

```