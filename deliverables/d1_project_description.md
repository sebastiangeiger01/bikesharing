# **Project Description**

## **Project Members & Roles**

* Project manager & backend developer: Sebastian Geiger
* Deputy project manager & backend developer: Luke Loewe
* Backend Developer: Kai Seegers
* Frontend Developer & Designer: Jonas Frey
* Frontend Developer: Tim Ottenstein
* Frontend Developer: Wilhelm Roman

## **Timeframe & planning**

For the implementation of the "**M**inimum **V**iable **P**roduct", an effort of approximately 50 working hours is estimated. The following topics were considered: 
* Initial set-up of the project - 2 hours
* Finding the appropriate services - 3 hours
* Implementation of the backend - 25 hours
* Implementation of the frontend - 15 hours
* The documentation - 5 hours

## **Budget**

Within this university project only those resources and services should be used that don’t incur costs, either for the user or for the implementation team.

## **Product Vision**

The need to urgently change to a climate friendly way of living is increasingly obvious to all of us. This raises demand in green, healthy and energy efficent mobility solutions. 
We want to enable citys, communitys and companies to offer safe, easy to set up & convenient bike rental services to their respective target groups. We envision our software product to be the connection point between people who love riding bikes & organisations searching to empower those people. The application will be accessible for all end user devices with web browsers and there is no need for additional software to be installed. 

## **User Story**
Imagine you are the mayor of a small city in the suburbs of a major city. You know that there is a huge demand in your population for easy to use and cheap public transport, but big investments in new busses or even train stations are not in your citys budget. So you think about offering a bike rental, especially because you heard that a lot of your residents wish for it. But this would still require a huge investment, in bikes and in IT infrastructure to manage the bike rental. 

Now we come into play! With our easy to set up, customize and scalable bike rental software solution, offering a bike rental is cheaper than ever and almost effortless. The costs and worries of developing an IT solution are thus out of your mind.
Wether you are a mayor like in our example, a company wanting to offer bike rental to their employees or a community of bike rental enthusiasts - to use our solution, you just have to do the following:

 * Download the Docker images for our webserver and database to your own server & start the containers
 * Personalize the frontend to your liking
 * Register your bikes in the database

And your done!

The users of the bike rental will easily be able to rent a bike by visiting the website, register/log in, selecting the bike they want to rent on a map and book it. Easy as eating cake.
To return the bike, they'll just have to visit the site again, log in and click on a return button.


## **Target Users**

BikeRental is aimed specifically at cities, communitys and companies that want to rent bikes to others without the need to develop a complicated IT infrastructure first.

# **Software-Architecture**

## **Execution Model**

BikeRental is a "Platform as a service" solution. All product features and logic are implemented and executable in containers that have to be hosted by the users of the software. They will have to make the inital database entrys of bikes themselves, create domains to access the service for end users and edit the frontend to their liking (if they want to).

## **UI/UX-Design**

The interface design will be developed according to the principle of 'Mobile First'. The core element of the website is the map on which the rentable bikes positions are shown. The design should be kept very simple and easy to use, so without creating unnecessary barriers for users.

## **Interfaces**

The most important interface is the connection to a map service. Which map service best suits the project requirements has yet to be determined. 
A database interface will have to be used to store the bikes locations and show them on the websites map.

## **MVP**

With this "**M**inimum **V**iable **P**roduct" we would like to reach a development stage where only the core functions are covered. According to the team's assessment, the following features should be provided:
* A website with a map that shows dummy-GPS-data for rental bikes.
* The software shall be hostable by running the provided Docker images. Some knowledge about running containers, setting up web servers, editing database entrys etc. will be required by the users wanting to host the service.
* The application must offer the end users the possibility to register/log in and rent a bike that's on the map. As soon as the bike is rented, it will not show up on the map until returned.
* The backend will store user login data, bikes with their GPS locations as well as logs of the rentals.

The functionality needed for unlocking the bike when being rented out will not be a part of our scope.


