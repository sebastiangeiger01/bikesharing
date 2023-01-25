## Wireframes
At the beginning of the project, so-called wireframes were created. Wireframes are simple visual sketches that are used to plan the basic structure of a user interface. A wireframe shows the basic layout, the possibilities for navigation and only the basic functions of the website.   

A wireframe itself usually has no images and usually no colors yet. This is so that only the elements themselves can be arranged and structured. Content is also not yet created in the wireframe. Typically placeholder texts are used for this.   

Theoretically, simple wireframes can even be drawn by hand. However, there are now many software offerings with which exactly such wireframes can be easily created. Besides Figma and Adobe Suit, which would have been too complex for this project, the software WireframeSketcher from wireframesketcher.com came in handy. This program is appropriately easy to use and has all the capabilities to create a simple wireframe.  

Below are three images showing the wireframes of the website.   

The first image shows the planned home page. The first approximately 50 percent of the screen is supposed to be an interactive map where bikes can later be rented. Above this is a simple navigation bar that can be used to navigate to all sub-pages. Below this is a so-called call-to-action section, which is intended to lead the user to interact with the button, but whose function is not yet specified in the wireframe. Next to it there will be a graphic. Below that, there are boxes of information about the bike rental and the team behind BikeSharing. The page ends with a footer with the usual links to be found there. 
![alt text](https://gitlab.rlp.net/software-engineering/2022/bike-sharing/-/raw/docu/jonas/deliverables/wireframes/home.png)


The following wireframe shows the "Shop Page" of a single bike. On the left side there is space for a picture of the bike. On the right side, there is information about the bike, with the possibility to rent it directly by clicking a button. Below is a map, so that the user can see directly where this one bike is located. 
![alt text](https://gitlab.rlp.net/software-engineering/2022/bike-sharing/-/raw/docu/jonas/deliverables/wireframes/bike.png)

The last wireframe shows our so-called "dashboard". This is the administration area, which can only be accessed with the appropriate rights. We decided to design this dashboard so that the administrators do not have to work with the database management systems every time, but can also work directly from the page. In total, there are two pages that can be found in the dashboard. One page is for creating, deleting and editing users, the other page equivalent to this for bikes.
![alt text](https://gitlab.rlp.net/software-engineering/2022/bike-sharing/-/raw/docu/jonas/deliverables/wireframes/BikeManager-UserManager.png)
## Color Scheme
It was intended from the beginning to use comparatively few colors on the website. The homepage should make a clean and user-friendly impression. For this, gaudy colors and too many animations were dispensed with. 
Since BikeSharing is an environmentally friendly way to travel from A to B, colors that can be found in nature were the most suitable. The color green is associated with nature and is considered the "color of flora". It is also associated with concepts such as clarity, freshness, openness and awareness. The color blue is associated with purity, relaxation, non-confrontational, organizing and controlling.

Due to this, a predominantly white background was chosen, paired with turquoise (mixture between blue and green) and blue elements.
The following color palette shows which colors were mainly used:
![alt text](https://gitlab.rlp.net/software-engineering/2022/bike-sharing/-/raw/docu/jonas/deliverables/ColorScheme.png)


## Bootstrap
Bootstrap is an open source front-end web development library developed by Twitter.  
Bootstrap provides a set of templates and styles for designing websites and applications. This includes CSS files for layout, typography, forms, buttons and other elements. Bootstrap is designed to simplify the development of responsive websites by providing a standardized set of tools and styles.  
It is popular mainly because it is almost completely supported by every major browser. Also, there is a large Bootstrap community, sharing designs with each other for free and without licensing conditions.  
Overall, Bootstrap is a powerful tool for developing websites and applications and is used by many developers because of its simplicity and power.


## Dynamische und statische Webseiten
A web page can be either static or dynamic. A static web page consists of HTML files that are stored on the server and sent directly to the user when the web page is called. A dynamic web page, on the other hand, generates the content only when it is called up, by retrieving data from a database and inserting it into the HTML files.  
Since the data of bikes, users, and rides are stored in a database, it will also be necessary to display them on the web page. This is enough reason to decide to create a dynamic website. 
Another reason why websites should be built dynamically is that the maintenance effort decreases significantly. Thus, it is possible to avoid redundancies. There is always content that should be displayed on different subpages. With static websites there would be the problem that the data is stored in several places at the same time. By dynamizing the pages, data is stored centrally and therefore only referenced.  
This not only saves storage space on the web server, but also ensures that the data is always available in a consistent manner. 
Other data coming from the database or the backend are specified in a shortcode. This is surrounded by two braces and is provided by the backend. This code snippet is then inserted in the frontend. When a user calls the page, this code snippet renders to the corresponding data that the backend passes with it.
