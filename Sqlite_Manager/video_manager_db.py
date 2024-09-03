import sqlite3
conn=sqlite3.connect("Streamer_videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY ,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )

 ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()
    

def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (name, time, video_id))
    conn.commit()
    
    

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()



def main():
    while True:
        print("\n")
        print("Streamer manager with database:")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update a Video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name= input("Enter the video name: ")
            time=input("Enter the video time:")
            add_video(name, time)

        elif choice == '3':
            video_id=input("Enter the video id to update ")
            name= input("Enter the new video name: ")
            time= input("Enter the new video time:")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id=input("Enter the video id to delete ")
            delete_video(video_id)  
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

    conn.close()

if __name__ == '__main__':
    main()

