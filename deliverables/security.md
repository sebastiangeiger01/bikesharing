# Security
CSRF tokens, session-based authentication, and token-based authentication are all important security measures that are being used to protect this web application from unauthorized actions and ensure that only authenticated users can access sensitive information.

CSRF tokens and session-based authentication are used in combination to secure the webapp. Token-based authentication is required for stateless authentication via the REST-API. 

[How to use the API](/deliverables/API_Documentation.md)

## CSRF Tokens
CSRF (Cross-Site Request Forgery) tokens are a security measure used to prevent unauthorized actions on a web application. They are used to protect against a specific type of attack known as a CSRF attack.

A CSRF attack occurs when a malicious website or attacker tricks a user into performing an unwanted action on a legitimate website. For example, imagine a user is logged into their bank account on a website and then visits a malicious website. The malicious website could then use JavaScript to automatically submit a request to the bank website to transfer money without the user's knowledge or consent.

To prevent this type of attack, web developers use CSRF tokens. A CSRF token is a unique, unpredictable value that is generated by the server and sent to the user's browser when they visit a web page. The browser then sends this token back to the server with every subsequent request, such as a form submission. The server then verifies that the token received in the request is the same as the one it issued. If the tokens do not match, the request is rejected, preventing unauthorized actions from being performed on the user's behalf.

There are different ways to implement CSRF token, one of them is to include it as a hidden field in forms.

Additionally, CSRF tokens can be included in HTTP headers, such as the X-CSRF-TOKEN header, which is added by the server and then checked by the browser on subsequent requests.

It's important to note that the goal of CSRF tokens is to ensure that requests are only accepted if they originate from the same domain as the website, but it does not prevent all kind of attacks, and it should be combined with other security measures, such as same-site cookies, and CORS (Cross-Origin Resource Sharing) headers.

In summary, CSRF tokens are a security measure that helps protect web applications from unauthorized actions by ensuring that requests are only accepted if they originate from the same domain. They are generated by the server and sent to the user's browser, and then sent back to the server with every subsequent request to verify the authenticity of the request.

## Session-Based Authentication
Session-based authentication is a method of authenticating users on a web application. It uses a session ID to identify a user and determine if they are authenticated. When a user logs in, the server generates a unique session ID and associates it with the user. The session ID is then sent to the user's browser as a cookie.

On subsequent requests, the browser sends the session ID back to the server as a cookie. The server then looks up the session ID in a session store and if it finds a match, it knows that the user is authenticated.

Session-based authentication can be used to track a user's activity across multiple requests, allowing the server to maintain information about the user's session, such as the items in their shopping cart, the pages they have visited, and their preferred language.

One of the benefits of session-based authentication is that it allows for easy integration with existing web frameworks. Most web frameworks include built-in support for session-based authentication, and it can be easily added to an existing application.

However, there are some drawbacks to session-based authentication. One of them is that it requires the server to maintain state, which can be problematic in a distributed environment. Additionally, it is not very secure if the session ID is stolen or leaked, an attacker could use the session ID to impersonate the user.

In summary, session-based authentication is a method of authenticating users on a web application that uses a session ID to identify a user and determine if they are authenticated. It allows for easy integration with existing web frameworks, but it also requires the server to maintain state, which can be problematic in a distributed environment. Additionally, it is not very secure if the session ID is stolen or leaked. It is recommended to use it in conjunction with other security measures such as SSL/TLS and regenerating the session ID after a user logs in or out.

## Token-Based Authentication
Token-based authentication is a method of authenticating users on a web application, particularly when the application is providing a REST-API. It uses a token, which is a unique, cryptographically-signed value, to identify a user and determine if they are authenticated.

When a user logs in, the server generates a token and sends it to the user. The token is stored on the client-side.

On subsequent requests, the client sends the token back to the server in the request headers. The server then verifies the token and if it is valid, it allows the request to proceed, otherwise it returns an error.

One of the main benefits of token-based authentication is that it allows for stateless authentication, as the server does not need to maintain any information about the user's session. This makes it more scalable and easier to implement in a distributed environment. Additionally, token-based authentication can be used to authenticate users across different devices and platforms.

Token-based authentication has some security considerations, the tokens must be kept private and securely stored on the client-side. Additionally, they must be cryptographically signed to prevent tampering. Tokens also have an expiration date, which means that they will become invalid after a certain period of time and the user will have to log in again.

In summary, token-based authentication is a method of authenticating users on a web application, particularly when the application is providing a REST-API. It uses a token, which is a unique, cryptographically-signed value, to identify a user and determine if they are authenticated. The token is generated by the server and sent to the client. On subsequent requests, the client sends the token back to the server in the request headers for authentication. This method allows for stateless authentication, as the server does not need to maintain any information about the user's session, making it more scalable and easier to implement in a distributed environment. However, it requires to keep the tokens private and securely stored on the client-side, and cryptographically signed to prevent tampering.
