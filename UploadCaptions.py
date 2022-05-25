import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib.flow
import googleapiclient.errors
from googleapiclient.discovery import build

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

captions = {
    "videoID": sys.argv[1],
    "languages":{
        "English": {
            "code":"en",
            "title":"English",
            "file":"caption-en-us.vtt"
        },
        "French":{
            "code":"fr",
            "title":"French",
            "file":"caption-fr-fr.vtt"
        },
        "German":{
            "code":"de",
            "title":"German",
            "file":"caption-de-de.vtt"
        },
        "Italian":{
            "code":"it",
            "title":"Italian",
            "file":"caption-it-it.vtt"
        },
        "Japanese":{
            "code":"ja",
            "title":"Japanese",
            "file":"caption-ja-jp.vtt"
        },
        "Korean":{
            "code":"ko",
            "title":"Korean",
            "file":"caption-ko-kr.vtt"
        },
        "Portuguese":{
            "code":"pt",
            "title":"Portuguese",
            "file":"caption-pt-pt.vtt"
        },
        "Russian":{
            "code":"ru",
            "title":"Rusian",
            "file":"caption-ru-ru.vtt"
        },
        "Spanish":{
            "code":"es",
            "title":"Spanish",
            "file":"caption-es-es.vtt"
        },
        "Chinese":{
            "code":"zh",
            "title":"Chinese Simplified",
            "file":"caption-zh-cn.vtt"
        }
    }
}

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"


    credentials = None
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', scopes)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
        # Get credentials and create an API client
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials = flow.run_console()
                # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    for language in captions["languages"].values():
        caption_file_path = sys.argv[2] + "\\" + language["file"]
        print("Adding captions to video with ID " + captions["videoID"] + 
              ": \n\tcode: " + language["code"] + 
              "\n\t" + language["title"] +
              "\n\t" + caption_file_path)
        request = youtube.captions().insert(
            part="snippet",
            sync=False,
            uploadType="resumable",
            body={
            "kind": "youtube#caption",
                "snippet": {
                    "videoId": captions["videoID"],
                    "language": language["code"],
                    "isDraft": False,
                    "name": language["title"]
                }  
            },
            
            media_body=MediaFileUpload(caption_file_path)
        )
        try:
            response = request.execute()
            print(language["title"] + " captions added")
        except googleapiclient.errors.HttpError as err:
            if err.status_code == 409:
                print("This video already has this language caption.")
                pass
            else:
                raise
            
    

if __name__ == "__main__":
    main()