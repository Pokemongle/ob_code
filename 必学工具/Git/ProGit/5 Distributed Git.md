# 5.1 Distributed Workflows
# Centralized Workflow
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/CVS_workflow.png)

## Integration-Manager Workflow
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_workflow.png)

## Dictator and Lieutenants Workflow
Used by huge projects with hundreds of collaborators
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/git_benevolent_dictator_workflow.png)

# 5.2 Contributing to a Project
## Commit Guidelines

## Private Small Team
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/private_team_workflow_0.png)
-> The simplest workflow of a small private team
## Private Managed Team
`$ -u` is short for `$ --set-upstream`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/managedTeamWorkflow.png)
->Managed Team Workflow
## Forked Public Project
1. clone the original repo to local directory
```git
$ git clone <url>
$ cd project 
...work...
$ git commit
...work...
$ git commit
```
2. fork the original data to the remote repository
3. add the forked repo as the remote repo
`$ git remote add myfork <url>`
4. push the work to the forked remote repo
`$ git push -u myfork featureA`
-> recommend to directly push the topic branch to the remote repo because the work you've done may not be accepted by the author of the origin repo
5. Add a pull request
`$ git request-pull origin/master myfork`
