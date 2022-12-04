"""
leetcode link: https://leetcode.com/problems/reverse-words-in-a-string/
Given a sentence,
reverse the order of its words without affecting the order of letters within a given word.

Constraints:
    - The length of the sentence should be equal to or more than one character or word.
    - Sentence contains English uppercase and lowercase letters, digits, and spaces.
    - 1 <= sentence.length <= 1e4
    - The order of the letters within a word is not to be reversed.

Test Cases:
    - “The quick brown fox jumped over a lazy dog” -> “dog lazy a over jumped fox brown quick The”
    - “Educative Answers” -> “Answers Educative”
    - "a" -> "a" 
    - "Mohamed Mostafa" -> "Mostafa Mohamed"
"""

def reverse_words(sentence: str) -> str:
    words = sentence.split()
    l, r = 0, len(words) - 1
    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
        
    return " ".join(words)

# Run the function with the above test cases
print(
    reverse_words("The quick brown fox jumped over a lazy dog"),
    reverse_words("Educative Answers"),
    reverse_words("a"),
    reverse_words("Mohamed Mostafa"),
    sep="\n"
)