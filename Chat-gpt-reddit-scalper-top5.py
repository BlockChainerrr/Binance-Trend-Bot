import requests
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import time

now = datetime.now()
current_time = date.today()
filter = 'all'

# ADD YOUR TOKENS HERE!
Telegram_Photo_Token = ""
Telegram_Message_Token = "6300914470:AAEZ5HswO98Wci8yEH5XZaqNd7O6xg3qmOs"
CHAT_ID = "5578195224"

def send_picture():
    # Send plot picture to Telegram.
    # Create a variable with the path to str(current_time) + '.png' in rb mode.
    file = open(str(current_time) + '.png', 'rb')
    time.sleep(40)
    url = f"https://api.telegram.org/bot{Telegram_Photo_Token}/sendPhoto"
    files = {'photo': file}
    payload = {'chat_id': CHAT_ID}
    response = requests.post(url, data=payload, files=files)
    print(response)
    # Close str(current_time) + '.png'.
    file.close()
    os.remove(str(current_time) + '.png')

def main():
    pageNbr = 1
    while pageNbr < 2:
        url = f'https://apewisdom.io/api/v1.0/filter/{filter}/page/{pageNbr}'
        response = requests.get(url)
        pageNbr += 1
        # Extract results list from response.
        results = response.json()['results']
        # For each result in results: put into a dataframe.
        df = pd.DataFrame(results)
        # Convert all numbers to floats.
        df['mentions'] = df['mentions'].astype(float)
        # Plot the top 25 tickers by mentions.
        df.sort_values(by='mentions', ascending=False).head(25).plot(kind='bar', x='ticker', y='mentions')
        plt.title('Top 25 tickers in Reddit by mentions ' + str(current_time))
        # Label the x-axis with tickers and the y-axis with mentions.
        plt.xlabel('Ticker')
        plt.ylabel('Mentions')
        # Save the plot to a file with the current time.
        plt.savefig(str(current_time) + '.png')
        # Append the top 25 tickers to the tickers list.
        tickers = df.sort_values(by='mentions', ascending=False).head(5)['ticker'].tolist()
        print(tickers)
        # Check for new tickers and send a request post to Telegram.
        for ticker in tickers:
            if ticker not in tickers_list:
                print(ticker)
                url = f"https://api.telegram.org/bot{Telegram_Message_Token}/sendMessage"
                payload = {'chat_id': CHAT_ID, 'text': ticker + ' is trending on Reddit'}
                response = requests.post(url, data=payload)
                if response.status_code != 200:
                    print("Error sending message:", response.text)
                    return  # Exit the function to break out of the loop
                tickers_list.append(ticker)
        # Check for tickers that have been removed and send a request post to Telegram.
        for ticker in tickers_list:
            if ticker not in tickers:
                print(ticker)
                url = f"https://api.telegram.org/bot{Telegram_Message_Token}/sendMessage"
                payload = {'chat_id': CHAT_ID, 'text': ticker + ' has been removed from the list'}
                response = requests.post(url, data=payload)
                if response.status_code != 200:
                    print("Error sending message:", response.text)
                    return  # Exit the function to break out of the loop
                tickers_list.remove(ticker)
                time.sleep(1)
        send_picture()

tickers_list = []

while True:
    print("New load")
    main()
    time.sleep(3600)
