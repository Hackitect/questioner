import datetime
from datetime import timedelta

meetups_db = [
    {
        "id": 4,
        "topic": "Andela Hackathon",
        "location": "PAC University",
        "happeningOn": "2019-03-17 12:37'",
        "tags": ["python", "machine learning"]
        },
    {
        "id": 1,
        "topic": "Advanced CSS3",
        "location": "The Hub",
        "happeningOn": "2019-02-17 12:37'",
        "tags": ["html", "css"]
        },

    {
        "id": 0,
        "topic": "Ubuntu Server Hangout",
        "location": "The Hub",
        "happeningOn": "2010-01-17 12:00'",
        "tags": ["linux", "server"]
    }

]

''' This is the response spec for a meeting
{
    "status": Integer,
    "data": [{
        "id": Integer,
        "topic": String,
        "location": String
        "happeningOn": Date,
        "tags": [String, String, ....]
    }

    ]
}
'''

class Meetups:
    
   

    @staticmethod
    def find_by_id(meetupId):
        # list comprehension
        return[meetup for meetup in meetups_db if meetup['id']==meetupId]

         
    def all(self):
        if len(meetups_db) == 0:
            return {"message": "empty database"}
        return [meetup for meetup in meetups_db]

    def new(self, new_meetup):
        meetups_db.append(new_meetup)
        return new_meetup

    def upcoming(self):
        # today = '{}'.format(datetime.datetime.now())

        """ to get upcoming meeting, the date has to be in the future
            we therefore need to loop through every meetup - happeningOn - value
            if its greater than now, the return the meetup          
        """    
        
        if len(meetups_db) == 0:
            return {"message": "no meetups found"}
        else:
            resp = [meetup for meetup in meetups_db if meetup['happeningOn'] > datetime.datetime.now().strftime('%Y-%m-%d %H:%M')]
            return resp
                # return the time delta
                # if negative then meetup has already taken place, return only +ve dates
                # meetup['happeningOn' "2019, 3, 8, 7, 50, 55, 529588" 
                # today "2019-01-10 11:55:55.892852"
                # datetime.datetime.strptime(meetup['happeningOn'], '%Y-%m-%d %H:%M:%S,%f')
                # time_delta = timedelta(meetup['happeningOn'] - today)
                # if meetup['happeningOn'] > datetime.datetime.now().strftime('%Y-%m-%d %H:%M'):