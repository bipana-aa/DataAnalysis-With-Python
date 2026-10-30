def analyze_username(username):
    username = username.strip().lower()
    total_characters = len(username.replace(" ", ""))
    vowels = sum(1 for ch in username if ch in "aeiou")

    if total_characters < 5:
        print("Username is too short.")
    elif username.isalpha():
        print("Username contains only alphabets.")
    else:
        print("Username contains mixed characters.")

    return (total_characters, vowels)


print(analyze_username("  BipanaKhadka  "))
print(analyze_username("ab1"))
print(analyze_username("user_123"))