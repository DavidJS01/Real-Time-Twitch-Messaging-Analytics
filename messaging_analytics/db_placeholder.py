import sqlite3

conn = sqlite3.connect('./data/test_db.db', check_same_thread=False)
c = conn.cursor()

def connect_to_db():
    conn = sqlite3.connect('./data/test_db.db')
    c = conn.cursor()

def create_streamer_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS streamers ([streamer_id] INTEGER PRIMARY KEY, [streamer_name] TEXT, UNIQUE(streamer_id, streamer_name))
    ''')
    conn.commit()

def insert_new_streamer(streamer_id, streamer_name):
    c.execute('INSERT OR IGNORE INTO streamers values (?,?)', (streamer_id, streamer_name))
    conn.commit()

def create_messages_table(): # This will be less ugly soon!
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages ([viewer_name] TEXT, [streamer_id] INTEGER,
                                            [game] TEXT, [viewer_message] TEXT,
                                            [message_date] TEXT
            )
        ''')
    conn.commit()

def insert_new_message(viewer_name, streamer_id, game, message): #@TODO: Make this prettier and less "hacky"
    conn = sqlite3.connect('./data/test_db.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('INSERT INTO messages VALUES (?,?,?,?, DATETIME("now"))', (viewer_name, streamer_id, game, message))
    conn.commit()
    conn.close()

connect_to_db()
create_streamer_table()
create_messages_table()

