# **Jira**

## General

Jira is a project management software from the company Atlassian. It enables teams to plan entire projects and to track and manage corresponding tasks and issues. For this purpose, these are created as tickets in Jira. For this, it offers a variety of features such as Agile boards, dashboards, reporting and integration capabilities with other tools. It is particularly useful for software development teams, so we decided to use Jira to plan and organize our project.
The first step for this was to create a project in Jira and then set up access for all team members. The corresponding users were then all added to the project with the role "Developer" and assigned the required permissions. 
Now it was necessary to think about how one would like to work in this project. Since the prerequisites of all team members in terms of experience and available time were very different here, agile working should and had to be used. This is now common practice in software development anyway. 


## Configuration

### **Issuetypes** <br />
The next step was to consider what types of tasks might be involved in the project. The number was kept limited and the task types "requirement", "task" and "bug" were created for the project. A "requirement" should describe a function of the software and the tasks to be done for it. Tickets of the type "task" should document these smaller activities. Errors in the software should be recorded as a "bug" in Jira.

### **Workflow** <br />
In order to reduce the administration effort a bit, all mentioned task types follow a common workflow and were not given a workflow of their own. For this one, statuses are necessary, which were created in parallel and are as follows: 
- Planning/Backlog
- Selected for implementation
- In progress/implementation
- In review
- Finished
- Discarded

#### "Planning" <br />
In the planning status, i.e. in the backlog, there are initially all tickets that are created and reflect an idea, task or bug in the project. At the beginning, it was unclear which tasks etc. would arise, how much time there would be for the minimum requirements and whether there might be other ideas for features from the "nice to have" category. However, in order to be able to record all of these and not lose track of all the tasks, this status was set as the first work step.
Afterwards, the project manager or the group should decide whether the respective ticket will be implemented or whether it is irrelevant and can therefore be discarded. Discarded ideas initially end up in their own status and are thus not simply deleted and possibly forgotten, but remain as a ticket and the possibility for later implementation is preserved.

#### "Selected for implementation" <br />
If a ticket is selected for implementation, it can be returned for rescheduling if, for example, something needs to be added or thought about. Otherwise, you can move it to the status "in progress/implementation" to show the team that you are now actively working on it. If you have forgotten this step and have finished working on the respective ticket, you can also set it directly to the status "In review".

#### "In progress/implementation" <br />
The status "in work/implementation" shows the team that they are actively working on the ticket. If it becomes necessary to reschedule, the ticket can be sent back to the backlog from here. If a task has been started but has to wait for another one or is required later, it is possible to return it to the status "To be implemented". When work on a ticket is completed, it is sent to the status "In review" so that the team or project management can view the results. 

#### "In Review" <br />
If a ticket is in the status "In Review", it is ready for a review by the team/project management. If it is determined that something needs to be fundamentally rethought, it can be moved from here to the planning status. If only something small needs to be revised and a team member takes care of it, it is moved back to the status "In progress/implementation". If the results for a ticket are satisfactory, it can be marked as "Done".

#### "Done" <br />
This status marks that a ticket has been finished and that you are satisfied with the results. However, if an error is discovered later or a change is still due, the ticket will be reopened for "Planning" in these cases. 

#### "Discarded" <br />
In this status are all tickets that have no relevance for the project according to the decision of the group/project management. However, it is possible to reverse this decision and resume planning.


The described workflow looks like this:

#### ![Bike sharing - Jira Workflow - grafik](deliverables/Jira_Workflow_-_Bike_sharing_-_grafik.png)


### **Fields**<br />
In order for the tickets to be usable and used to document the work, it had to be decided which fields were needed. Here, we limited ourselves to the essentials and used fields provided by Jira and did not create any of our own. The following fields were included for the project:


|field name|meaning or purpose|
|:----|:----|
|Summary|Topic of the ticket|
|Task type|What type of ticket (request, task or bug)|
|Author|Who created the ticket|
|Assigned Person|Who is responsible for the ticket|
|Components|What category is the ticket in (frontend, backend...)?
|Description|What exactly is the ticket about?
|Due date|When should it be finished|
|Related tasks|Which tickets are related to it|
|Attachment|Field for pictures or documents|
|Affects version|Request the version the ticket affects (bug)|

Other non-relevant fields provided by Jira by default were completely hidden from the project via its field configuration. 
After the required fields had been determined and configured, they then had to be integrated into screen masks so that they are visible and can be edited when creating or transitioning tickets. For this purpose, two screen masks were created. A standard screen for the project with all fields except "Concerns version". As well as a screen for possible bugs with exactly this one field in addition, in order to be able to specify the affected version. At that time it was not yet clear to what extent versions would be used.

### **Screen masks** <br />
These screen masks were then provided for the project via the screen mask scheme and assigned to their activity type. They then had to be activated in the workflow.

### **Components** <br />
So that the tickets can be better distinguished in their subject area, so-called components were created. This way, the tickets could be better categorised. The following components were created for the project and assigned to it:
- Web server
- Administration
- SQL database
- GUI
- Docker

### **Kanban board** <br />
After the basic framework for the use of Jira was in place, a proper overview for the tickets had to be created. For this purpose, a Kanban board was created. This was configured in such a way that first each status is displayed in a column, so that the progress of the project can be read from left to right and each ticket, depending on its status, is displayed in the corresponding column. The columns were named like the associated statuses. In order to be able to distinguish between the different types of tasks, so-called swimming lanes (=lines) have been created. This makes it possible to search for/find the different ticket types in their respective line. The arrangement was set so that bugs are placed in the top row, requests in the middle row and tasks in the bottom row.

### **Connecting Gitlab to Jira**
It is possible to connect Jira to Gitlab via a plugin and thus obtain more detailed documentation of the software development. This option should be integrated for the project and was checked. Unfortunately, creating a connection between Gitlab and Jira failed because the Gitlab used is provided centrally for universities and students by the state of Rhineland-Palatinate. An implementation would have required further considerable effort and probably approval from the state. Therefore, this idea was discarded.

## **Using Jira during the project**
The following is intended to show how Jira was received, used and advanced in the group.
After Jira was set up, some tickets were created right at the first big meeting. These were the first tasks or those that definitely had to be completed at some point during the project. These included, for example, the submissions to the master project manager and lecturer Mr. Scholz. An assignment was made to the persons who had agreed to take on a task in each case. It is already noticeable here that the field for a more detailed description was used rather little. Rather, other devices and media were used for this purpose. In the next period, a first development phase followed, which, however, was not further planned via Jira and was also not documented. The group did not record any tasks that arose, neither their own, nor those that arose for others or were taken on by them. Communication also took place in other ways. Technical documentation was uploaded to Gitlab. Further tickets for upcoming tasks were only created after another break and then assigned to the respective persons at the next big meeting. Again, a little more detail was spared. Another development phase followed in which Jira was used very little to document tasks or problems. Here, too, other communication channels were more in the foreground. In the final phase of the project, the use of Jira reached its peak and tasks were increasingly recorded in tickets and assigned within the group. But here too, the tickets served more as digital reminders, as more detailed task descriptions were recorded verbally or via separate notes. At the end of the project, all tickets created have been processed and have the status "Done".

## Conclusion on Jira in the project
Unfortunately, Jira was used rather sporadically in this project and only for the most important tasks. These tickets were processed and closed with a very good rate. Nevertheless, coordination and planning were increasingly carried out via other media. Gitlab, for example, should be mentioned here, because some commits and merge requests were developed and made here. One can only speculate how Jira would have been used if the connection to Gitlab had worked. However, it should be noted that Jira served the group well as an experience and as a way of getting to know each other. The central tasks were not forgotten and in the end the project can be considered a success and closed.


