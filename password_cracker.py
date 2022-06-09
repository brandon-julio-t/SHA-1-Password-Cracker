import hashlib


def crack_sha1_hash(hash, use_salts=False):
    passwords = read_all_lines_in_file('top-10000-passwords.txt')
    salts = read_all_lines_in_file('known-salts.txt')

    for password in passwords:
        result = ''
        
        if use_salts:
            for salt in salts:
                possibilities = [
                    salt + password,
                    password + salt,
                    salt + password + salt
                ]

                for possibility in possibilities:
                    result = hashlib.sha1(possibility.encode()).hexdigest()
                    if (hash == result):
                        return password
        else:
            result = hashlib.sha1(password.encode()).hexdigest()
            if (hash == result):
                return password
        
    return 'PASSWORD NOT IN DATABASE'

def read_all_lines_in_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip())
    return data
