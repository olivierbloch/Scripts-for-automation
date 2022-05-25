# Upload Captions to YouTube video

This script allows to upload multiple captions files to a YouTube video.
It uses the YouTube APIs (specifically the [Captions Insert](https://developers.google.com/youtube/v3/docs/captions/insert) API) and requires a Google account that has Owner permissions on the channel.

## Prerequisites

1. Download the [repo](https://github.com/olivierbloch/Scripts-for-automation/archive/refs/heads/main.zip) and extract it in a folder of your choice.

1. Install Python from <https://www.python.com/downloads>

1. Obtain Google OAuth Client ID:
   In order to run the script, you will need to obtain OAuth authorization credentials from the Google developer console. For this, you can follow the steps [here](https://wpythub.com/documentation/getting-started/set-youtube-oauth-client-id-client-secret/). When following the steps at this link, after completing all steps including 3.5, select "Desktop app" as the application type, and name your app anything you want, then download the json file, place it next to the py script file (in the current folder) and rename it **client_secret.json**

## Usage

1. If that's the first time you are running the script or if your token has expired, delete the **token.json* file.

1. The script expects to have the following vtt files in a single folder (for example C:\Captions):

   - caption-en-us.vtt
   - caption-fr-fr.vtt
   - caption-de-de.vtt
   - caption-it-it.vtt
   - caption-ja-jp.vtt
   - caption-ko-kr.vtt
   - caption-pt-pt.vtt
   - caption-ru-ru.vtt
   - caption-es-es.vtt
   - caption-zh-cn.vtt

   If you are getting them from the Docs Video Portal, just download every single vtt file in a folder.

1. Get your YouTube video ID from your YouTube video URL, extract the ID (see bold part in examples):

   <pre>
      https://www.youtube.com/watch?v=<b>OzTagK628FM</b>
      https://youtu.be/<b>OzTagK628FM</b>
   </pre>

1. Run the script

   From the Terminal, make sure you are in the folder where the script file is, then type the following command (replacing the video ID and path to captions files with yours):

   ```bash
      python .\UploadCaptions.py OzTagK628FM "C:\Captions"
   ```

1. Get your authorization code

   On the first run or after you have deleted the token.json file, you will be prompted to visit a URL and get an authorization code. For this, visit the URL displayed in your terminal:

   ![Visit URL prompt](.\Assets\UploadCaptions_1.png)

   Select the brand account to get the credentials for:

   ![Select Brand account](.\Assets\UploadCaptions_2.png)

   Click on **Continue** to discard warning message:

   ![Discard warning message](.\Assets\UploadCaptions_3.png)

    Click on **Allow** to generate and access your code:

   ![Allow the app to access the google account](.\Assets\UploadCaptions_4.png)

    Copy the Code:

   ![Copy the code](.\Assets\UploadCaptions_5.png)

    Paste the code in your terminal and hit **Enter**

   ![Paste the code and continue the script](.\Assets\UploadCaptions_6.png)

    From here, the script will proceed with the creation of the captions and upload of the files from the local folder
