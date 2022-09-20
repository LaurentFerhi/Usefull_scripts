import hashlib
import getpass

upper = list(range(65,91))
lower = list(range(97,123))
digit = list(range(48,58))
special = [ord(c) for c in '!#@;:$%-_()']
authorized = upper+lower+digit+special

user_in = getpass.getpass('Write input:')
size_in = getpass.getpass('Write size:')
user_in += size_in
size = int(size_in)

valid = False

while not valid:
    
    # Generate SHA512 hash
    user_hash = hashlib.sha512(str.encode(user_in)).hexdigest()

    # Decompose in groups of 3
    i, j = divmod(len(user_hash), 6)
    l_hash = [user_hash[:j]] + [user_hash[j+(i-1)*3:j+i*3] for i in range(1,i+1)]

    # Scrap 1st group (which value will be too low)
    l_hash = l_hash[1:]

    # convert to ascii in authorized range
    l_hash_ascii = [int(x, 16)%(122-33) + 33 for x in l_hash][:size]

    # check for characters
    if any(x not in authorized for x in l_hash_ascii) \
    or not any(i in upper for i in l_hash_ascii)\
    or not any(i in lower for i in l_hash_ascii)\
    or not any(i in digit for i in l_hash_ascii)\
    or not any(i in special for i in l_hash_ascii):
        user_in += '0'
    
    else:
        valid = True

print('Output: '+''.join([chr(s) for s in l_hash_ascii]))