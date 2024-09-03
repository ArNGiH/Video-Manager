def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos=[]
    while(True):
        print("\n Video Manager | Choose an option")
        print("1. List a favorite video")
        print("2. Add a video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit")
        choice=input("Enter your choice")


        match choice:
            case '1':
                list_all_videos(videos)
                
            case '2':
                add_video(videos)
                
            case '3':
                update_video(videos)
                
            case '4':
                delete_video(videos)
                
            case '5':
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice. Please try again.")



if __name__ =="__main__":
    main()