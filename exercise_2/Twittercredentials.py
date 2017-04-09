import tweepy

consumer_key = "Vk9kCWPUw8KctdN4QGywZFpvd";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";

consumer_secret = "CoPsToBCXDYWkaxoSnPf9qnNEPazxvHGDzexDzZ6KJxq9ZplQb";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "820596649-FSomVy8OakTPYrCKrJQw2IfsUZXGk5Xp6kCzfbFt";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "c2jLc2HNQPKFGncaeNQzRonB4B9LOOKOU67lVcaOeEzYK";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



