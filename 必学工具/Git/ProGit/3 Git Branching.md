# 3.1 Branches in a Nutshell
diverge from the main line and continue working without messing that main line
-> Why Git?
instead of copying the whole project to the new branch, git is *lightweight*

## Switching Branches
`$ git checkout <existing branch name>`
-> can just switch to an existing branch
-> Switching branches will change the file version in the working directory

`$ git checkout -b <new branch name>`
-> create a new branch and switch to it

---
# 3.2 Basic Branching and Merging
## Basic Branching
switch branch?
-> can not do this if *uncommitted changes conflict* with the branching being checked out

`$ git checkout -b hotfix`
`$ vim hotfix.html`
`$ git checkout master`
`$ git merge hotfix`
->merge branch hotfix to the master branch
`$ git branch -d hotfix`
->delete the branch that has been merged

## Basic Merging
just delete a branch after it is merged to another branch

## Basic Merge Conflicts
-> when will the merge conflict happen?
when merge two branches and both of the branches have modified the same file at the same places

1. open the conflicted file manually and resolve those conflicts
2. run `git add` on each file
3. run `$ git commit` again to see the default git merge message
---
# 3.3 Branch Management
`$ git branch`
-> just list all the branches of the repo and the current branch

`$ git branch -v`
-> shows the latest commit on the current branch

`$ git branch --merged or --no-merged`
-> shows all the branches that have been or haven't been merged
-> can not use `$ git branch -d <branch name>` to delete the branches that haven't been merged. 
	Use `$ git branch -D <branch name>` to force the deletion

## Changing a branch name
1. Rename the branch on local repo(old on local disappear)
`$ git branch --move old_name new_name`
-> Remember how to change a file's name in the terminal?
	`mv file_old_name file_new_name`
2. Push the 'new' branch to remote repo
`$ git push origin new_name:new_name`

`$ git branch -a`
-> View all the branches on local and remote repositories
3. Delete the old file ref on remote repo
`$ git push origin --delete old_name `
->Remember? Can also delete unnecessary tags on remote repo using this command

## Changing the master branch name
I recommend not to do this as a green hand

---
# 3.4 Branching Workflows
## Long-Running Branches
`master`: always stable or will be released
`develop` or `next`: not always stable, but when it gets to a stable state, it can be *merged* into `master`
`iss[num]`: different topics and tests, can be merged into `develop`
## Topic Branches
a short-lived branch for a single particular feature or related work(not expensive to create a branch in Git)
`hotfix`
`iss[num]`

---
# 3.5 Remote Branches
view remote repo info
`$ git ls-remote <remote repo name>`
-> this will show all the branches and tags of the remote repo
`$ git remote show origin`
-> this will show all the local and remote branches of the repo

## git remote workflow
`$ git clone <url>`
-> copy remote repo data and branch mark on both local and remote repo
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_clone.png)

->do different work on both the local and remote repo
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/workon_local_remote.png)

-> synchronize local work with remote work
`$ git fetch <remote>`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_fetch.png)

## Pushing
`$ git push <remote> <local branch>:<remote branch>`
-> push local branch to the remote repo

## Tracking Branches
link tracking branches with upstream branches
can use `$ git pull` directly

`$ git checkout -b <branch> <origin/branch>`
->to track a remote branch that the local *do not have*

`$ git branch -u <remote branch>`
-> track the remote branch with the local branch

`$ git branch -vv`
-> See which branches have been tracked

->use `$ git fetch` and `$ git merge` separately instead of `$ git pull`

## Deleting Remote Branches
`$ git push <remote repo> --delete <remote branch>`

---
# 3.6 Git Branching - Rebasing
integrate changes from one branch into another
`$ git merge` or `$ git rebase`
## The Basic Rebase
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_rebase_0.png)
-> simple divergent history
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_rebase_1.png)
->merging to integrate diverged work history

`$ git checkout experiment`
`$ git rebase master`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_rebase_2.png)
-> Rebasing the change introduced in C4 onto C3

`$ git checkout master`
`$ git merge experiment`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_rebase_3.png)
-> Fast-forwarding the `master` branch

-> no difference in the product but `$ git rebase` makes for a *cleaner history*

>  Do note rebase commits that exist outside your repo and that people may have based work on

 ---
# 3.7 Summary
