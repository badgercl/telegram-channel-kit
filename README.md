# Scripts to easily setup a Telegran bot to post on a channel 

## Step 1: Create your bot
Go to the <a href="https://t.me/botfather">@botfather</a> bot and create a new bot using the /newbot comand. Follow the instructions and then you'll receive a bot token.
Keep this token safe and hidden from users. This is the way your code identifies and autenticates the calls to the bot API.

## Step 2: Save the bot token at the config file
Add the bot token to the telegram_config file on the bot_token field.

## Step 3: Create channel
Create a channel from the Telegram. It's up to you whether you create an username for it. We can easily get the internal UID in case you do not set the channel name.
Then add the bot as channel administrator and make sure it has at least posting permissions.

## Step 4: Get the channel UID 
In case your channel is private or you haven't created the channel with an username (the custom name shown on the invite link) you should get the channel's UID. In other case skip this step.

Once the bot is added to the channel, write anything on the channel from the Telegram app. Then run the get_updates script. It retrieves the last command and messages sent to the bot. You should get a result that looks like:

```
{
  "channel_post": {
  "chat": {
    "id": UID,
    "title": "Channel title",
    "type": "channel",
    "username": "your_channel_name"
  },
  "date": 1500656316,
  "message_id": 3,
  "text": "hi"
  },
  "update_id": 00000000
}
```

Find the "chat"->"id" value (in the example is UID). This is the unique identifier for your channel. It's a large negative number. You must copy this number including the negative symbol.

## Step 5: Add the Channel UID to the config file
Now you should have either the channel ID or the channel name.
Open again the telegram_config file and fill the channel_id field with the UID or the channel. In case of the channel, you must add an @ sign before the name. For example:

```
channel_id = "-234567890"
channel_id = "@my_channel_name"
```


## Step 6: Starting sending automatic messages
That's all.

test your bot by executing the send_example script. If everything is working well, on your channel should see a new message saying "Hello Channel".

After this setup, as administrator you can delete these messages using the Telegram App. Hence your users won't see them whem they start joining your channel.

The bot assumes HTML code as the text, you can change it to markdown by changing the setting on the telegram_config file. 
