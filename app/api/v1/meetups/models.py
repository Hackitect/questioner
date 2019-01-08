meetups_db = [
{
    "id": 1,
    "topic": "Andela Hackathon",
    "location": "PAC University",
    "happeningOn": "2019, 1, 8, 7, 50, 55, 529588",
    "tags": ["python", "machine learning"]
    },
{
    "id": 2,
    "topic": "Advanced CSS3",
    "location": "The Hub",
    "happeningOn": "2019, 1, 8, 7, 50, 55, 529588",
    "tags": ["html", "css"]
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

class Meetups():
    def find_by_id(self, meetupId):
        for meetup in meetups_db:
            if meetup['id'] == meetupId:
                return meetup
            else:
                return {"message": "No meetup found with that id"}
    
    def all(self):
        if len(meetups_db) == 0:
            return {"message": "empty database"}
        return meetups_db
