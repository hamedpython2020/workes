text = "i love python"

l_text = text.split()
print(l_text)
# for i in l_text :
#     n = i[-1:-len(i)]
#     print(n)
for i in range(len(l_text)):
    print(l_text[i][::-1])  