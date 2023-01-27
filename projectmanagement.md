# Projectmanagement
## Jira
Jira is a project management tool developed by Atlassian that allows teams to track, prioritize, and manage tasks and bugs in a software development process. It offers features such as agile boards, sprint planning, and customizable workflows to help teams stay organized and on track. Additionally, Jira can be integrated with other tools and has a robust API for customization and automation. It is widely used in software development, IT and other industries for agile project management.

For the BikeRental project we have chosen an agile project management method. We created a kanban board in jira and invited all team members. We split our team of 6 into a 3 member frontend team and a 3 member backend team. Once a month we set a 1 hour meeting where we defined our tasks and shared results. Kai Seegers was the moderator/project manager who entered the tasks on the kanban board, communicated the dates for the meetings, and reminded the team of deadlines. Within the teams of 3, communication took place on a weekly to daily basis. 

## Gitlab
GitLab is a web-based Git repository manager that provides source code management (SCM), continuous integration, and more. It allows teams to collaborate on code, track and manage changes, and build, test, and deploy software. GitLab provides a single unified platform for the entire software development life cycle, from idea to production. It also offers features such as issue tracking, wiki, and project management. GitLab is open-source and can be self-hosted or used as a service. It is widely used for software development and also DevOps.

### Git Repository
In a Git repository, branches are used to create separate lines of development for a project. By default, most Git repositories have a "master" branch which represents the production-ready code. Developers can create new branches to work on new features or bug fixes without affecting the main branch.

Merge requests are used to bring changes from one branch into another. A developer creates a merge request to propose changes to the main branch. Then, other members of the team can review the code, discuss it and if all is good, approve and merge the changes into the main branch.

For the BikeRental project, we created a master branch and have agreed on a naming convention for branches. The branch name must start with its own type and after a slash follows a description, for example feature/newMap or documentation/mapCode. Other branch types are listed below:

1. `feature branches`: Branches used for developing new features, typically named with a prefix of "feature/". Example: feature/new-login-page
2. `hotfix branches`: Branches used for quickly patching production bugs, typically named with a prefix of "hotfix/". Example: hotfix/critical-security-issue
3. `release branches`: Branches used for preparing a new release, typically named with a prefix of "release/". Example: release/v1.0
4. `develop branches`: Branches used as a staging area for features before they are merged into the master branch. Example: develop
5. `master branches`: The default branch where the production code lives.

After a change was completed in a branch, a merge request had to be created. Since the master branch was protected, two other team members had to view and test the changes first. If the branch was error-free, the two team members could approve it and then merge it with the master branch.

## Testing
Luke Löwe, Sebastian Geiger, Jonas Frey and Kai Seegers were responsible for the testing.

