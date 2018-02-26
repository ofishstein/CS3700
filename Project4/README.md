Oliver Fishstein and Jacob Taylor
CS3700 - Networks and Distributed Systems
Project 4

High Level Approach
----
We simply started by stubbing out the methods we would need and creating a crawler class. Then, it was a matter of adding the ability to log into Fakebook. Once logged in, we had to crawl all the pages and add the appropriate queueing mechanisms in order to do that. Finally, we had to handle edge cases- the various response codes, chunking, socket timeout, etc. Finally, once the crawling was completely working, we needed only to add the logic for finding the secret flags.

Crawler
----

init                  -> Set credentials and initialize data structures

initSocket            -> Create and open the socket for communicating with Fakebook

start                 -> Inits the socket, logs in, and begins crawling

login                 -> Handles logging in

crawl                 -> Handles the crawling loop

parseUrlPaths         -> Parses URLs on the page into the queue

parseSecretFlags      -> Parses secret flags on the page into a list

areAllFlagsFound      -> Determines if all five flags have been found and exits the program

sendGetRequest        -> Send a GET request, handle chunking and empty responses, and return the response

buildGetRequest       -> Builds the GET request that will be sent

sendLoginPostRequest  -> Sends the POST request for logging in

buildLoginPostRequest -> Builds the POST request for logging in

setCookies            -> Parse result of login request for a cookie and set it for future requests

getResponseCode       -> Determines the response code of each response

handleRedirect        -> Handles redirects for a 301 response code

Challenges
----

We had difficulty in the initial stages of creating the login request and properly handling the cookie, since at this point there was little structure behind our program. Once logging in began working, it next became a question of how to handle each response code. This raised a few edge cases, such as a socket becoming invalid (response of 0) and needing to reinitialize. The only problem left at this point was chunking, which we were able to implement in a straightforward way after some thought. Finally, the crawler was running completely correctly and we needed only obtain the secret flags.

Testing
----

In order to test, we used a bunch of different log messages throughout the program in order to verify it was functioning properly. Additionally, we added exceptions, which allowed us to easily determine edge cases that needed to be handled to avoid said exceptions. The final test was running the crawler beginning-to-end, which showed that it was capable of crawling the entirety of Fakebook and able to locate all the flags.
