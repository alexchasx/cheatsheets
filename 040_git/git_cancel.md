```bash 
# Перезаписать последний коммит
git commit --amend   


# ---- ОТМЕНА ДО `git add`(индексации)

# во всех файлах
git checkout -f

# в файле
git restore <file>
# или (ОПАСНО)
git checkout -- <file> 
# или (ОПАСНО)
git checkout <file>  


# ---- ОТМЕНА ПОСЛЕ `git add`

# во всех файлах
git reset HEAD
# или
git reset --hard

# в файле
git rm --cached <file>
# или
git restore --staged <file>  
# или
git reset HEAD <file>  


# ---- ВРЕМЕННЫЙ ОТКАТ

# Времен. сброс незафикс. измен-й
git stash

# Вернуть после `git stash`
git stash pop


# ---- ОТМЕНА ДО ОПРЕДЕЛЁННОГО КОММИТА 

# отмен. коммит до предыд. версии 
# (--no-edit  - без редактора)
git revert HEAD --no-edit

# Отменяет коммит, используя его хэш
git revert <hash>
# или (ОПАСНО)
git reset --hard

# Отменяет коммит, помеченный тегом
git revert <tag>

# отмена коммита слияния
git revert <hash> -m 1

# Состояние отдел. HEAD, не указ. на ветку
git checkout <hash>

# в файле
git checkout <hash> <file>

# файл к состоянию на два коммита назад
git checkout HEAD~2 <file>
```