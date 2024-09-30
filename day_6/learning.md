## Some things that you dont want to add to your git repository 

* sensitive (password)
* large files/folders
* build folders (/bin, /out, etc)
* Hidden  system files 

.gitignore is the solutions


git rm --cached -r .\.idea 


## danger if file is still accesible in previous commits and need to remove?
SOLUTION:
option 1:
remove previous commits with that file (e.g 'git reset' risky)

option 2:
remove github repo
remove sensitive from your local file
remove .git folder from your local repo

option 3: also remove/regeneration credentials 

---