# 11. Given a string consisting of words separated by spaces. Determine how many
# words it has. To solve the problem, use the method count.


any_words = input("Enter a sentence: ")
# count = 1
# for i in any_words:
#     if i == " ":
#         count+=1

# print(count)
count = any_words.count(" ")
print(count+1)