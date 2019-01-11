# Questioner

# Project Overview
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

# Badges
[![Build Status](https://travis-ci.org/Hackitect/questioner.svg?branch=master)](https://travis-ci.org/Hackitect/questioner)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Hackitect/questioner/pulls)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/hackitect/questioner.svg)](https://github.com/hackitect/questioner/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed)
[![Coverage Status](https://coveralls.io/repos/github/Hackitect/questioner/badge.svg)](https://coveralls.io/github/Hackitect/questioner)

# Endpoints required for testing
<!-- * `POST /meetup` Create a meetup record<br>
* `GET /meetups/<meetup-id>`Fetch a specific meetup record<br>
* `GET /meetups/upcoming/ ` Fetch all upcoming meetup records<br>
* `POST /questions` Create a question for a specific meetup<br>
* `PATCH /questions/<question-id>/upvote` Upvote (increase votes by 1) a specific question.<br>
* `PATCH /questions/<question-id>/downvote` Downvote (decrease votes by 1) a specific question.<br>
* `POST /meetups/<meetup-id>/rsvps` Respond to meetup RSVP.<br> -->

| METHOD  	| ROUTE  	|   DESCRIPTION	|
|---	|---	|---	|
|   POST	| `/meetup`   	|  Create a meetup recorD 	|
|   GET	|  `/meetups/<meetup_id> `	|  fetch a specific meetup record 	|
|   GET	|  `/meetups/upcoming/`	|  Fetch all upcoming meetup records 	|
|   POST	| `/questions ` 	|   Create a question for a specific meetup 	|
|   PATCH	|  `/questions/<question_id>/upvote` 	|  Upvote (increase votes by 1) a specific question. 	|
|   PATCH	|  `/questions/<question-id>/downvote` 	| Downvote (decrease votes by 1) a specific question  	|
|   PATCH	|  `/meetups/<meetup-id>/rsvps` 	|  Respond to meetup RSVP 	|

# Contributors

[Charles Njenga](https://github.com/Hackitect)







