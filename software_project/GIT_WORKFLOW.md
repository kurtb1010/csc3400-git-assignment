# Git Workflow Documentation

## Branching Strategy
- main : the main branch is always stable and production ready, no merges happen until it is checked and won't destabilize the main branch
- feature/branch-name : these branches are for new features being implemented. these branches may even have sub feature branches that branch off from this one, that will all get added to the main when it works without errors
- hotfix/branch-name : these branches are for urgent fixes

## Commit Message Conventions
Standard commit message:
git commit -m "Message"

- use clear and descriptive messages to understand the purpose of the commit

Example for adding advanced operations
git commit -m "Added advanced calculator operations"

## Code Review Process
- Every feature branch is reviewed for errors and bugs before being merged into the main branch
- Review process checks:
    - code readability
    - functions correctly
    - style and consistency

## Release Workflow
Once all features for that release are merged into main:
- add a release number (ex. v1.0.0)
- update README.md with release number and new features/ project status
- delete merged branches

## Common Git Commands
- Clone repository:
git clone <repo-url>
- Create branch:
git checkout -b 'branch-name'
- Switch branch:
git checkout 'branch-name'
- State changes:
git add <file>
- Commit changes:
git commit -m "Commit Message"
(Put " " around your commit message)
- Push:
git push -u origin 'branch-name'
- Pull:
git pull origin main
- Delete local branch:
git branch -d 'branch-name'

