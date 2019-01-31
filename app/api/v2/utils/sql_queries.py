tables = (
            """
            CREATE TABLE IF NOT EXISTS users(
                user_id serial PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                lastname VARCHAR(20) NOT NULL,
                username VARCHAR(20) NOT NULL,
                phonenumber VARCHAR(15) NOT NULL,
                email VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL,
                is_admin bool
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS meetups(
                meetups_id serial PRIMARY KEY,
                topic VARCHAR(30) NOT NULL,
                location VARCHAR(30) NOT NULL,
                happeningon TIMESTAMP,
                created_on TIMESTAMP,
                tags VARCHAR(100)
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS questions(
                questions_id serial PRIMARY KEY,
                createdon TIMESTAMP,
                title VARCHAR(30) NOT NULL,
                body VARCHAR(100) NOT NULL,
                votes INTEGER DEFAULT 0,
                meetupid INTEGER REFERENCES meetups(meetups_id),
                createdby INTEGER REFERENCES users(user_id)
                ON UPDATE CASCADE ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS answers(
                answers_id serial PRIMARY KEY,
                data VARCHAR NOT NULL
            );
            """)
# tables = []