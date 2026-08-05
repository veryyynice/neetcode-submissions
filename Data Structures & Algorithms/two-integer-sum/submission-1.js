class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const visited = new Map();
        for (let i =0; nums.length; i++){
            const current = nums[i];
            const dif = target-current;
            if (visited.has(dif)){
                return [visited.get(dif),i];
            }
            visited.set(current,i);
        }
        return [];
    }

//     class Solution:
//     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
//         visited = {}
//         for i in range(len(nums)):
//             current = nums[i]
//             if (target-current) in visited:
//                 return [visited[(target-current)],i]
//             visited[current] = i                

// #1,0,2,3 target was 5

}
