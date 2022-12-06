# API Documentation
## Authentication
### Session
Use `/login` to login. When using session authentication a CSRF token is required in every request. The token is generated with `{{ csrf_token() }}`. Include the CSRF token in the HTTP header `X-CSRF-Token`. Close the session with `GET /logout`. 

**Add Bike HTTP**
```http
POST /bike-management HTTP/1.1
Content-Type: application/json
X-CSRF-Token: IjJiZDI3MDFjOWU4ZDMwNDViMjJjOTg1ZWFiMjE5ZjIwZGFjOWUzNDAi.Y44IVQ.BuYR-AFs7KJVRvO3HCkyw211xtY
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 52

{"name":"gbike","x_coordinate":21,"y_coordinate":20}
```

**Add Bike cURL**
```sh
## json add
curl -X "POST" "http://localhost/bike-management" \
     -H 'Content-Type: application/json' \
     -H 'X-CSRF-Token: IjJiZDI3MDFjOWU4ZDMwNDViMjJjOTg1ZWFiMjE5ZjIwZGFjOWUzNDAi.Y44IVQ.BuYR-AFs7KJVRvO3HCkyw211xtY' \
     -d $'{
  "name": "gbike",
  "x_coordinate": 21,
  "y_coordinate": 20
}'
```
**Add Bike JavaScript (jQuery)**
```javascript
// json add (POST http://localhost/bike-management)

jQuery.ajax({
    url: "http://localhost/bike-management",
    type: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRF-Token: IjJiZDI3MDFjOWU4ZDMwNDViMjJjOTg1ZWFiMjE5ZjIwZGFjOWUzNDAi.Y44IVQ.BuYR-AFs7KJVRvO3HCkyw211xtY",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "name": "gbike",
        "x_coordinate": 21,
        "y_coordinate": 20
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

### Token
The token can either be included in the header `Authentication-Token` or passed as URL parameter `auth_token`. To get your token use `/login` with the URL parameter `include_auth_token=true`. 

**Get Token HTTP**
```http
POST /login?include_auth_token=true HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 55

{"password":"admin","email":"admin@bikesharing.com"}
```
**Get Token cURL**
```sh
## Login
curl -X "POST" "http://localhost/login?include_auth_token=true" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "email": "admin@bikesharing.com",
  "password": "admin"
}'
```

**Get Token JavaScript (jQuery)**
```javascript
// Login (POST http://localhost/login)

jQuery.ajax({
    url: "http://localhost/login?" + jQuery.param({
        "include_auth_token": "true",
    }),
    type: "POST",
    headers: {
        "Content-Type": "application/json; charset=utf-8",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "email": "admin@bikesharing.com",
        "password": "admin"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

**Response**
```http
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.0
Date: Mon, 05 Dec 2022 19:03:29 GMT
Content-Type: application/json
Content-Length: 260
Vary: Cookie
Set-Cookie: session=.eJwljktOBDEMRO-SNUJ24jjxXKbl-CMQEqDuYYW4OxnNwgtLVfXebznyjOut3O7nT7yU493LrXhLZrHMhtrVEESpCuiKwImCJtF8GuFwCF_VBQhQRh8xjIZhTCdXxsGV6_QJHDux5xi7LBsBmllbH91dTT3FefHG0qyJXrbIzxXn00bbFKQEWiY0UFZM06k8RGSiwU7bdeZx__qIz50HJ1r9gY9t7WJrKKSia1VsIC0Xa_e6e3kdZrtyxf35fauWG_KAug_k9cEDpL9_K8RTgA.Y45AgQ.a0looKCu-nBzvE8th2RdnwAp6Wo; HttpOnly; Path=/
Connection: close

{"meta":{"code":200},"response":{"csrf_token":"IjBkNDRiNWRhNjFlNDI5ZDljYjdhMGZhMWRhMmExMzA5M2ZiNmE1ZDIi.Y45AgQ.G-Z0I-L1YwtOw0cuvVr2n7uxjJk","user":{"authentication_token":"WyJhMzg5MTRmMDRiYzk0NzE5YmU4Y2E4YTY3OTk5ODFjMCJd.Y45AgQ.Fi6Fk8iep5moYN3P9E2G8YLd83Q"}}}
```

**Add Bike URL parameter HTTP**
```http
POST /bike-management?auth_token=WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU HTTP/1.1
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 52

{"name":"gbike","x_coordinate":21,"y_coordinate":20}
```

**Add Bike header HTTP**
```http
POST /bike-management HTTP/1.1
Content-Type: application/json
Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 52

{"name":"gbike","x_coordinate":21,"y_coordinate":20}
```

**Add Bike URL parameter cURL**
```sh
## json add
curl -X "POST" "http://localhost/bike-management?auth_token=WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU" \
     -H 'Content-Type: application/json' \
     -d $'{
  "name": "gbike",
  "x_coordinate": 21,
  "y_coordinate": 20
}'
```
**Add Bike header cURL**
```sh
## json add
curl -X "POST" "http://localhost/bike-management" \
     -H 'Content-Type: application/json' \
     -H 'Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU' \
     -d $'{
  "name": "gbike",
  "x_coordinate": 21,
  "y_coordinate": 20
}'
```
**Add Bike URL parameter JavaScript (jQuery)**
```javascript
// json add (POST http://localhost/bike-management)

jQuery.ajax({
    url: "http://localhost/bike-management?" + jQuery.param({
        "auth_token": "WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU",
    }),
    type: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "name": "gbike",
        "x_coordinate": 21,
        "y_coordinate": 20
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```
**Add Bike header JavaScript (jQuery)**
```javascript
// json add (POST http://localhost/bike-management)

jQuery.ajax({
    url: "http://localhost/bike-management",
    type: "POST",
    headers: {
        "Content-Type": "application/json",
        "Authentication-Token": "WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "name": "gbike",
        "x_coordinate": 21,
        "y_coordinate": 20
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

## User
### Register
**HTTP**
```http
POST /register HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 40

{"email":"t@l.co","password":"password"}
```
**cURL**
```sh
## Request Duplicate
curl -X "POST" "http://localhost/register" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "email": "t@l.co",
  "password": "password"
}'
```
**JavaScript (jQuery)**
```javascript
// Request Duplicate (POST http://localhost/register)

jQuery.ajax({
    url: "http://localhost/register",
    type: "POST",
    headers: {
        "Content-Type": "application/json; charset=utf-8",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "email": "t@l.co",
        "password": "password"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

### Change Password
**HTTP**
```http
POST /change?auth_token=WyIzNjk2YjczZTg2YWE0ZmIzODI0YzBhNmVkYzQ2Zjc3YiJd.Y44_wA.3WWVoGbyRA6IB1VH7Oj3-mHTHC4 HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 83

{"password":"password","new_password":"admin123","new_password_confirm":"admin123"}
```
**cURL**
```sh
## change
curl -X "POST" "http://localhost/change?auth_token=WyIzNjk2YjczZTg2YWE0ZmIzODI0YzBhNmVkYzQ2Zjc3YiJd.Y44_wA.3WWVoGbyRA6IB1VH7Oj3-mHTHC4" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "new_password": "admin123",
  "new_password_confirm": "admin123",
  "password": "password"
}'
```
**JavaScript (jQuery)**
```javascript
// change (POST http://localhost/change)

jQuery.ajax({
    url: "http://localhost/change?" + jQuery.param({
        "auth_token": "WyIzNjk2YjczZTg2YWE0ZmIzODI0YzBhNmVkYzQ2Zjc3YiJd.Y44_wA.3WWVoGbyRA6IB1VH7Oj3-mHTHC4",
    }),
    type: "POST",
    headers: {
        "Content-Type": "application/json; charset=utf-8",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "new_password": "admin123",
        "new_password_confirm": "admin123",
        "password": "password"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

### Delete
**HTTP**
```http
DELETE /user-management HTTP/1.1
Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 15

{"user_id":"3"}
```
**cURL**
```sh
## delete
curl -X "DELETE" "http://localhost/user-management" \
     -H 'Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU' \
     -H 'Content-Type: application/json' \
     -d $'{
  "user_id": "3"
}'
```
**JavaScript (jQuery)**
```javascript
// delete (DELETE http://localhost/user-management)

jQuery.ajax({
    url: "http://localhost/user-management",
    type: "DELETE",
    headers: {
        "Authentication-Token": "WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU",
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "user_id": "3"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

### Add Role
**HTTP**
```http
PUT /user-management HTTP/1.1
Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 48

{"user_id":4,"role_id":1,"operation":"add_role"}
```
**cURL**
```sh
## add role
curl -X "PUT" "http://localhost/user-management" \
     -H 'Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU' \
     -H 'Content-Type: application/json' \
     -d $'{
  "user_id": 4,
  "role_id": 1,
  "operation": "add_role"
}'
```
**JavaScript (jQuery)**
```javascript
// add role (PUT http://localhost/user-management)

jQuery.ajax({
    url: "http://localhost/user-management",
    type: "PUT",
    headers: {
        "Authentication-Token": "WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU",
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "user_id": 4,
        "role_id": 1,
        "operation": "add_role"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```

### Remove Role
**HTTP**
```http
PUT /user-management HTTP/1.1
Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 34

{"id":3,"operation":"remove_role"}
```
**cURL**
```sh
## remove role
curl -X "PUT" "http://localhost/user-management" \
     -H 'Authentication-Token: WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU' \
     -H 'Content-Type: application/json' \
     -d $'{
  "id": 3,
  "operation": "remove_role"
}'
```
**JavaScript (jQuery)**
```javascript
// remove role (PUT http://localhost/user-management)

jQuery.ajax({
    url: "http://localhost/user-management",
    type: "PUT",
    headers: {
        "Authentication-Token": "WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU",
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "id": 3,
        "operation": "remove_role"
    })
})
.done(function(data, textStatus, jqXHR) {
    console.log("HTTP Request Succeeded: " + jqXHR.status);
    console.log(data);
})
.fail(function(jqXHR, textStatus, errorThrown) {
    console.log("HTTP Request Failed");
})
.always(function() {
    /* ... */
});
```
