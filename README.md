# Reddit Timed Poster
Posts specified links at a specific time, so you can post at peak hours without physically posting

# Installing

1. Install [Python](http://www.python.org/download/) (Python 2.7)
2. Install PRAW (you'll need this so the script can actually access reddit)
3. Download the ZIP from above and extract it
4. Edit the submission json with your information (more info below)
5. To run the bot, navigate to the location you unzipped the folder via the command line/terminal and "python autoposter.py" (without quotes)
6. Relax and leave the command line/terminal and computer open, the script will automatically post the link at the specified time. 

# Submission JSON

The submission JSON file contains several parameters, which are then used to make the post to reddit. Leave everything in the quotes.

## Subreddit

Simply put the name of the subreddit you want to post to in this field. For example, if I want to make a post to reddit.com/r/AskReddit, I'll put "AskReddit" in the field.

## Username and Password

This is the account you're going to post from. Put the username and password to the account that's making the post. **This will be reworked to use OAuth2 in the future**

## Title

This is the title to your submission. Just put the title in this field. 

## Link

Put the link in this field. I will add functionality for self posts and text at a later date. 

## Time

This is the bread and butter of the script. For the **month** field, input the month number (January is 1, March is 3, July is 7 ...). For the **day** field, input the date in the month (July 8th would mean you input 7 for the month, and 8 for the day). For the **hour**, input the hour in 24 hour time (0-23) and for **minutes**, input the minutes. So if I wanted July 8th, 4:00pm, I would input 7 for the month, 8 for the day, 16 for the hour, and 0 for the minutes. 

# Future of this script

I will add more functionality for text posts, multiple posts, posting to multiple subreddits, and better error handling if the user has inputted something in the JSON incorrectly. 

