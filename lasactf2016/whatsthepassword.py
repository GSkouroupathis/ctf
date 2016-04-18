
def get_passwords(textFile):
    with open(textFile) as f:
        passwords = map(lambda x:x.replace('\n',''), f.readlines())
        return passwords

def solve_it(passwords):
    finalPwd = passwords[0]

    for pwd in passwords[1:]:
        startIndex = 0
        for char in pwd:


if __name__ == "__main__":
    passwords = get_passwords('/Users/george/Downloads/Logins.txt')
    solve_it(passwords)
