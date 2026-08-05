class Solution:
    def candy(self, ratings: List[int]) -> int:
        #brute force hard to do if statement and everytime do left to right
        #2 pass is O(n) left-to right pass we look left. right to left pass we look right
        #greedy
        arr = [1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                arr[i] = arr[i-1]+1
        #second pass
        for i in range (len(ratings)-2,-1,-1):
            if ratings[i]> ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1]+1)

        return sum(arr)