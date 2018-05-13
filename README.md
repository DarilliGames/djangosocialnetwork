## Django Social Network

###  About

#### Author

Stephen Moody

Submittion for Project 3 for Code Institute

Live Project Available [here](https://gbrand-network.herokuapp.com) or at:

https://gbrand-network.herokuapp.com

Git-Hub Available [here](https://github.com/DarilliGames/djangosocialnetwork) or at:

https://github.com/DarilliGames/djangosocialnetwork

#### Project Contents


| Folder | Condition | Comments |
|-------|----|--------|
| djangonetwork | Working | The base file the for project including setting, urls, etc. |
| accounts | Working|  User Accounts folder with Profile settings and game character settings |
| chatroom | Working|  Provides functionality to send instant messages in both a chatroom and private message capasity |
| follow | Working | Allows users to follow other users.  Currently no other additional functionality |
| games | Working | Allows both Games and Publishers to added to the website |
| home | Working | Includes pages not dedicated to other folders |
| mbox | Working | Provides an outdated inbox system (Sending Messages is not supported for non-admin users) |
| premium | Working | Allows Users to Update their accounts to premium static.  This allows users to be found easier and get promoted on both the front page and prioritised when searched |
| review | Working | Provieds Reviews Possible for Games |
| search | Working | A number of search tools - Search for a game, user, etc.  Characters are search for by game and attributes associated by that game. |
| stream | Working | Allows Live streaming via Twitch.tv for users. |

#### Industry Insight 

Video Games is the fastest growing form of Media Industry,  in 2013 the Gaming Industry generated $70.4 billion ([^1]) vs Worldwide Films at only $35.9 billion([^2]).

In addition, the numbers of professional Gamers has also dramatically increased.  One reason is both through websites like Twitch.tv, Youtube and more catagorising Gamers and their videos as entertainment.  The other reason is the Prize Pool's for Competitive Tournements has also increased.

#### Features

##### Accounts

The Accounts App offers a number of features from Registration, Login and Logout, Accounts deleting.
Each account has the ability to be customised with a profile picture, basic information and a "Main Character" (more on this later).

Each User can create a number of Characters.  These characters are their in game avatars and accounts with relative details for that specific game.  The basic Character has a set number of variables (eg. name, what game the character is in, what rank they are).  For different games though the values of this information can vary dramatically, in one game being "Rank 1" means you are the best in the world;  while in another this rank could be the sign of a brand new player.  A way around this was created and functional, more details in "Difficulties" Section.
In addition to these features, depending on the game specific attributes may be desired for searching purposes (eg. team, role, position, etc.).  I call my solution "Variable Characteristics", these possible characteristics are related to each Game but do not within the Game Model.

##### Games

A core part of the functionality is the Games Model.  Games have two images, a Thumbnail and Tall Box Art.  Games also can be reviewed, details added and more.

##### Review

Games can be reviewed through models on the game profile game.

##### Streams

Live Streaming is a huge part of the modern gaming industry.  Players Stream to get views, followers, donations and fees collected by streaming platforms for subscriptions to the players.  For Twitch.tv viewers pay €5 per month for additional perks.

For Game Publishers, Players streaming their game is a very valid for of advertising and player retension which is vital for the many publishers who are moving to subscription and/or micro-transaction based service.

Being such an important part of the industry, I knew I had to include it into the website.  The website has two forms of Stream, which I have termed "Dedicated" and "User Submitted".

Dedicated Streams are created and are visible all the time and I have set these up while there are no active users.  If released, these would service event based streams, featured or premium streams.

User Submitted are streams created by players once their user profile is completed and their Twitch.tv accounts are set up.

##### Search

A core for the website and a custom search funciton was required as again the "Variable Characteristics" cropped up.  In order for a character to be searched, a specific game must be selected first.  After a game is selected, it populates the search page with the possible attributes which may be selected as individual dropdown boxes, it then populates these dropdown boxes with the possible variables assigned to these attributes.

The search function will search for a character based off the Game, Name of the Character, Rank and any number of possible attributes.  Only if a variable charactistic is selected, only then it will be searched. 

##### Messaging

Messaging between users is available in two forms.  Mailboxes and instant messaging is available.  The Website also offers a chatroom, which any member can join.

This chatrom is made possible through AJAX, but in future versions a would be introduced.


##### Notifications

Unread messages from either your Mailbox or from any instant messages show up as a notification in the Nav-Bar.

##### Following

Following shows support for another user.  Currently, following a user offers no notifications, other than allowing you to find your favourite players easier.

#### Website Successes

When setting out to build the website, 4 key aspects were identified. 

The first goal was to allow Video Game Players to find eachother.  Not only that, the players should be able to narrow down their prefered playing partner.  

The second goal was to find a way for the players to communicate.  Originally, I had thought a mail box system would be sufficient, but when the possibility to change this to an instant messaging system was available, it was quite clear this option was much more desired.

The third goal was to make the website financially viable.  A subscription model was chosen with the basis that serious players would receive more offers from other gamers as they would be promoted in searches though additional ideas have also been generated.

The final goal was to encourage Streamers to the website.  Streamers could help generate the numbers of Users joining the website and trigger the growth.

| Goal | Pass | Notes |
|-----|-----|-----|
| Finding Other Gamers | Yes | Through the search function on the website finding similarly skilled or desired players is possible.  The Game Model(Class) is adaptable allowing for new games to be rapidly added to the database. |
| Contacting Players | Yes | Finding other gamers is pointless if you can not connect with eachother.  The Live Chat System allows users to discuss when they are available to play together. |
| Payments | Yes | The ultimate goal of any website is to become financially viable.  The website if successfully launched would allow a number of revenue generating areas.  Subscriptions would make a section of this but between additional revenue could be generated through targeted advertising based on similar games previously played. |
| Streamer Appeal | Yes | As streamers could provide a lot of attention and help increase number of users on the website.  In turn, the website will allow co-operative advertising for the streamers as users will be able to find them.  |

#### Difficulties Present

##### Lack of Filter

Unfortunately, the basic Django Framework's filtering system does not allow for a core part of our search function.  That is the prementioned "Variable Characteristic".
In order the get around this difficulty I was required rearrange customised search functionality.

Unfortunately, this was a huge time investment but is crucial to the overall functionality of the website, now with a working version I am extremely proud of the outcome.

##### Live Chat

Instant Messaging was something I really thought the website could use to improve the user experience.  Originally I had thought of using a Mailling System but for users looking to find other players to play with would give up on waiting for replies.

I first set out to build and Instant Messaging system, I found a very rough guide on AJAX and PHP.  I figured give it a read and see if I could understand any of it - I was unsuccessful for the PHP part but I could salvage some of the AJAX.

Eventually, I had a very bugged version.  Which would load once and stop.  Then would do nothing.  About three days later I had a open chatroom with a live chat with AJAX polling every 3 seconds.  Through another long stage of trial and error I finally got a Private chat working.


#### Bug Tracker

##### Known Bugs

1) Django Messages - For some reason the inbuilt Django Messages do not always show.  This was mentioned before during Lectures with the Code Institute.
2) Character Search - As all attributes are generated on the search form, Search does not show characters without attributes.  Character must be updated before it can be found by search function.
3) Stream Update When Offline - The Twitch iframes do NOT update when the stream goes offline.  This in turn means that Users must click the "Go Offline" button to remove their Stream from the stream section.

##### Resolved Bugs

1) Subscriptions Not Updating - Error: User Profiles while being marked as "Premium", did not correctly get displayed when searched. Solved.
2) Updating "Playing Game" (Used in setting up the streaming functions) - Error: Form did not correctly Save the Game, leading to Stream and Profile errors. Solved.
3) Images Not Loading - Error: Images for profile pictures were not being saved. Solved:  Images were being saved but the URL to get the images was going to the wrong AWS Folder.
4) Character Updates Giving Incorrect Options - Error: Attribute Values were allowing a user to assign attributes that were relevant to Other Games. Solved: Attributes were incorrectly given the wrong Game ID prior to testing, they have been removed.
5) Ranking System Always Says "0" - Error: Ranking Names not showing.  Solved: the get_rank function needed to be remade outside of the games models file.
6) Live Chat Updating Incorrectly - Error: Live Chat would display strange characters. Solved: Characters removed.  Only text is not available.
7) Stripe Payment Not Responding - Error:  Payments for subscriptions not available.  Solved: Stripe.js file not being opened do to missing {% load_scripts %}
8) User Profiles Errors - Error: Nothing Works/Nothing Saves/Can Save Many User Profiles from One User.  Solved.
9) Images Do Not Load - Error: No Images Load.  Solved: Missed a settings Modual in base.py
10) Heroku Key Error - Error: Issues on Heroku Deploy.  Solved: Used Incorrect Key.

[^1]: https://newzoo.com/games-market-data/reports/global-games-market-reports/global-games-market-report/
[^2]: https://www.mpaa.org/wp-content/uploads/2014/03/MPAA-Theatrical-Market-Statistics-2013_032514-v2.pdf

