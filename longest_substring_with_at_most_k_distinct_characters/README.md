## 340. Longest Substring with At Most K Distinct Characters

Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

Complexity: medium

Solution: \
Sliding window. Iteratively move right bound of the window. Move the left if current symbol set is bigger than k.

Complexity: O(n), as we move window bounds only in one direction

Memory: O(k), as we remember current k symbols

tags:
- sliding window
- two pointers
- arrays
- strings