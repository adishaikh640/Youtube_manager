
import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with  open ('youtube.txt', 'w') as file:
        json.dump(videos, file)  


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}.  {video['name']}, Duration: {video['time']},  ")
    print("\n")
    print("*" * 70)


def add_videos(videos):
    name = input("Enter Video Name:")
    time = input("Enter Video Time:")
    videos.append({'name': name, 'time': time })
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)

    index = int(input("Enter The Video NUmber To Update :"))
    if 1 <= index <= len(videos):
        name = input("Enter Video Name:")
        time = input("Enter Video Time:")
        videos [index - 1] = ({'name': name, 'time': time })
        save_data_helper(videos)
    else:
         print("Invalid Syntax")



def delete_videos(videos):
     list_all_videos(videos)
     index = int(input("Enter the video number to be deleted"))
    
     if 1<= index <= len(videos):
            del videos[index-1]
            save_data_helper(videos)
     else:
            print("Invalid video index selected")

def main():
    videos = load_data()
    while True:
        print("\nYOUTUBE MANAGER | CHOOSE AN OPTION")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. EXIT")

        choice = input("Enter your choice: ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()