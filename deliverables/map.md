# Map
## What is OpenStreetMap?
OpenStreetMap (OSM) is a collaborative project to create a free, editable map of the world. 
The data is open and can be integrated into various applications, including web and mobile applications. 

## Integration
1. Register for an API key from OpenStreetMap.
2. Choose a mapping library that works with OSM data, such as Leaflet or OpenLayers (in the BikeRental project we used Leaflet).
3. Use the chosen library to create a map on your website or application.
4. Use the API key to access OSM data and display it on the map.
5. Customize the appearance and functionality of the map to suit the needs of your project.
6. Use the editing tools provided by the chosen library to allow users to add, edit, or delete data on the map.
7. Regularly download the updated data from OSM to keep the map up-to-date.

It is also important to note that OSM data is contributed by volunteers, so the quality and coverage of data may vary in different areas. 
Additionally, there may be usage limits on the number of API requests that can be made per day.

## GeoJSON
GeoJSON is a format for encoding a variety of geographic data structures, such as points, lines, and polygons, using the JSON (JavaScript Object Notation) data format. 
It is a widely used and open standard for representing geographic data, and is supported by many GIS and web mapping libraries, including OpenStreetMap.

In OpenStreetMap, GeoJSON is often used to export data from the OSM database, and to import data into it. 
For example, in the BikeRental project we use a GeoJSON to import an array of bike data and display it on the map. 

You can also use GeoJSON to add data to OpenStreetMap by uploading a GeoJSON file with the features you want to add. This is useful for adding large amounts of data.

Additionally, GeoJSON can be used to customize the appearance and behavior of OpenStreetMap data in web and mobile applications. 
For example, you can use GeoJSON to style the map, add pop-ups and interactivity, or to filter or group the data in different ways.

Overall, GeoJSON provides a flexible and interoperable way of working with OpenStreetMap data, and is a widely supported and powerful format for representing geographic data.

## How is it used for the BikeRental homepage?
### home.html
```html
<div id="map" style="width: 100%; height: 600px;" class="inverted"></div>
   <section class="map-clean">
      <div class="intro"></div>
      <script>
         var map = L.map('map').setView([0, 0]);
         map.fitBounds([
            [{{ min_y }}, {{ min_x }}],
            [{{ max_y }}, {{ max_x }}]
         ]);

         var tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
         }).addTo(map);

         var Fahrradstellplatz = {{ geo | safe}};

         L.geoJSON(Fahrradstellplatz).bindPopup(function (layer) {
            return '<a href="/bike' + layer.feature.properties.id + '">' + layer.feature.properties.name + "</a>";

         }).addTo(map);

      </script>
```
This code is a section of HTML that is used to display the map on the BikeRental homepage using the Leaflet library. It has the following features:

1. `<div id="map" style="width: 100%; height: 600px;" class="inverted"></div>`: This line creates a div element that will be used to display the map. The id attribute is set to "map" which will be used to reference the div element in the JavaScript code. The style attribute sets the width and height of the div element, and the class attribute is used for CSS styling.
2. `var map = L.map('map').setView([0, 0]);`: This line creates a new map object and sets its initial view to the coordinates (0, 0). It references the "map" div element created in the previous step.
3. `map.fitBounds([[{{ min_y }}, {{ min_x }}], [{{ max_y }}, {{ max_x }}]]);`: This line sets the visible area of the map based on the coordinates passed in the min_x, max_x, min_y, and max_y variables.
4. `var tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' }).addTo(map);`: This line adds a tile layer to the map, using the OpenStreetMap tiles. It sets the maximum zoom level to 19 and adds an attribution link to OpenStreetMap.
5. `var Fahrradstellplatz = {{ geo | safe}};`: This line assigns the GeoJSON object passed in the geo variable to a variable called Fahrradstellplatz. The | safe filter is used to make sure that the GeoJSON is treated as plain text and not HTML.
6. `L.geoJSON(Fahrradstellplatz).bindPopup(function (layer) { return '<a href="/bike' + layer.feature.properties.id + '">' + layer.feature.properties.name + "</a>"; }).addTo(map);`: This line creates a new GeoJSON layer, using the Fahrradstellplatz variable, and binds a popup to it. The popup will display the name of the bike, and the link to the detail page of the bike.

In summary, this code uses the Leaflet library to create a map and display it on the BikeRental homepage. It sets the map's initial view based on passed coordinates, adds a tile layer using OpenStreetMap tiles, and adds a GeoJSON layer, which is used to display the location of bikes on the map with a link to the detail page of the bike.

### app.py
```sh
# Home
# GeoJSON Template: '{"type": "FeatureCollection", "features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[20.0,30.0]},"properties":{"id":"1","name":"Pegasus 500"} },{"type":"Feature","geometry":{"type":"Point","coordinates":[15.0,50.0]},"properties":{"id":"2","name":"Tesla E3000"} },]}'
@app.route("/")
def home():
    #Initialize variables
    geo = '{"type": "FeatureCollection", "features":['
    min_x = 8.212967
    max_x = 8.343430
    min_y = 49.977280
    max_y = 50.021858
    list_x = list()
    list_y = list()
    bikes = get_all(Bike)

    #Loop through bike array
    for current_bike in bikes:
        geo = geo + '{"type":"Feature","geometry":{"type":"Point","coordinates":[' + str(current_bike.x_coordinate) + ',' + str(current_bike.y_coordinate) + ']},"properties":{"id":"' + str(current_bike.id) + '","name":"' + current_bike.name + '"} },'
        list_x.append(current_bike.x_coordinate)
        list_y.append(current_bike.y_coordinate) 
    geo = geo + ']}'

    #Variables to calculate zoom for map startview
    if len(list_x) & len(list_y) != 0:
        min_x=min(list_x)
        min_y=min(list_y)
        max_x=max(list_x)
        max_y=max(list_y)

    return render_template('home.html', geo=geo, min_y=min_y, min_x=min_x, max_y=max_y, max_x=max_x)
```
This code is a Flask web application that defines a route for the home page ("/") and a corresponding function, "home()". The function performs several tasks:

1. `Initialize variables`: The function starts by initializing several variables, including geo, which is a string that will store a GeoJSON object. The other variables, such as min_x, max_x, min_y, and max_y, will be used later to calculate the map's starting view. The list_x and list_y lists will store the x and y coordinates of all bikes respectively.
2. `Get all bikes`: The function then calls the get_all(Bike) function, which is assumed to return an array of all bikes.
3. Loop through bike array: The function then loops through the array of bikes, adding each bike's x and y coordinates and id to the GeoJSON object stored in the geo variable. It also appends the bike's x and y coordinates to the list_x and list_y lists.
4. `Build GeoJSON object`: The function then concatenates the final brackets to the geo variable to make it a valid GeoJSON object
5. `Calculate zoom for map startview`: The function then checks if the list_x and list_y lists have at least one value. If they do, it calculates the minimum and maximum values of both lists and assigns them to the corresponding variables (min_x, max_x, min_y, and max_y).
6. `Render template`: The function then renders a template called home.html and passes the geo, min_x, max_x, min_y, and max_y variables as arguments.

This code is responsible for generating a GeoJSON object from the array of bikes and passing it along with other variables to the home page template. The home page template can then use these variables to display a map of the bikes with an appropriate starting view.

## How is it used for the BikeRental BikeManagement?
```html
<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"></script>
  <script>
    // create a map object
    var map = L.map('map').setView([49.988276672519454,8.228244781494142], 20);
    // add a tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
    }).addTo(map);
    // create a marker and add it to the map
    var marker = L.marker([49.988276672519454,8.228244781494142]).addTo(map);
    // update the text fields when the marker is dragged
    marker.on('drag', function (event) {
      var coords = event.target.getLatLng();
      document.getElementById("latitude").value = coords.lat;
      document.getElementById("longitude").value = coords.lng;
    });
    // prevent the marker from moving outside the map container
    map.on('mouseout', function (event) {
      event.stopPropagation();
    });
    // enable dragging of the marker
    marker.dragging.enable();
  </script>
```
This code is a section of HTML that is used to display a map with a marker that can be dragged by the user on the BikeRental BikeManagement using the Leaflet library. It has the following features:

1. `<div id="map" style="width: 100%; height: 400px;"></div>`: This line creates a div element that will be used to display the map. The id attribute is set to "map" which will be used to reference the div element in the JavaScript code. The style attribute sets the width and height of the div element.
2. `<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"></script>`: This line includes the Leaflet JavaScript library.
3. `var map = L.map('map').setView([49.988276672519454,8.228244781494142], 20);`: This line creates a new map object and sets its initial view to the coordinates of Mainz University of Applied Sciences (49.988276672519454,8.228244781494142) and zoom level 20. It references the "map" div element created in the previous step.
4. `L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors' }).addTo(map);`: This line adds a tile layer to the map, using the OpenStreetMap tiles. It also adds an attribution link to OpenStreetMap.
5. `var marker = L.marker([49.988276672519454,8.228244781494142]).addTo(map);`: This line creates a new marker object and sets its position to the coordinates of Mainz University of Applied Sciences (49.988276672519454,8.228244781494142). It also adds the marker to the map.
6. `marker.on('drag', function (event) { var coords = event.target.getLatLng(); document.getElementById("latitude").value = coords.lat; document.getElementById("longitude").value = coords.lng; });`: This line sets an event listener on the marker that listens for the "drag" event. When the marker is dragged, the function updates the value of the elements with the id "latitude" and "longitude" with the marker's latitude and longitude respectively.
7. `map.on('mouseout', function (event) { event.stopPropagation(); });`: This line sets an event listener on the map that listens for the "mouseout" event. When the mouse moves out of the map container, the function stops the event from propagating.
8. `marker.dragging.enable();`: This line enables the dragging of the marker.

In summary, this code uses the Leaflet library to create a map and display it on the BikeRental BikeManagement with a marker that can be dragged by the user. When the marker is dragged, it updates the latitude and longitude values in the text fields, and also prevents the marker from moving outside the map container. This information makes it easier for the user to add new bikes on the map.
