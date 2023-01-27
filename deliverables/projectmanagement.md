# Projectmanagement
Project management is the process of planning, organizing, and overseeing the work of a team to achieve specific goals and objectives. This includes identifying and defining project goals, establishing tasks and deadlines, acquiring resources, and monitoring progress to ensure that the project is completed on time, within budget, and to the satisfaction of all stakeholders. 

## Jira
Jira is a project management tool developed by Atlassian that allows teams to track, prioritize, and manage tasks and bugs in a software development process. It offers features such as agile boards, sprint planning, and customizable workflows to help teams stay organized and on track. Additionally, Jira can be integrated with other tools and has a robust API for customization and automation. It is widely used in software development, IT and other industries for agile project management.

For the BikeRental project we have chosen an agile project management method. We created a kanban board in jira and invited all team members. We split our team of 6 into a 3 member frontend team and a 3 member backend team. Once a month we set a 1 hour meeting where we defined our tasks and shared results. Kai Seegers was the moderator/project manager who entered the tasks on the kanban board, communicated the dates for the meetings, and reminded the team of deadlines. Within the teams of 3, communication took place on a weekly to daily basis. 

## Gitlab
GitLab is a web-based Git repository manager that provides source code management (SCM), continuous integration, and more. It allows teams to collaborate on code, track and manage changes, and build, test, and deploy software. GitLab provides a single unified platform for the entire software development life cycle, from idea to production. It also offers features such as issue tracking, wiki, and project management. GitLab is open-source and can be self-hosted or used as a service. It is widely used for software development and also DevOps.

### Git Repository
In a Git repository, branches are used to create separate lines of development for a project. By default, most Git repositories have a "master" branch which represents the production-ready code. Developers can create new branches to work on new features or bug fixes without affecting the main branch.

Merge requests are used to bring changes from one branch into another. A developer creates a merge request to propose changes to the main branch. Then, other members of the team can review the code, discuss it and if all is good, approve and merge the changes into the main branch.

For the BikeRental project, we also created a master branch and have agreed on a naming convention for branches. New branches must start with its own type and after a slash follows a description, for example feature/newMap or documentation/mapCode. Other branch types are listed below:

1. `feature branches`: Branches used for developing new features, typically named with a prefix of "feature/". Example: feature/new-login-page
2. `hotfix branches`: Branches used for quickly patching production bugs, typically named with a prefix of "hotfix/". Example: hotfix/critical-security-issue
3. `release branches`: Branches used for preparing a new release, typically named with a prefix of "release/". Example: release/v1.0
4. `develop branches`: Branches used as a staging area for features before they are merged into the master branch. Example: develop
5. `master branches`: The default branch where the production code lives.

After a change was completed in a branch, a merge request had to be created. Since the master branch was protected, two other team members had to view and test the changes first. If the branch was error-free, the two team members could approve it and then merge it with the master branch.

## Testing
### Connect Gitlab with Visual Studio Code
To test the changes, you has to link your IDE to Gitlab. This allowed you to download and publish branches from or to other team members and view the source code. For the BikeRental project we used the IDE Visual Studio Code. To link a GitLab repository with VS Code, you can use the built-in Git integration. Here are the steps to follow:

1. Open Visual Studio Code and navigate to the Source Control tab (the icon with the "T" in the left sidebar).
2. Click the "+" icon in the top left corner of the Source Control pane to create a new repository.
3. In the "Clone Repository" dialog that appears, enter the URL of your GitLab repository.
4. Click the "Clone" button to clone the repository to your local machine.
5. Once the repository is cloned, you can navigate through the files and make changes.
6. To commit your changes and push them to the remote repository, open the Source Control tab, make your changes, add a commit message and press the check icon.
7. If you want to keep your local repository up to date with the remote repository, you can use the "Fetch" and "Pull" options in the Source Control pane.

Note: To use Git in VS Code you will need to have Git installed and configured on your system. 

### Restart Docker Container
To test the program code, the Docker containers had to be terminated and started with the new source code. This was possible using the "docker compose up --build" command in the terminal of VS Code.

After that the web application could be reached via /localhost and the changes could be tested. If an error was detected or other problems occurred, a comment was created on the merge request and the owner of the branch had to fix the problems.

