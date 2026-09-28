class Twitter:

    def __init__(self):
        self.count = 0
        self.followermap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res =[]
        minheap =[]
        self.followermap[userId].add(userId)
        for followeeid in self.followermap[userId]:
            if followeeid in self.tweetmap:
                index = len(self.tweetmap[followeeid])-1
                count,tweetId = self.tweetmap[followeeid][index]
                minheap.append([count,tweetId,followeeid,index-1])
        heapq.heapify(minheap)

        while minheap and len(res)<10:
            count,tweetId,followeeid,index = heapq.heappop(minheap)
            res.append(tweetId)

            if index >=0:
                count,tweetId = self.tweetmap[followeeid][index]
                heapq.heappush(minheap,[count,tweetId,followeeid,index-1])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followermap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followermap[followerId]:
            self.followermap[followerId].remove(followeeId)

