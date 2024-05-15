# Algorithms and Data Structures - learning by doing
<br>
I recently took a technical test that I didn't do that well on so decided to take a more in-depth look, slowly, at some of these problems - the type found on platforms such as Leetcode that are based on common data structures and algorithms. I wanted to work through how to solve the problems, but also how to think through solving them, iterations, breaking down the problem, and improving efficiency.
<br>
I'll take one problem at a time and first of all write down how I initially plan to tackle it, then how I think through it and what I figure out along the way. Code will be written in Python. Table of contents will be added to as I solve the problems. I will be trying to solve these problems by myself, but if I have to look up how to write a portion of the solution I will make sure to include a reference.

## Contents
1. Roman Numeral Converter
2. Amount of 1s that appear in a digit

### Roman Numeral Converter
The whole idea behind this problem is that a function takes an integer value as input and returns a string that is the integer value in Roman Numeral form. My initial plan on how to tackle this is:
1. Map all unique Roman Numeral characters to their corresponding number (I, V, X, C, M etc.). I will have to look up a full table of Numerals as I can't name all of them off the top of my head.
2. Decompose the integer number into its composite parts (based on powers of 10), so for example, 17847 would bw 10000 + 7000 + 800 + 40 + 7. I am not sure how to do this, so will have to think about it.
3. Add to a string or build up a mutable array with the Roman Numerals based on these powers of ten.

I will probably need to alter these steps as I go along and find out what works and what doesn't, and I'll add to the README as I do.
#### Iteration One
Going well, I'd figured out how to get the number of digits, but then realised I will need to reverse the number. My plan for that probably none too efficient, but I will:
1. Convert the number to a string
2. Reverse it using a loop
3. Convert the characters back to integers when needed

I will come back to this later if I think of a more efficient method.
<br><br>
I have managed to now produce numbers up to 100, but it is unweidly in 19 lines, with 9 lines needed for every power of 10. I think I will add a helper function. 
<br><br>
I now can generate Roman Numerals up to 1000, and as I had hoped, a pattern has emerged. Each numerical argument () to the helper function just needs to keep being increased by powers of 10, which makes sense. So all I need do do is set up the base case, then multiply it by 10 every loop. I am going to have to stop there because Roman Numerals start requiring special characters once you get much higher than 1000. But the solution I have come up with would be easily scalable to larger numbers. I'd just need to add to the dictionary.
<br><br>
**References**<br>
[Roman Numeral Reference at Britannica](https://www.britannica.com/topic/Roman-numeral)

### Amount of 1s that appear in digits
I saw this question on Leetcode and thought it looked interesting. The difficulty level was listed as "hard". The idea is that, for any given number, find out how many times "1" appears in all numbers less than or equal to the number. So 13 is 6, because 1, 10, 11, 12, 13 (where 11 is counted twice as there are two 1s).<br>
How I plan to tackle this is:
1. Work out the mathematical pattern for a 1 appearing in a digit (I get the feeling powers of 10 will come into this one as well)
2. Work out how to filter and count the 1s, given the pattern
3. Count the 1s

Easy, right?<br>
So, thinking this through: for every block of 0-9 numbers, 1 will appear once. For every block of 10-19 numbers, 1 will appear 10 + 1 times, and for every block of 20-99, 1 will appear 8 * 1 times. Or to look at it another way, for each block of 0 - 99, 1 will appear (10 * 1) + (10 * 1) times. For each block 0 - 999, 1 will appear 10 * ((10 * 1) + (10 * 1)) + 100, with the multiplying by 10 being for all the times 0-99 appears, and the extra 100 being for the 100 numerals in the 100-199 range. For 0-9999, 1 will appear 10 * (10 * ((10 * 1) + (10 * 1)) + 100) + 1000.<br>
Hey presto, we have our pattern! To stop "counting" at a certain number, say if we are given the number 762, we only need to check each power of 10 for its position. So 2 > 1, therefore 1 has appeared. Drop the 2. in 60, 1 has appeard (6 * 1) + (10 * 1) times. Drop the 60. In 700, 1 has appeared 7 * ((10 * 1) + (10 * 1)) + 100.<br>
It gets a bit tricker if you stop in a 1s zone, so 182. Then you need to say it has appeared 1 * (10 * 1) + (8 * 1) + 82 times. I think...<br><br>
What I've learned so far, hours later: <br>
This was really tricky because having a certain power AND having the number start with 1 gave edge cases I hadn't bargained on. As long as the number doesn't start with 1, this is easy because you can account for all the 1s that have appeared with the rule I already mentioned. When the number starts with 1 and the rest is zeros, it gets even trickier because you have to work backwards, find out what the previous number was, and then just add 1. But I have solved it now, and without looking up any help. Not too bad for a student.