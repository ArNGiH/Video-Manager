import os
import pymongo
from bson import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB URL from environment variable
mongo_url = os.getenv('MONGO_URL')

if not mongo_url:
    raise ValueError("MongoDB URL is not set in the .env file")

# Create a MongoDB client
try:
    client = pymongo.MongoClient(mongo_url, tlsAllowInvalidCertificates=True)
    print("MongoDB client created successfully")
except Exception as e:
    print(f"Error creating MongoDB client: {e}")

# Access the database and collection
db = client.get_database("manager")
video_collection = db.get_collection("videos")

def add_video(name, time):
    try:
        result = video_collection.insert_one({"name": name, "time": time})
        print(f"Video '{name}' added successfully with id {result.inserted_id}")
    except Exception as e:
        print(f"Error adding video: {e}")

def list_videos():
    try:
        videos = video_collection.find()
        for video in videos:
            print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    except Exception as e:
        print(f"Error listing videos: {e}")

def update_video(newname, newtime, video_id):
    try:
        video_id = ObjectId(video_id)
        result = video_collection.update_one(
            {'_id': video_id},
            {"$set": {"name": newname, "time": newtime}}
        )
        if result.matched_count > 0:
            print(f"Video with id {video_id} updated successfully")
        else:
            print(f"No video found with id {video_id}")
    except Exception as e:
        print(f"Error updating video: {e}")

def delete_video(video_id):
    try:
        video_id = ObjectId(video_id)
        result = video_collection.delete_one({'_id': video_id})
        if result.deleted_count > 0:
            print(f"Video with id {video_id} deleted successfully")
        else:
            print(f"No video found with id {video_id}")
    except Exception as e:
        print(f"Error deleting video: {e}")

def main():
    while True:
        print("\nStreamer manager with Mongo database:")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update a Video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter your video name: ")
            time = input("Enter the duration of the video: ")
            add_video(name, time)
        elif choice == '3':
            name = input("Enter the new name of the video you want to update: ")
            time = input("Enter the new duration of the video you want to update: ")
            video_id = input("Enter the video id you want to update: ")
            update_video(name, time, video_id)
        elif choice == '4':
            video_id = input("Enter the video id you want to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("Exiting the process...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
