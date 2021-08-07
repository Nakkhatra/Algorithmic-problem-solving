# Algorithmic-problem-solving
Here I will be uploading the algorithmic problem solving solutions by me that I practise from leetcode and hackerrank.


Problem 1: Find out number of nearly similar rectangles from a list where rectangle sides are given.

Solution: Here I have used two different approaches, one is naive and the other is optimized. The naive approach will use two loops: The outer loop will iterate through the elements of the list (rectangle sides) and the inner loop will iterate from the next element of the first loop to the end of the list. And in each iteration it will check if the ratio of the first sides of each rectangle equals to the ratio of the second sides or not. If same, then it will count a pair and will finally return the number of pairs at the end.

In the optimized solution, we don't actually need to iterate for all the elements. For example, if we find two rectangle pairs as nearly similar (i.e.: ([5,9],[15,18]) and ([5,9],[20,36])) then each of the other rectangles will also be nearly similar to each other. So, we can say that we have got three pairs of rectangles (3C2=3). Now we can cross them out from the list to avoid checking further in the next iteration with the help of a boolean list called check. We will add true if we get a pair and want to cross that off the list. So it reduces the runtime greatly!

stresstest function: Here I have created a function that will help us to check if our optimized solution is bug free. As we do believe that our brute force/non optimized solution should be correct, so we check our optimized results against that one for bug testing. Here I have created random inputs in range of the constraints given and run both functions, if the results are similar, then it will print 'ok'. I have looped for upto 100 'ok's. You can do more if you want.

timecounter function: In this function we use timeit module to calculate the runtime of both functions to check if our optimized algorithm really works faster. After checking the total time for 1000 iterations, I found out that our optimized algorithm is about 262 times faster!
