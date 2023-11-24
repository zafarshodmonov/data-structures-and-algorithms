
class Solution:

    def max_sum_subarray(nums, k):
        # nums --> [3, 2, 1, 6, 4, 5]
        # k --> 3


        def window_sum_function(window: list):
            return sum(window)
        
        def max_sum_function(a : int, b : int):
            return max(a, b)
        
        n = len(nums)
        
        # 1-qadam:
        window = nums[k]  # window --> [2, 1, 6]
        window_sum = window_sum_function(window)  # window_sum --> 6
        max_sum = max_sum_function(0, window_sum)  # max_sum --> 6
        
        # Slide the window through the array
        for i in range(k, len(nums)):  # i --> 3 4 5
            # Add the new element and subtract the old element
            window = window[1:] + [nums[i]]
            # Update the maximum sum
            window_sum = window_sum_function(window)
            max_sum = max_sum_function(max_sum, window_sum)
        return max_sum

    def lengthOfLongestSubstring(self, s: str) -> int:

        def window_length_function(window: list) -> int:
            return len(window)
        
        def max_length_function(a: int, b: int) -> int:
            return max(a, b)
        
        # leetcode-3-medium
        # s --> "abcabcbb"
        window = []  # window --> ['a', 'b', 'c']
        for e in s:
            if e in window:
                break
            window.append(e)
        window_length = window_length_function(window)
        max_length = max_length_function(0, window_length)
        for i in range(len(window), len(s)):  # i --> 3 4 5 6 7
            if s[i] in window:
                window_length = window_length_function(window)
                max_length = max_length_function(max_length, window_length)

                # window-ni yangilash
                index = window.index(s[i])
                window = window[index + 1:] + [s[i]]
            else:
                window.append(s[i])
        return max_length_function(max_length, window_length_function(window))
    

    def longestNiceSubstring(self, s: str) -> str:
        # leetcode-1763-easy
        # s --> "YazaAay"
        def f(ch : str, zalist : list[str]):
            # s --> 'z'
            # zalist --> ['Y', 'a']
            lower_and_upper = [ch]
            if ch.islower():
                lower_and_upper.append(chr(ord(ch) - 32))
            else:
                lower_and_upper.append(chr(ord(ch) + 32))
            for e in lower_and_upper:
                if e not in zalist:
                    return [ch]
            zalist.append(ch)
            return zalist
        

        # 1-qadam:
        window = []  # window --> []

        # 2-qadam:

        # 3-qadam:
        for i in range(2, len(s)):  # i --> 2 3 4 5 6
            win = f(s[i], window)
            window = win if len(win) >= len(window) else window
        return window

    def countGoodSubstrings(self, s: str) -> int:
        # leetcode-1876-easy
        # s --> "xyzzaz"

        # 1-qadam: Initializatsiya: Dastlabki oynani uning hajmini aniqlash va kerakli o'zgaruvchilarni ishga tushirish orqali o'rnating.
        window = list(s[:3])

        # 2-qadam: Jarayonning dastlabki oynasi: Dastlabki oyna ichidagi elementlar uchun kerakli amallar yoki hisob-kitoblarni bajaring.
        count = 1 if 3 == len(set(window)) else 0

        # 3-qadam: Oynani siljitish: Oynani massiv yoki ro‘yxat bo‘ylab bir qadam siljiting.
        for i in range(3, len(s)):  # i --> 3 4 5

            # 4-qadam: Oynani yangilash: Oyna siljishi bilan oynaga kiruvchi yangi elementni qo‘shish va oynadan chiqayotgan eski elementni olib tashlash orqali elementlar to‘plamini samarali yangilang.
            window = window[1:] + [s[i]]

            # 5-qadam: Joriy oyna holatini qayta ishlash: Joriy oyna ichidagi elementlar uchun kerakli amallar yoki hisob-kitoblarni bajaring.
            count += 1 if 3 == len(set(window)) else 0

            # 6-qadam: Takrorlash: Oynani massiv yoki ro‘yxat oxirigacha siljitishda davom eting.

        # 7-qadam: Natijani qaytarish.    
        return count


        
        



def main():
    solution = Solution()

    # Example usage
    s = "YazaAay"
    result = solution.longestNiceSubstring(s)
    print(result)

if __name__ == "__main__":
    main()
