1. Consumper.py : Main
  -Creates Twitter instance
  -Listens real time tweets via my twitter application which is created for this project
  -I used only hashtag filters such as #newyork, #london etc /also we can filter by location follower count, friends count/
  -send it to localhost:9000 through topic named test
2. Producer.py : Main  
  -Listes real time at localhost:9000 through topic named test
  -do simple Natural Language multiprocessing
        -I have positive.txt, negative.txt which posses words.
        -If the tweet contains words from these lib they will count and will be calculcated
            -for example 'this is good tweet' 0.25 positive 0.0 negative tweet_text
            -if tweet doesn't contain any word from this lib we will skip.
  -save result into two places
        -if the HBase is working correctly, it will put it into ns_twitter:tb_twitter
        -if HBase is not working/in case of emergency/, I am also saving it into calculated1.txt which is not good way to store data.
3. rowid.txt : Main
   -if the program starts row_id is 0 and row_id.txt is empty. As we stream data we have to generate row_id's but in HBase it is kind of difficult to get row_id, so I wrote simple logic that saves and reads row_id from txt file.
4. db_connection.py : Main
   kafka_start.py : Main
   twitter_api_start.py : Main
   - these are just start up and test files. Don't care about it.
5. configs.text
  -It has some steps, I used to start and set up my local machine
  -Hadoop, Hbase, Kafka, Zookeeper, Jupyter, even Python
6. screen_shots
  -this folder contains few SS that shows I created table and it had data on it. Also shows that kafka producer and consumer is working at the same time in right place of the screen.
7. jupyter_result
  -I created very simple pie chart that shows percentage of positive and negative tweets.
  -If we collect datas day by day, we can see more fun charts such as which day and time people tweets positive or negative things.
