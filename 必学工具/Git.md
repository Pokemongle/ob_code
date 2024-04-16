[How to Write a Git Commit Message](https://cbea.ms/git-commit/)
[The seven rules of a great Git commit message](https://cbea.ms/git-commit/#seven-rules)
> Use the body to explain what and why vs. how
	 ` Fix the typo in introduction to user guide`

1. Separate subject from body with a blank line
	` git commit -m "commit message"`
	- Message title
	- Message body
		recommend `vim`
		[Customizing Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
	- git-log configuration
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202404162313001.png)
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202404162314335.png)
2. Limit the subject line to 50 characters
3. **Capitalize** the subject line 
	`Accelerate to 88 miles per hour`
	~~`accelerate to 88 miles per hour`~~
4. Do not end the subject line with a *period*
	`Open the pod bay doors`
	~~`Open the pod bay doors.`~~
5. Use the imperative mood in the subject line
	Use *verb* at the beginning of a sentence
	- If applied, this commit will <u>your subject line here</u>
	`Refactor subsystem X for readability
	`Update getting started documentation`
	`Remove deprecated methods`
	`Release version 1.0.0`
6. Wrap the body at 72 characters
7. 