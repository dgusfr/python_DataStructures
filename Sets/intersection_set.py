text_one = set(input("Enter the first text:").lower().split())
text_two = set(input("Enter the secound text:").lower().split())


union_text = text_one.intersection(text_two)
print(f"Words in both texts: {union_text}")
