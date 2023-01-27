![This is an image](https://www.lehrer-online.de/fileadmin/user_upload/Hochschule_Mainz-Logo-W-orange-4c_324x174.png)

# **D2: Personas, Scenarios, User Stories**

# **Bike Sharing**

Software Engineering (A) // 626-2304/A // Scholz
Hochschule Mainz

<details><summary>Project Members & Roles</summary>
<p>

## **Project Members & Roles**

* Project manager & backend developer: Sebastian Geiger
* Deputy project manager & backend developer: Luke Loewe
* Backend Developer: Kai Seegers
* Frontend Developer & Designer: Jonas Frey
* Frontend Developer: Tim Ottenstein
* Frontend Developer: Wilhelm Roman

</p>
</details>


<details><summary>Personas</summary>
<p>

## **1. Personas**

   ### **1.1) Bruno Pressazk, Mayor**
   Bruno, 52, is the mayor of a small municipality in Mu-nich. He completed a dual degree in banking at the BankColleg in Würzburg and is a passionate cyclist. In his new  candidacy, he is promoting the possibility of renting bicycles at low cost.

   ### **1.2) Dr. Peter Wiesemann, CEO**
   Peter, 44, has been managing a medium-sized compa-ny with 200 employees since 2013. His employees want an environmentally friendly way to get to their cus-tomers. After acquiring electric cars, the company now also wants to offer the option of cycling to their nearby customers.

   ### **1.3) Petra Schlauberger, Costumer**
   Petra, 21, is a student and works as a reporter for a small journalist while studying. She is in the process of finding a way to rent cheap bicycles.

</p>
</details>


<details><summary>Scenarios</summary>
<p>

   ## **2. Scenarios**

   ### **2.1) Bruno Pressazk**
   #### *Use for municipalities*
   An important task of the mayor is to lead the municipality. The mayor advises and helps to decide whether there should be a possibility for citizens to rent bicycles at low cost. With this possibility, the municipality could cooperate with the local bicycle shops and provide a new cost-efficient and future-proof answer to public transport.
To launch the bike rental, the mayor himself or the members of statt from the commune can follow our [instructions for starting your own bike rental](https://gitlab.rlp.net/software-engineering/2022/bike-sharing/-/blob/docu/sebastian/deliverables/deployment.md). Only some basic technical knowledge will be needed.
As an administrator of the service you will not only be able to edit the appearance of the website, but also can see who rented which bike when. Thus, you can gather information about the workload of your bike fleet and keep the renters accountable.
    
   ### **2.2) Dr. Peter Wiesemann**
   #### *Use for management*
   As the head of a 200-person company, it is important to Peter that all his employees have a way to travel around the company premises or to customers in an environmentally friendly way. With an easy-to-set-up, customisable and scalable software solution, renting is almost effortless for his employees. This software solution does not require any major investment.
   Dr. Wiesemann can follow our [instructions for starting your own bike rental](https://gitlab.rlp.net/software-engineering/2022/bike-sharing/-/blob/docu/sebastian/deliverables/deployment.md), just like Bruno Pressazk could, to start the bike rental, add/remove bikes to his fleet and administrate the rental. Once operational, it is easy to customize the UI and adopt it to align with corporate identity by editing the frontend files.
   
   ### **2.3) Petra Schlauberger**
   #### *Use for customer*
   Petra could rent a bike at any time through a web-based bike rental service to do her job. Not only your job, but also a small contribution to the environment and your own health.
   To rent a bike, Petra can enter the url provided by her local bike rental in all common web browsers. After logging in/registering she will see a website with a map showing all available bikes in her city. By choosing a bike on the map, she will be forwarded to a page for the bike, showing some basic information of the bike (e.g. a picture of the bike) and a button to rent the bike. 
   To the a rental, she will have to return the bike to the location where she picked it up & click on a button to give back the bike.

</p>
</details>


<details><summary>User Stories</summary>
<p>


   ## **3. User Stories**

   - As a mayor, I can offer a web-based and cost-efficient bike rental service for the municipality and the citizens.
   -As a mayor, I can have control over my bike fleet and add as well as remove new bikes easily
   - As a manager, I can offer my staff an internal and environmentally friendly option for bike hire.
   - As a customer, I can rent bicycles easily and without complications.
   - As a customer I can register via the website to rent bicycles 
   - As a customer, I can see at a glance where and how many bicycles are available.
   - As a customer I can rent a bike by pressing a button.
   - As a customer, I will be asked for permission to retrieve my GPS data.
   - As a customer, I can set up the system myself via Docker and a manual without having to develop it myself.
   - As an operator, I would like to create the data for the bicycles independently.
   - As an operator, I would like to have quick access to the data.
</p>
</details>
