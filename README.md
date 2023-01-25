# Youtube Statistics

A script to extract statistics from youtube channels. As the title says, it uses the YouTube Data API. 
In this case, I briefly used it to extract statistics like Subscribers, Likes, Dates and View Counts. But it gives other information too.
Props to @Patrickloeber youtube tutorial, it gave me the main base on which this project is based on. 

## Requirements

pip install requests (for GET requests)
pip install tqdm (for the Progressbar)

*Use the main.py file from this repo, in order to execute the program. 

## API KEY
https://developers.google.com/youtube/v3/getting-started
https://console.developers.google.com/

**Well need an API key in oreder to make the requests. 

So follow the next steps:

*1-Go to the second link and create an account in case you dont have one. 
*2-Go to API and Services and enable a new one. Itll give you a list with different APIs that you can use.
*3-Choose the Youtube Data API v3 and enable it.
*4-Right next to the Google Cloud Icon, youll find the buttom to create a new project, name it.
*5-Once created, selcet it and obtain the authorization credentials. Save the token. 

You can check if the API is enabled, in the  Enable APIs page, if you select the API (youtube data v3) it should say its enabled.  

PS: If you are having troubles with the channel id, when copying it with the @. Find the alphanumeric one in the source code, it worked for me.






