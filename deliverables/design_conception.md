# Definition User Interface (UI)
The focus of user interface design is on the visual design of digital applications. A good user interface is by no means just visually high-quality design; in addition to the design, the goal of the application and the brand message must be conveyed via the visual expression of websites.
The user interface is the element through which users interact with an interactive application. This interaction must be efficient and effective, which in turn can only be achieved through intuitive usability. For a user interface to develop its full potential, it must also be visually appealing. If we take the example of the large number of touchpoints mentioned above, the individual interfaces must be designed consistently on the various devices.

# Definition User Experience (UX)
The focus of user experience design is on creating experiences. A successful UX is composed of various factors, for example, in addition to usability, the feeling that arises before, during and after the use of an interactive application is relevant.
A good user experience design satisfies people's context of use regardless of the communication channel or device used. In addition, it is important that a brand has a consistent appearance and communication style.

# Wireframes
At the beginning of the project, so-called wireframes were created. Wireframes are simple visual sketches that are used to plan the basic structure of a user interface. A wireframe shows the basic layout, the possibilities for navigation and only the basic functions of the website.   

A wireframe itself usually has no images and usually no colors yet. This is so that only the elements themselves can be arranged and structured. Content is also not yet created in the wireframe. Typically placeholder texts are used for this.   

Theoretically, simple wireframes can even be drawn by hand. However, there are now many software offerings with which exactly such wireframes can be easily created. Besides Figma and Adobe Suit, which would have been too complex for this project, the software WireframeSketcher from wireframesketcher.com came in handy. This program is appropriately easy to use and has all the capabilities to create a simple wireframe.  

Below are three images showing the wireframes of the website.   

The first image shows the planned home page. The first approximately 50 percent of the screen is supposed to be an interactive map where bikes can later be rented. Above this is a simple navigation bar that can be used to navigate to all sub-pages. Below this is a so-called call-to-action section, which is intended to lead the user to interact with the button, but whose function is not yet specified in the wireframe. Next to it there will be a graphic. Below that, there are boxes of information about the bike rental and the team behind BikeSharing. The page ends with a footer with the usual links to be found there. 
![alt text](/deliverables/wireframes/home.png)


The following wireframe shows the "Shop Page" of a single bike. On the left side there is space for a picture of the bike. On the right side, there is information about the bike, with the possibility to rent it directly by clicking a button. Below is a map, so that the user can see directly where this one bike is located. 
![alt text](/deliverables/wireframes/bike.png)

The last wireframe shows our so-called "dashboard". This is the administration area, which can only be accessed with the appropriate rights. We decided to design this dashboard so that the administrators do not have to work with the database management systems every time, but can also work directly from the page. In total, there are two pages that can be found in the dashboard. One page is for creating, deleting and editing users, the other page equivalent to this for bikes.
![alt text](/deliverables/wireframes/BikeManager-UserManager.png)
# Color Scheme
It was intended from the beginning to use comparatively few colors on the website. The homepage should make a clean and user-friendly impression. For this, gaudy colors and too many animations were dispensed with. 
Since BikeSharing is an environmentally friendly way to travel from A to B, colors that can be found in nature were the most suitable. The color green is associated with nature and is considered the "color of flora". It is also associated with concepts such as clarity, freshness, openness and awareness. The color blue is associated with purity, relaxation, non-confrontational, organizing and controlling.

Due to this, a predominantly white background was chosen, paired with turquoise (mixture between blue and green) and blue elements.
The following color palette shows which colors were mainly used:
![alt text](/deliverables/ColorScheme.png)



# Bootstrap
Bootstrap is an open source front-end web development library developed by Twitter.  
Bootstrap provides a set of templates and styles for designing websites and applications. This includes CSS files for layout, typography, forms, buttons and other elements. Bootstrap is designed to simplify the development of responsive websites by providing a standardized set of tools and styles.  
It is popular mainly because it is almost completely supported by every major browser. Also, there is a large Bootstrap community, sharing designs with each other for free and without licensing conditions.  
Overall, Bootstrap is a powerful tool for developing websites and applications and is used by many developers because of its simplicity and power.


# Dynamische und statische Webseiten
A web page can be either static or dynamic. A static web page consists of HTML files that are stored on the server and sent directly to the user when the web page is called. A dynamic web page, on the other hand, generates the content only when it is called up, by retrieving data from a database and inserting it into the HTML files.  
Since the data of bikes, users, and rides are stored in a database, it will also be necessary to display them on the web page. This is enough reason to decide to create a dynamic website. 
Another reason why websites should be built dynamically is that the maintenance effort decreases significantly. Thus, it is possible to avoid redundancies. There is always content that should be displayed on different subpages. With static websites there would be the problem that the data is stored in several places at the same time. By dynamizing the pages, data is stored centrally and therefore only referenced.  
This not only saves storage space on the web server, but also ensures that the data is always available in a consistent manner. 
Other data coming from the database or the backend are specified in a shortcode. This is surrounded by two braces and is provided by the backend. This code snippet is then inserted in the frontend. When a user calls the page, this code snippet renders to the corresponding data that the backend passes with it.


## Inheritance of Base.html
The Base Template is an important concept in web development with Flask. It is a template that defines the basic structure and layout of a web page and serves as a base for other templates.  
The Base.html can contain elements such as a header, footer, and a main content area. It is typically used by means of the extends directive in other templates to indicate that the new template should inherit from the base template.
The Base.html opens the HTML document with the corresponding doctype and the complete head area and contains all necessary links to different stylesheets and a link to the favicon. 

The body area of the Base.html also contains the role-based main menu and the footer.  Any page that now inherits from Base.html will be rendered between the menu and the footer. So these two big contents don't have to be created every time.
![alt text](/deliverables/vererbung_frontend.png)
# Leaflet
Leaflet is an open source JavaScript library for creating interactive maps on the web.
Leaflet provides a variety of features and tools that allow developers to customize and design maps, add markers and pop-ups, and more. It is also very easy to integrate and compatible with most modern web browsers and devices.  
In summary, Leaflet is a useful JavaScript library for creating interactive maps on the web. It is easy to integrate and provides a variety of tools and features for designing maps. It is especially suitable for those who want to integrate maps into web pages and applications. 
Before leaflet was integrated, it was tested to see if it met the requirements of the project. For this purpose, the map local was included in an HTML file. The rendering of the map worked without any problems. Afterwards it was tested if it is possible to place a marker on the map using x and y coordinates. This was achieved with simple PHP scripts. When this function was also achieved, it was clear that Leaflet was suitable for this project and was finally implemented as follows
