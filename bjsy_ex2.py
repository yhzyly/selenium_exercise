# 给你一个字符串，如果一个字符在它前面k个字符中已经出现过了，就把这个字符改成’-’
def replace_chars(string, k):
    result = ""
    seen_chars = []
    for i, char in enumerate(string):
        if char in seen_chars[-k:]:
            result += "-"
        else:
            result += char
        seen_chars.append(char)
    return result


input_string = input("请输入字符串：")
k = int(input("请输入k值："))
output_string = replace_chars(input_string, k)
print("Output:", output_string)
