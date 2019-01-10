import datetime

meetups_db = [
    {
        "id": 4,
        "topic": "Andela Hackathon",
        "location": "PAC University",
        "happeningOn": "2019, 3, 8, 7, 50, 55, 529588",
        "tags": ["python", "machine learning"]
        },
    {
        "id": 1,
        "topic": "Advanced CSS3",
        "location": "The Hub",
        "happeningOn": "2010, 1, 8, 7, 50, 55, 529588",
        "tags": ["html", "css"]
        },

    {
        "id": 0,
        "topic": "Ubuntu Server Hangout",
        "location": "The Hub",
        "happeningOn": "2019, 2, 8, 7, 50, 55, 529588",
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
    
    # def __init__(self, topic, location, tags):
    #     self.id = len(meetups_db)+1
    #     self.topic = topic
    #     self.location = location
    #     self.tags = tags

    def save(self):
        meetups_db.append(self)



    @staticmethod
    def find_by_id(meetupId):
        # list comprehension
        return[meetup for meetup in meetups_db if meetup['id']==meetupId]

        # for meetup in meetups_db:
        #     if meetup['id'] == meetupId:
        #         return meetup
            # else:
            #     return {"message": "No meetup found with that id"}
    
    def all(self):
        if len(meetups_db) == 0:
            return {"message": "empty database"}
        return [meetup for meetup in meetups_db]

    def upcoming(self):
        today = datetime.datetime.now()

        """ to get upcoming meeting, the date has to be in the future
            we therefore need to loop through every meetup - happeningOn - value

            if its greater than now, the return the meetup       
        
        """    
        
        if len(meetups_db) == 0:
            return {"message": "no meetups found"}
        else:
            for meetup in meetups_db:
                time_difference = abs((meetup['happeningOn'] - today).days)
                return {"message": time_difference}
            # return[meetup for meetup in meetups_db if meetup['happeningOn']==meetupId]

