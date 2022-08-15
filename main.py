import json

def main():
    tweets_retweeted()
    most_tweets()
    day_tweets()
    most_hashtags()


def tweets_retweeted():
    most_retweeted = []
    retweet_nums = []
    f = open('farmers-protest-tweets-2021-03-5.json')
    for l in f.readlines():
        data = json.loads(l)
        if len(most_retweeted) < 10:
            most_retweeted.append(data)
            retweet_nums.append(int(data['retweetCount']))
        else:
            for tweet in range(10):
                if int(data['retweetCount']) > retweet_nums[tweet]:
                    retweet_nums[tweet] = int(data['retweetCount'])
                    most_retweeted[tweet] = data
                    break
    print('------------------------')
    print('Los top 10 tweets más retweeted:\n\n')
    #print(retweet_nums)
    for i in range(len(most_retweeted)):
        print(f'{i+1}. {most_retweeted[i]}\n')
    f.close()

def most_tweets():
    user_num_tweets = {} # {str(user): int(num_tweets)}
    f = open('farmers-protest-tweets-2021-03-5.json')
    for l in f.readlines():
        data = json.loads(l)
        if data['user']['username'] not in user_num_tweets.keys():
            user_num_tweets[data['user']['username']] = 1
        else:
            user_num_tweets[data['user']['username']] += 1
    f.close()
    top_users = []
    tweet_count = []
    for i in range(10):
        user = max(user_num_tweets, key=user_num_tweets.get)
        top_users.append(user)
        tweet_count.append(user_num_tweets[user])
        del user_num_tweets[user]
    print('\n------------------------')
    print('Los top 10 usuarios en función de la cantidad de tweets que emitieron\n\n')
    for i in range(len(top_users)):
        print(f'{i+1}. {top_users[i]}: {tweet_count[i]}')
        

def day_tweets():
    pass

def most_hashtags():
    pass

if __name__ == '__main__':
    main()