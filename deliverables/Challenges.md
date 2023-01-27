# Challenges 

During a project, there are always new challenges that the project team faces. This project was no different. Therefore, we will show here a little bit what they were and how they were solved.

## General

### Finding a Topic

The basic challenge at the beginning of the project was to find a topic, but this was solved relatively quickly. A team member had explained one of his private interests to the group and the group was immediately enthusiastic about the proposed project. Bike sharing was born.

### Group coordination and time management

Since the group is relatively large with six members, it was clear from the beginning that, for one thing, the time planning and coordination had to be well managed. Many team members work at different times. Therefore, this point was also included in the risk assessment. The difficulties in coordinating the cooperation could be limited through the use of additional media such as WhatsApp and Zoom. This made it easy to exchange information and participate in meetings online from different locations.

### Skills and Expertise

In group projects, different levels of technical knowledge and expertise inevitably come together among the team members, so everyone has their strengths and weaknesses. This has to be taken into account in such a project and was also assessed as a risk. These different levels of knowledge about the tools to be used were tried to be balanced out by the respective experts in the group holding small training sessions for the team.

### Establishing requirements
In projects, the team has to agree among themselves on requirements for the software, unless there is a real client to take over or provide them. In this project, there was no real client. There were rough requirements, but otherwise the software was free to be designed during development. Therefore, the team had to agree on what their demands and requirements were for the software. Here, the team was mostly in agreement and appropriate solutions could usually be found.

## Technical

In the course of a software project, unforeseen technical errors or operating errors can always occur. The following problems occurred:

### Connection to GitLab 
Every now and then, team members had problems with their SSH connection to the Gitlab server. This led to delays and problems in completing some tasks. Since the exact causes could not be found, the only option was to generate a new SSH key to solve the problem. 

### Docker
During the development phase, problems arose when working with Docker. On the one hand, it was unfortunately discovered that Docker, and thus also the Docker Desktop App shown to the team, cannot be run on one of the notebooks. This meant that this notebook could not be used for development and an alternative computer had to be organised or procured. But even on this computer, there were initially problems getting Docker to run, as it simply wouldn't start. A command "docker-compose up" inevitably led to an error again and again: <br />
<br />
_Error invoking remote method 'docker-start-container': Error: (HTTP code 500) server error - Ports are not availiable: exposing port TCP 0.0.0.0:80 -> 0.0.0.0:0: listen tcp 0.0.0.0:80: bind: An attempt was made to access a socket in a way forbidden by its access permissions._
<br />
<br />
After an analysis of the error message and the Docker log by the team, it was determined that other processes might be blocking Docker from starting and getting in the way. Thereupon, an extremely complex search for the cause was started and was found deep in the Windows operating system. Here, a setting that was probably made by some other programme during its installation prevented Docker from starting. After changing this setting, the problem was solved and it was possible to develop properly on this computer. 
Another computer, on the other hand, had massive problems with Docker's performance. The PC became extremely slow overall, so that graphical interfaces were very jerky and there were eternally long waiting times. Starting Docker itself took quite a long time, as did creating containers via "docker-compose build" and booting these containers. This resulted in significant time restrictions and sometimes frustration for the developer concerned. Unfortunately, it was not possible to replace the PC or install more powerful components. The performance problem had to be accepted throughout the entire project.

### Frontend - Backend

Flawless technical cooperation between the frontend and the backend is essential for software, as it cannot function without it. In the development process, as with any software, there were problems here and there in this project. An example of this was during the development of the bike management page. Once there were problems with the creation of bicycles. After discussion between the two development teams, it turned out that there was a misunderstanding in the frontend regarding the API and the implementation of the backend. Later, errors occurred again when deleting bikes, when the layout of the bike management page was revised again and was to be tested. These errors were then corrected by adjustments in the backend.






