# Description:

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

# For example, when an array is passed like [19,5,42,2,77], the output should be 7.

# [10,343445353,3453445,3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    min2 = max(numbers)
    for num in numbers:
        if min1 < num and num < min2:
            min2 = num
    return min1 + min2



# Description:

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(string):
    seen = {}
    for letter in string:
        lower = letter.lower()
        if lower not in seen:
            seen[lower] = True
        else:
            return False
    return True



# Description:

# Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

# Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.

# For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

# Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

# Input

# The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

# Output

# Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

# Examples

# song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
#   # =>  WE ARE THE CHAMPIONS MY FRIEND

def song_decoder(song):
    # Remove all WUBs from string with str.split(), ignoring empty strs
    strip_wubs = [word for word in song.split('WUB') if word]
    # Join with spaces
    return ' '.join(strip_wubs)


# Description:

# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.


# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    words = map((lambda word: word[::-1] if len(word) >= 5 else word),
                sentence.split(' '))
    return ' '.join(words)