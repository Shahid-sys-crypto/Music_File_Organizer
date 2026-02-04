import os
import shutil
from mutagen import File
import json

def scan_directory(directory,extensions=[".mp3",".flac",".wav"]):
    music_files=[]
    for root,_,files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                music_files.append(os.path.join(root,file))
    return music_files

def extract_metadata(file_path):
    try:
        audio=File(file_path,easy=True)
        if audio is None:
            return None
        return {
            "title":audio.get("title",["unknown title"])[0],
            "album":audio.get("album",["unknown album"])[0],
            "genre":audio.get("genre",["unknown genre"])[0],
            "artist":audio.get("artist",["unknown artist"])[0]
        }
    except Exception as e:
        print(f"Error extracting metadata for {file_path}:{e}")
        return None
def organize_files(music_files,output_directory):
    for file in music_files:
        metadata=extract_metadata(file)
        if metadata:
            artist=metadata["artist"]
            album=metadata["album"]
            artist_folder=os.path.join(output_directory,artist)
            album_folder=os.path.join(artist_folder,album)
            os.makedirs(album_folder,exist_ok=True)
            destination=os.path.join(album_folder,os.path.basename(file))
            shutil.move(file,destination)
            print(f"moved:{file}->{destination}")
def save_summary_to_json(music_files,output_file):
    summary=[]
    for file in music_files:
        metadata=extract_metadata(file)
        if metadata:
            summary.append(metadata)
    with open(output_file,"w") as json_file:
        json.dump(summary,json_file,indent=4)
    print(f"summary saved to {output_file}")
def main():
    print("welcome to the music playlist organizer")
    music_direactory=input("enter the the directoty of musics")
    output_directory=input("enter the path to organize musics")

    music_files=scan_directory(music_direactory)
    if not music_files:
        print("no music to be found")
        return None
    print(f"found {len(music_files)} music files")
    save_summary_to_json(music_files,"music_summary.json")
    organize_files(music_files,output_directory)
    print("music organization completely")
if __name__=="__main__":
    main()
            