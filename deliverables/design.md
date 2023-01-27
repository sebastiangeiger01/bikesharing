# Rolebased Mainmenu
The main menu of the website is role-based. This means that the content changes whenever the user's role is different. 
At the beginning, when the user is not logged in, the main menu appears rather empty. There are only two buttons with the possibility to register or login.  
As soon as the user is logged in, these links are swapped. The user now has the possibility to change his password or to log out at the same place. 
If the user has an administrative role on the website, i.e. is either a user or bike manager, then additional entries are displayed in the main menu. The user has the possibility to access the dashboard via the new links that appear.
The following shortcodes were used to query the appropriate logic to determine if a user is authenticated and what roles they have. According to this the frontend was rendered.
```
{% if current_user.has_role('bike-manager') %} 

{% if current_user.has_role('user-manager') %} 

{% if current_user.is_authenticated %} 
```
# Responsive Design
The website was created directly responsive, using the Bootstrap framework. Responsive design refers to the ability of websites to automatically adapt to the size and aspect ratio of the screen on which they are displayed. This is important as more and more people are accessing websites through different devices and screen sizes, and it is important that the website looks good and is usable on all devices. 
# Dashboard
Since we decided to also implement a backend for administrators, a backend with a corresponding user interface was also created. This has the advantage that it is not necessary to work directly on database systems or other admin tools, but directly from the website. The admin panel is accessible with appropriate rights. The logged in admin has two additional entries in the main menu, which he can use to access either the user management or the bike management. 
The interface for administrators should be kept simple. The goal was to map the most important functions directly so that each function can be performed without scrolling or additional navigation on the page. 
For this purpose, two forms were added to the user management, which can be used to create and edit new users. 
Below these forms there is an automatically generated table with all necessary information about the users. In the last column there is also a red button with a trash can icon, which can be used to easily remove users.  
The bike management page has a similar structure. However, above it there is a map with two read-only fields with X and Y coordinates. During development, we noticed that it is very complicated to add bikes if you don't have the exact coordinates of the bike. In order to not have to rely on external tools from the Internet that calculate a location into the corresponding coordinates, such a function was implemented directly. By dragging the marker on the map, the data in the coordinate fields are updated. So the admin has the possibility to easily find out the coordinates for new bikes. 
The API for the complete dashboard was provided by Backend Team. 
## Errorhandling
The entries in the dashboard can cause errors. For example, if the admin enters invalid values for the coordinates or leaves a field blank. Here it would have gone beyond the scope of the project if the backend would have had to catch error cases, which are then returned via the frontend. In order to still inform the admin about success or failure when editing the data, the various jQuery functions provided by the backend were used. Depending on the success, the functions .done or .fail were called, which rendered a standard alter window with the corresponding message.
```javascript
.done(function (data, textStatus, jqXHR) {
  console.log("HTTP Request Succeeded: " + jqXHR.status);
  console.log(data);
  alert('Rolle wurde zugewiesen');
  location.reload();
})
.fail(function (jqXHR, textStatus, errorThrown) {
  console.log("HTTP Request Failed");
  alert('Etwas ist schief gelaufen');
})
.always(function () {
/* ... */
});
```
In this way, the UX in the dashboard could be increased through error messages even without a large query and error handling on the part of the backend.


# Darkmode implementation
Normally for the light design (Light mode) and the dark mode different CSS classes are used. Depending on the need, either the one CSS class is loaded, which contains the light design, or just the one with the dark design. This assumes that the function was already planned in advance, because a subsequent change of all classes is very labor intensive and takes a lot of time.   
The idea with the darkmode within the BikeRental project came spontaneously. Since it is a very small site with relatively few design elements, a different way of implementation was used.  
First, a checkbox was placed in the main menu. This was designed as a toggle to make the design more appealing. When the toggle is activated, a boolean and local variable is set directly in the browser. If this variable is true, so the toggle is activated, then all color ads are inverted. However, we did not choose an implementation that simply maps the negative color value, but a combination of inverting the colors and a so called HUE rotation by 180 degrees:

```
filter: invert(1) hue-rotate(180deg);  
```

This CSS code uses two filter properties: "invert" and "hue-rotate". The "invert" property reverses the colors of the element that applies it. This means that light colors become darker and dark colors become lighter. The value "1" indicates that all colors should be completely inverted.  
The "hue-rotate" property rotates the hue of the element by a certain angle in the HSL (Hue-Saturation-Lightness) color space. The value "180deg" means that the hue is rotated 180 degrees to the right. This results in colors that were originally red now being green and vice versa.  
The two filter properties are applied in combination, which first inverts the element and then rotates the hue. This results in the element being displayed with inverted colors, but shifted 180 degrees in the HSL color space.  
"Hue" is a term from the HSL color space and refers to the hue of a color. The Hue value of a color indicates where it is in the color spectrum, with 0 degrees corresponding to red and 180 degrees to green.  

The following image shows the difference between pure invert and invert with Hue-rotate(180).

![alt text](/deliverables/huerotate.png)

It can be seen that the colors remain more color tinged. The image retains its blue tint (although slightly darker than before) and the green button remains almost unchanged, while with the pure invert filter it appears red. 

> Note: The dark mode function was removed in the final release due to a small bug. However, it is planned to include it in the project again in the future. 

## CSS Filter Effects 
CSS Filter Effects are method for applying filter effects using the Filter property to elements that correspond to the filters available in SVG. Filter functions include blur, brightness, contrast, drop shadow, grayscale, hue rotation, invert, opacity, sepia, and saturation. These methods are comparatively new. In order for the darkmode to work safely, care was taken beforehand to ensure compatibility of different browsers. The website https://caniuse.com/ offers a good overview of the compatibility of common web browsers.
Overall, all browsers cover 97.98% of all functions. This seems to be sufficient to be able to include the function without hesitation. 
![alt text](/deliverables/css-filter-effects.png)
# Lottie
Lottie is a framework that enables animations created in Adobe After Effects to be rendered to mobile devices and the web. The animations are saved as JSON files called "Lottie files". The advantages of Lottie are that the animations are very smooth and responsive, and they take up little memory because they are rendered on the user's device. 
Lottie is used in the menu. The Lottie file always links to the start page and starts an animation on mouseover.   
In addition, there are Lottie animations on the start page, which fulfills purely optical purposes.  
The Lottie JSON files, as well as the Javascript for the player, are loaded via a CDN. In the future, however, the files will be integrated locally. 

# Bike Rental Page
The Bike.html is next to the homepage the most important page for the customer. Therefore, special attention had to be paid to a user-friendly design here as well. 
On the left side, as already in the wireframe, there is a large picture of the bike. This is currently still statically integrated and is not generated dynamically. This should change in the future. To the right of the image is more information about the bike. The name of the bike and the address are generated dynamically. The price and the description of the bike are currently not yet stored in the database and are also created statically - this will also change in the future. 
Below the description and above the map, depending on the status of the availability of the bike, there is a button to rent the bike, to return it or an information text that the bike is currently rented and cannot be rented. 
![alt text](/deliverables/Bike.html.png)
