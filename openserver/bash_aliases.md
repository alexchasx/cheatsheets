
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
alias gcam=git commit -am $* 
alias gpl=git pull 
alias gps=git push 
alias ga=git add .
alias gch=git checkout $* 
alias glpo=git log --pretty=oneline 

# laravel
alias pa=php artisan $*  
alias paclear=php artisan cache:clear && php artisan view:clear && php artisan route:clear && php artisan config:clear && php artisan clear-compiled

```