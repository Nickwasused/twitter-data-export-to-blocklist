

# Docs for Twitter-data-export-to-blocklist

This Page is going to instruct you how to use the program.

# Setup (Based on Windows)

Requirements for this Guide are:

- Python3 
- pip3

If you don't have Python3 installed then here is a Guide: [https://phoenixnap.com/kb/how-to-install-python-3-windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)  

Continue by downloading the Repository code from here: [https://github.com/Nickwasused/twitter-data-export-to-blocklist/archive/refs/heads/main.zip](https://github.com/Nickwasused/twitter-data-export-to-blocklist/archive/refs/heads/main.zip)

Now unpack the folder to your Desktop.

At this point, you should have Python3 with pip3 installed, and a folder called "twitter-data-export-to-blocklist-main" on your desktop.

Now enter the folder, it should look like this:

![Folder](./images/image_1.webp)

After you have opened the folder, press `SHIFT` and press the Right mouse button `RMB`.

You should see something like this:

![RMB](./images/image_2.webp)

Somewhere should be a point to "Open PowerShell window here". Click on that.

A PowerShell window should open.

![PowerShell](./images/image_3.webp)

Now enter the following command: `pip3 install -r requirements.txt --user`.

After that, you have all required packages installed and can use the program.

# Twitter

Now you need to obtain two things:

- The Twitter Data archive
- A Twitter Developer Account (With Elevated access!)

## Twitter Archive

The first one is easy, go to the Settings > Your Account > Download an Archive of your Data (See images below)

![Twitter-Archive](./images/image_4.webp)

Now wait for the email that the Archive is ready and after that extract the archive to the "export" folder in the "twitter-data-export-to-blocklist-main" folder.

![Extracted Archive](./images/image_5.webp)

## Twitter Credentials

Getting a Twitter developer Account has gotten more easy over time, just follow the Steps. [https://developer.twitter.com](https://developer.twitter.com)

You are now logged in to the Dashboard.

![Dashboard](./images/image_6.webp)

Now create a new Project and give it a random name. (For example, a bad name would be "advertising blocker" or something like that.)
The use case should be "Student" or "Teacher". I can't help you with the project description, just get creative here.

![Twitter](./images/image_7.webp)

"Add an existing App or create a new App" at this point select create a new APP.

For the name, get creative again.

Now copy your API_KEY and API_SECRET and save them somewhere.

![Keys](./images/image_8.webp)

Now go to your App Page and select "Keys and tokens".

![Page](./images/image_9.webp)

After that, scroll down to "Access Token and Secret" and click on generate.

![Tokens](./images/image_10.webp)

Now copy the generated "ACCESS_TOKEN" and "ACCESS_TOKEN_SECRET"

![Copy](./images/image_11.webp)

At this point, you need to go back to the folder "twitter-data-export-to-blocklist-main". Now rename ".env.example" to ".env".
Open the ".env" file and fill in the values.

The file should look like this now: 

![File](./images/image_12.webp)

After that, go to Products > Twitter API v2 and click on Elevated.

![Elevated](./images/image_18.webp)

After that, apply for the elevated access.

![Elevated-2](./images/image_19.webp)

Please keep in mind that you need to be creative while applying, don't write something like: "Hello Twitter I would like to block AD's."

# Generating the List

Now go back to your PowerShell window (the blue one) and type ```python main.py``` (or maybe ```python3 main.py```).

The output should look like this:

![Output](./images/image_13.webp)

# Uploading

Now you need to upload the generated list in a raw format.

Go back to the "twitter-data-export-to-blocklist-main" folder and right-click on the file "export.csv", after that click on edit or open in editor.

Click inside the editor window and press `STRG-A` and `STRG-C`.

Now go to the website [https://pastebin.com](https://pastebin.com) and click inside the edit field there. Now press `STRG-V`.

The Page should look similar to this:

![pastebin.com](./images/image_14.webp)

Now click on create new paste and after that on "raw" (See below).

![raw](./images/image_15.webp)

# Blocking

Now you need to go to [https://twitter-blocklist-auth.glitch.me/](https://twitter-blocklist-auth.glitch.me/) and log in.

After that, you paste the Pastebin link there and press submit.

![block-submit](./images/image_16.webp)

After that, the page is going to tell you how many accounts got blocked.

![block-result](./images/image_17.webp)