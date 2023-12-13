


# multiple arguments
"""1.Positional Arguments: These arguments are passed to the function in the order of their position.
Positional Arguments (स्थानिक आर्ग्यूमेंट्स): इन आर्ग्यूमेंट्स को फ़ंक्शन कोल के दौरान उनके स्थान पर पास किया जाता है।
"""
"""
2.Keyword Arguments: You can pass arguments to the function using their names,
 allowing you to pass arguments out of order.
"""
"""
3.Arbitrary Arguments: You can pass an arbitrary number of arguments to a 
function by using an asterisk (*) followed by an argument name.
"""

# def print_arguments(*args):
#     even = []
#     for i in args:
#         if i % 2==0:
#             even.append(i)
#     return even
#
# x = print_arguments(1,2,3,5,68,7,80,45,2,45,767,6,87,8,87,8,8,22)
# print(x)

# API :- 'application programing interface'

# The API communicates between the client and server.
# server provides limited data to the API client.




"""
Rest_API = rest api disign principle of the rest or representational state transfer artichitectural style
rest api is a standerd , jisme api bnate hai
web API se jab sarver se data lete hai  rest ke hisab se use resource khte h
]
request in rest:-
================
1.URL(Uniform Resource Locator)
2.Method
3.Headers
4.Body
"""

# 1. URL :- URLs became an easy way for the client to tell the server which things it wants to
# interfact, called resources.

"""
2. Method :- the method request tells the server what kind of action the client wants 
the server to take.
the 4 most commonly used or seen in APIs are:-
a REST API would use a GET request to retrieve a record, a POST request to
create one, a PUT request to update a record, and a DELETE request to delete one.
"""


"""
a) GET :- Asks the server to retrive a resource.
b) POST :- Asks the server to Create a new resource.
c) PUT :- Asks the server to edit/update an existing resource.
d) DELETE :- Asks the server to delete a resource.
"""

# 3. Headers :- Headers provide meta-information about a request.
"""http headers are used to pass additional information between the client and server through the request 
and response headers"""

# 4.Body :- The request body contains  data the clients want to send the server.

"""
http :- hyper text transfer protocol

"""


# Response in REST :-

# the server respons with a status code.
# status codes are 3 digit numbers

"""
1xx – Informational Response (These status codes are all about the information received
by the server when a request is made).
2xx – Success (This status code depicts that the request made has been fulfilled by the
server and the expected response has been achieved).
3xx – Redirection (The requested URL is redirected elsewhere).
4xx – Client Errors (This indicates that the page is not  found).
5xx – Server Errors (A request made by the client but the server fails to complete the request).
"""
100 = countinue
200 = ok/success
201 = created
301 = moved permsnently
302 = found
304 = not modified
400 = bad request
401 = unaouthorized
403 = forbidden
404 = not found
405 = method not allowed
413 = request entity to large
414 = request url to large
500 = internal server error
503 = service unavaiable




# What is a URI? A URI — short for “Uniform Resource Identifier” — is a sequence of
# characters that distinguishes one resource from another.

"""
What do you mean by authentication?
In authentication, the user or computer has to prove its identity to the server
or client.Usually, authentication by a server entails the use of a user name and 
password.Other ways to authenticate can be through cards, retina scans, voice 
recognition,and fingerprints.
"""


# access token = pass/personl inform



