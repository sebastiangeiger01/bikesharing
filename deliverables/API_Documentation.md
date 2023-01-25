# API Documentation

This REST API accepts the `Content-Type: application/json`. 

## Authentication
<details>
<summary><h3>Session</summary>

Use `/login` to login. When using session authentication a CSRF token is required in every request. The token is generated with `{{ csrf_token() }}`. Include the CSRF token in the HTTP header `X-CSRF-Token`. Close the session with `GET /logout`.

Here are some examples on how to add a bike using session authentication:

**Add Bike HTTP**
```http
POST /bike-management HTTP/1.1
X-CSRF-Token: Ijc4ZjFlZTI2NGYyNGY1N2JkMGJkMDJhMzk4ZTliZDM3YTA2NjhlOTUi.Y5GW6A.N9Yofk_vd3zVh2UKqqLjkSlwjQc
Content-Type: application/json; charset=utf-8
Cookie: session=.eJwljklqBDEMRe_idQiSB8nqyxSyBhICSajqXjW5ewwNWnzB-8OzHHnG9VFu9_MRb-X49HIr3pJILLOhDjUE0V4FdEXgREGTaD6tIzuEr-oCHVB4cLB1Nozp3ZWQqVKdPoFiEzuOcMgyDtDM2gYPdzX1FKdFu7bPmuhlD3lccb7WaJuCPaEvk84oK6bpVGIRmWiwabvOPO4_X_G9eZ6JEZV61p6Dl8O-qk1myPLGCkRbju3L6zDblivur-9XtdyQGPoc3OidgGFC_fsHFoJTIg.Y5GW6A.b4PVLItp7hTptzQZ2Uqd0_SAV3U
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 52

{"name":"gbike","x_coordinate":21,"y_coordinate":20}
```

**Add Bike cURL**
```sh
## json add
curl -X "POST" "/bike-management" \
     -H 'X-CSRF-Token: Ijc4ZjFlZTI2NGYyNGY1N2JkMGJkMDJhMzk4ZTliZDM3YTA2NjhlOTUi.Y5GW6A.N9Yofk_vd3zVh2UKqqLjkSlwjQc' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -H 'Cookie: session=.eJwljklqBDEMRe_idQiSB8nqyxSyBhICSajqXjW5ewwNWnzB-8OzHHnG9VFu9_MRb-X49HIr3pJILLOhDjUE0V4FdEXgREGTaD6tIzuEr-oCHVB4cLB1Nozp3ZWQqVKdPoFiEzuOcMgyDtDM2gYPdzX1FKdFu7bPmuhlD3lccb7WaJuCPaEvk84oK6bpVGIRmWiwabvOPO4_X_G9eZ6JEZV61p6Dl8O-qk1myPLGCkRbju3L6zDblivur-9XtdyQGPoc3OidgGFC_fsHFoJTIg.Y5GW6A.b4PVLItp7hTptzQZ2Uqd0_SAV3U' \
     -d $'{
  "name": "gbike",
  "x_coordinate": 21,
  "y_coordinate": 20
}'
```
**Add Bike JavaScript (jQuery)**
```javascript
// json add (POST /bike-management)

jQuery.ajax({
    url: "/bike-management",
    type: "POST",
    headers: {
        "X-CSRF-Token": "Ijc4ZjFlZTI2NGYyNGY1N2JkMGJkMDJhMzk4ZTliZDM3YTA2NjhlOTUi.Y5GW6A.N9Yofk_vd3zVh2UKqqLjkSlwjQc",
        "Content-Type": "application/json; charset=utf-8",
        "Cookie": "session=.eJwljklqBDEMRe_idQiSB8nqyxSyBhICSajqXjW5ewwNWnzB-8OzHHnG9VFu9_MRb-X49HIr3pJILLOhDjUE0V4FdEXgREGTaD6tIzuEr-oCHVB4cLB1Nozp3ZWQqVKdPoFiEzuOcMgyDtDM2gYPdzX1FKdFu7bPmuhlD3lccb7WaJuCPaEvk84oK6bpVGIRmWiwabvOPO4_X_G9eZ6JEZV61p6Dl8O-qk1myPLGCkRbju3L6zDblivur-9XtdyQGPoc3OidgGFC_fsHFoJTIg.Y5GW6A.b4PVLItp7hTptzQZ2Uqd0_SAV3U",
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
</details>

<details>
<summary><h3>Token</summary>
The token can either be included in the header `Authentication-Token` or passed as URL parameter `auth_token`. 

To get your token use `/login` with the URL parameter `include_auth_token=true`. 

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
curl -X "POST" "/login?include_auth_token=true" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "email": "admin@bikesharing.com",
  "password": "admin"
}'
```

**Get Token JavaScript (jQuery)**
```javascript
// Login (POST /login)

jQuery.ajax({
    url: "/login?" + jQuery.param({
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

The response has an attribute `authentication_token` in its body:

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

The following examples demonstrate the difference between transmitting the authentication token as URL parameter or in the header:

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
curl -X "POST" "/bike-management?auth_token=WyI0ZmFhOTQ1MDY2ZWE0NjNmOGI4NzA1NjE1YmY2MDJmZCJd.Y4zrmw.gzQE1prXoNBEiFxDzaagGJ3UKtU" \
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
curl -X "POST" "/bike-management" \
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
// json add (POST /bike-management)

jQuery.ajax({
    url: "/bike-management?" + jQuery.param({
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
// json add (POST /bike-management)

jQuery.ajax({
    url: "/bike-management",
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
</details>

## User
<details>
<summary><h3>Register</summary>

| Method | URL | Requirements |
|---|---|---|
| POST | `/register` | None |

**Body**
```json
{
  "email": "t@l.co",
  "password": "password"
}
```

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
curl -X "POST" "/register" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "email": "t@l.co",
  "password": "password"
}'
```
**JavaScript (jQuery)**
```javascript
// Request Duplicate (POST /register)

jQuery.ajax({
    url: "/register",
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
</details>

<details>
<summary><h3>Change Password</summary>

| Method | URL | Requirements |
|---|---|---|
| POST | `/change` | authentication |

**Body**
```json
{
  "password": "password",
  "new_password": "admin123",
  "new_password_confirm": "admin123"
}
```

**HTTP**
```http
POST /change HTTP/1.1
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
curl -X "POST" "/change" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "new_password": "admin123",
  "new_password_confirm": "admin123",
  "password": "password"
}'
```
**JavaScript (jQuery)**
```javascript
// change (POST /change)

jQuery.ajax({
    url: "/change",
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
</details>

<details>
<summary><h3>Delete</summary>

| Method | URL | Requirements |
|---|---|---|
| DELETE | `/user-management` | Role: user-manager |

**Body**
```json
{
  "user_id": "3"
}
```

**HTTP**
```http
DELETE /user-management HTTP/1.1
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
curl -X "DELETE" "/user-management" \
     -H 'Content-Type: application/json' \
     -d $'{
  "user_id": "3"
}'
```
**JavaScript (jQuery)**
```javascript
// delete (DELETE /user-management)

jQuery.ajax({
    url: "/user-management",
    type: "DELETE",
    headers: {
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
</details>

<details>
<summary><h3>Add Role</summary>

| Method | URL | Requirements |
|---|---|---|
| PUT | `/user-management` | Role: user-manager |

**Body**
```json
{
  "user_id": 4,
  "role_id": 1,
  "operation": "add_role"
}
```

**HTTP**
```http
PUT /user-management HTTP/1.1
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
curl -X "PUT" "/user-management" \
     -H 'Content-Type: application/json' \
     -d $'{
  "user_id": 4,
  "role_id": 1,
  "operation": "add_role"
}'
```
**JavaScript (jQuery)**
```javascript
// add role (PUT /user-management)

jQuery.ajax({
    url: "/user-management",
    type: "PUT",
    headers: {
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
</details>

<details>
<summary><h3>Remove Role</summary>

| Method | URL | Requirements |
|---|---|---|
| PUT | `/user-management` | Role: user-manager |

**Body**
```json
{
  "user_id": 3,
  "role_id": 1,
  "operation": "remove_role"
}
```

**HTTP**
```http
PUT /user-management HTTP/1.1
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.1.0) GCDHTTPRequest
Content-Length: 51

{"user_id":3,"role_id":1,"operation":"remove_role"}
```
**cURL**
```sh
## remove role
curl -X "PUT" "/user-management" \
     -H 'Content-Type: application/json' \
     -d $'{
  "user_id": 3,
  "role_id": 1,
  "operation": "remove_role"
}'
```
**JavaScript (jQuery)**
```javascript
// remove role (PUT /user-management)

jQuery.ajax({
    url: "/user-management",
    type: "PUT",
    headers: {
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "user_id": 3,
        "role_id": 1,
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
</details>

<details>
<summary><h3>Get all users</summary>

| Method | URL | Requirements |
|---|---|---|
| GET | `/allusers` | Role: user-manager |

**HTTP**
```http
GET /allusers HTTP/1.1
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.1.0) GCDHTTPRequest
```
**cURL**
```sh
## get_all(User)
curl "/allusers"
```
**JavaScript (jQuery)**
```javascript
// get_all(User) (GET /allusers)

jQuery.ajax({
    url: "/allusers",
    type: "GET",
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
</details>

## Bike
<details>
<summary><h3>Add Bike</summary>

| Method | URL | Requirements |
|---|---|---|
| POST | `/bike-management` | Role: bike-manager |

**Body**
```json
{
  "name": "gbike",
  "x_coordinate": 21,
  "y_coordinate": 20
}
```

**HTTP**
```http
POST /bike-management HTTP/1.1
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 52

{"name":"gbike","x_coordinate":21,"y_coordinate":20}
```
**cURL**
```sh
## json add
curl -X "POST" "/bike-management" \
     -H 'Content-Type: application/json' \
     -d $'{
  "name": "gbike",
  "x_coordinate": 21,
  "y_coordinate": 20
}'
```
**JavaScript (jQuery)**
```javascript
// json add (POST /bike-management)

jQuery.ajax({
    url: "/bike-management",
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
</details>

<details>
<summary><h3>Delete Bike</summary>

| Method | URL | Requirements |
|---|---|---|
| DELETE | `/bike-management` | Role: bike-manager |

**Body**
```json
{
  "id": 3
}
```

**HTTP**
```http
DELETE /bike-management HTTP/1.1
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 8

{"id":3}
```
**cURL**
```sh
## json delete
curl -X "DELETE" "/bike-management" \
     -H 'Content-Type: application/json' \
     -d $'{
  "id": 3
}'
```
**JavaScript (jQuery)**
```javascript
// json delete (DELETE /bike-management)

jQuery.ajax({
    url: "/bike-management",
    type: "DELETE",
    headers: {
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "id": 3
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
</details>

<details>
<summary><h3>Edit Bike</summary>

| Method | URL | Requirements |
|---|---|---|
| PUT | `/bike-management` | Role: bike-manager |

**Body**
```json
{
  "name": "Cabik",
  "x_coordinate": 20,
  "y_coordinate": 20,
  "id": 1
}
```

**HTTP**
```http
PUT /bike-management HTTP/1.1
Content-Type: application/json
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 59

{"name":"Cabik","x_coordinate":20,"y_coordinate":20,"id":1}
```
**cURL**
```sh
## json edit
curl -X "PUT" "/bike-management" \
     -H 'Content-Type: application/json' \
     -d $'{
  "id": 1,
  "name": "Cabik",
  "x_coordinate": 20,
  "y_coordinate": 20
}'
```
**JavaScript (jQuery)**
```javascript
// json edit (PUT /bike-management)

jQuery.ajax({
    url: "/bike-management",
    type: "PUT",
    headers: {
        "Content-Type": "application/json",
    },
    contentType: "application/json",
    data: JSON.stringify({
        "id": 1,
        "name": "Cabik",
        "x_coordinate": 20,
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
</details>

<details>
<summary><h3>Get all bikes</summary>

| Method | URL | Requirements |
|---|---|---|
| GET | `/allbikes` | Role: bike-manager |

**HTTP**
```http
GET /allbikes HTTP/1.1
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.1.0) GCDHTTPRequest
```
**cURL**
```sh
## get_all(Bike)
curl "/allbikes"
```
**JavaScript (jQuery)**
```javascript
// get_all(Bike) (GET /allusers)

jQuery.ajax({
    url: "/allbikes",
    type: "GET",
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
</details>

## Ride
<details>
<summary><h3>Start Ride</summary>

| Method | URL | Requirements |
|---|---|---|
| POST | `/bike<id>` | authenticated |

**HTTP**
```http
POST /bike1 HTTP/1.1
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 0
```
**cURL**
```sh
## start
curl -X "POST" "/bike1"
```
**JavaScript (jQuery)**
```javascript
// start (POST /bike1)

jQuery.ajax({
    url: "/bike1",
    type: "POST",
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
</details>

<details>
<summary><h3>End Ride</summary>

| Method | URL | Requirements |
|---|---|---|
| PUT | `/bike<id>` | authenticated |

**HTTP**
```http
PUT /bike1 HTTP/1.1
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.0.1) GCDHTTPRequest
Content-Length: 0
```
**cURL**
```sh
## end
curl -X "PUT" "/bike1" 
```
**JavaScript (jQuery)**
```javascript
// end (PUT /bike1)

jQuery.ajax({
    url: "/bike1",
    type: "PUT",
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
</details>

<details>
<summary><h3>Get all rides</summary>

| Method | URL | Requirements |
|---|---|---|
| GET | `/allrides` | Role: user-manager, bike-manager |

**HTTP**
```http
GET /allrides HTTP/1.1
Host: localhost
Connection: close
User-Agent: RapidAPI/4.0.0 (Macintosh; OS X/13.1.0) GCDHTTPRequest
```
**cURL**
```sh
## get_all(Rides)
curl "/allrides"
```
**JavaScript (jQuery)**
```javascript
// get_all(Rides) (GET /allrides)

jQuery.ajax({
    url: "/allrides",
    type: "GET",
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
</details>
