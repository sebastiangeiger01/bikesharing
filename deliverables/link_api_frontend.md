#API integration of the backend
After the basic design was ready, the interface implementation of the backend was awaited. The good documentation of the API ensured an easy implementation of the desired functions. 

By directly embedded Javascript the functions of the website were extended so that the frontend and the backend harmonize.

The code was written directly in <script> tags of the html file, but this makes the code look a little less messy in the frontend. In the future, the plan is to offload the code into custom javascript and then include it.

##API customisation
The API with the function for renting a bike provided for a time to be sent in the request. However, after close analysis, it was determined that users would theoretically be able to intercept the code before it was sent, manipulate it, and thus manipulate the time of the rental and return. This is because the Javascript code is stored and executed locally, and is not checked on the server side.
After the tip was passed to the backend, the timestamps were set in the backend and the API changed as follows:


```javascript
@@ -910,13 +896,6 @@ curl -X "POST" "http://localhost/bike1" \
@@ -910,13 +896,6 @@ curl -X "POST" "http://localhost/bike1" \
jQuery.ajax({
    url: "http://localhost/bike1",
    type: "POST",
    headers: {
        "Content-Type": "application/json; charset=utf-8",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "start_time": "2004-10-19 10:23:54"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
'''
