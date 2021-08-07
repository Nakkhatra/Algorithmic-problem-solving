# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 04:14:32 2021

@author: snakk
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength= 0
        sub=""
        
        while sub!= s: 
            for string in s:
                if string not in sub: 
                    sub+=string
                    
                else:
                    if len(sub)>maxlength:
                        maxlength= len(sub)
                    sub=""
                    s= s[1:]
                    break

            if maxlength>= len(s):
                break
                
        if len(sub)>maxlength:
            maxlength= len(sub)
        
        return maxlength