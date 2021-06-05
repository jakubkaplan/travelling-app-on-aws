# travelling-app-on-aws
Toy travelling app on AWS for learning new AWS technologies

The app will allow users to save travel places and prioritize them.

Followed this article to get started: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

Technologies: 
- Backend: Flask in Python
  
- Database: Dynamo DB
- Front-end: Bootstrap

##Use cases

P0:
- I view all travel destinations
- I view all travel destinations for which optimal quarter is Q1/Q2/Q3/Q4, ordered by priority ascending

P1:
- I view top priority destinations for which optimal quarter is TK

I can save a travel destination with ID, name, priority, quarter, country, state, description

Primary key
- HASH Key: DestinationID
- Sort Key: None

Optimal Quarter GSI
- HASH Key: optimal_quarter
- Sort key: priority
