class Twitter:

    def __init__(self):
        
        #each user and tweet have id
        #keep most recent tweet and chornololigally
        #hashmap of who each user follows
        #who they follow
        self.whoFollows = defaultdict(set)

        #hash map each persons tweets (stack) with timestamp count, tweetid
        self.personsTweets = defaultdict(list)
        self.count = 0

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.personsTweets[userId].append([self.count,tweetId])
        self.count -=1
    #10 most recent tweet ids, each item must be by user who 
    #user is following or by the user themself. order by mst recent
    #min heap for every user , their most recent tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        #create minHeap
        res = []
        minHeap = []

        self.whoFollows[userId].add(userId)
        for followeeId in self.whoFollows[userId]:
            if followeeId in self.personsTweets:
                index = len(self.personsTweets[followeeId])-1
                count,tweetId = self.personsTweets[followeeId][index]
                #ordered by count
                minHeap.append([count,tweetId, followeeId, index-1])
        #DEFAULT MAX HEAP
        heapq.heapify(minHeap)
        #heapify and return res
        while minHeap and len(res)<10:
            count,tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >=0:
                count, tweetId = self.personsTweets[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId, followeeId, index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.whoFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.whoFollows[followerId]:
            self.whoFollows[followerId].remove(followeeId)
