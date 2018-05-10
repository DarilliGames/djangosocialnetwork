## Django Social Network

####  About

##### Industry Insight 

Video Games is the fastest growing form of Media Industry,  in 2013 the Gaming Industry generated $70.4 billion ([^1]) vs Worldwide Films at only $35.9 billion([^2]).

In addition, the numbers of professional Gamers has also dramatically increased.  One reason is both through websites like Twitch.tv, Youtube and more catagorising Gamers and their videos as entertainment.  The other reason is the Prize Pool's for Competitive Tournements has also increased.

#### Features

##### Accounts

The Accounts App offers a number of features from Registration, Login and Logout, Accounts deleting.
Each account has the ability to be customised with a profile picture, basic information and a "Main Character" (more on this later).

Each User can create a number of Characters.  These characters are their in game avatars and accounts with relative details for that specific game.  The basic Character has a set number of variables (eg. name, what game the character is in, what rank they are).  For different games though the values of this information can vary dramatically, in one game being "Rank 1" means you are the best in the world;  while in another this rank could be the sign of a brand new player.  A way around this was created and functional, more details in "Difficulties" Section.
In addition to these features, depending on the game specific attributes may be desired for searching purposes (eg. team, role, position, etc.).  I call my solution "Variable Characteristics", these possible characteristics are related to each Game but do not within the Game Model.

####  Games

A core part of the functionality is the Games Model.  Games have two images, a Thumbnail and Tall Box Art.  Games also can be reviewed, details added and more.

#### Review

Games can be reviewed through models on the game profile game.

####  Streams

Live Streaming is a huge part of the modern gaming industry.  Players Stream to get views, followers, donations and fees collected by streaming platforms for subscriptions to the players.  For Twitch.tv viewers pay €5 per month for additional perks.

For Game Publishers, Players streaming their game is a very valid for of advertising and player retension which is vital for the many publishers who are moving to subscription and/or micro-transaction based service.

Being such an important part of the industry, I knew I had to include it into the website.  The website has two forms of Stream, which I have termed "Dedicated" and "User Submitted".

Dedicated Streams are created and are visible all the time and I have set these up while there are no active users.  If released, these would service event based streams, featured or premium streams.

User Submitted are streams created by players once their user profile is completed and their Twitch.tv accounts are set up.

####  Search

A core for the website and a custom search funciton was required as again the "Variable Characteristics" cropped up.  In order for a character to be searched, a specific game must be selected first.  After a game is selected, it populates the search page with the possible attributes which may be selected as individual dropdown boxes, it then populates these dropdown boxes with the possible variables assigned to these attributes.

The search function will search for a character based off the Game, Name of the Character, Rank and any number of possible attributes.  Only if a variable charactistic is selected, only then it will be searched. 

####  Messaging

Messaging between users is available in two forms.  Mailboxes and instant messaging is available.  The Website also offers a chatroom, which any member can join.

This chatrom is made possible through AJAX, but in future versions a would be introduced.


####  Notifications

Unread messages from either your Mailbox or from any instant messages show up as a notification in the Nav-Bar.

####  Following

Following shows support for another user.  Currently, following a user offers no notifications, other than allowing you to find your favourite players easier.

#### Website Successes

#### Difficulties Present

##### Lack of Filter

Unfortunately, the basic Django Framework's filtering system does not allow for a core part of our search function.  That is the prementioned "Variable Characteristic".
In order the get around this difficulty I was required rearrange customised search functionality.

Unfortunately, this was a huge time investment but is crucial to the overall functionality of the website, now with a working version I am extremely proud of the outcome.

##### Live Chat

Instant Messaging was something I really thought the website could use to improve the user experience.  Originally I had thought of using a Mailling System but for users looking to find other players to play with would give up on waiting for replies.

I first set out to build and Instant Messaging system, I found a very rough guide on AJAX and PHP.  I figured give it a read and see if I could understand any of it - I was unsuccessful for the PHP part but I could salvage some of the AJAX.

Eventually, I had a very bugged version.  Which would load once and stop.  Then would do nothing.  About three days later I had a open chatroom with a live chat with AJAX polling every 3 seconds.  Through another long stage of trial and error I finally got a Private chat working.


[^1]: https://newzoo.com/games-market-data/reports/global-games-market-reports/global-games-market-report/
[^2]: https://www.mpaa.org/wp-content/uploads/2014/03/MPAA-Theatrical-Market-Statistics-2013_032514-v2.pdf

