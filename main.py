import random
import os


if __name__ == "__main__":
    log_lvl = 2
    size = 2048
    original_data = "Hello, World!"
    



how_manny_see = 100
if log_lvl == 0:
    how_manny_see = 1
elif log_lvl == 2:
    how_manny_see = 1000

def test_print(message, lvl=1):
    if __name__ == "__main__":
        if log_lvl <= lvl:
            print(message)
            


# Ez ai irta nekem (is_prime fuggvenyt)
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # n-1 = d * 2^r formára hozás
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # tesztelés
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def make_random_bits():
    test_print("make_random_bits", 0)
    return "".join(random.choice(["0", "1"]) for i in range(size))
        
def convert_to_byte(data):
    test_print("convert_to_byte()", 0)
    return int(data, 2)

def get_prime_number(they_wont_be=[]):
    test_print("get_prime_number()", 2)
    try_number = 0
    while True:
        try_number += 1
        random_bits = make_random_bits()
    
        byte = convert_to_byte(random_bits)

        if is_prime(byte) and byte not in they_wont_be:
            test_print(f"megvan {byte}", 0)
            return byte
        
        if try_number % how_manny_see == 0:
            test_print(f"Make Prime number... {try_number} -")



def get_two_prime_number():
    test_print("")
    test_print("get_two_prime_number()")
    prime_numbers = []
    while len(prime_numbers) <= 1 :
            test_print(prime_numbers, 0)
            prime_numbers.append(get_prime_number(prime_numbers))
            test_print(f"Make Prime number... {len(prime_numbers)}/2 ----|")
    
    test_print(prime_numbers, 0)
    return prime_numbers

def get_e(En):
    test_print("get_e()")
    test_print("get_e()", 0)
    while True:
        prime = get_prime_number()
        if prime % En != 0:
            return prime



def get_keys_with_n(primes):
    test_print("")
    test_print("get_keys_with_n()", 0)

    n = primes[0] * primes[1]
    En = (primes[0] - 1) * (primes[1] - 1)

    e = get_e(En)
    test_print(e, 0)

    try:
        d = pow(e, -1, En)
    except:
        test_print("ERROR get_keys_with_n() and I dont know what!!!! /////////////////// ", 2)
        return None


    test_print(d, 0)

# e = publikus key | d = private key
    return [n, e, d]


    

#------------------------------------------------------

def make_to_byte(data):
    return [ord(c) for c in data]



def counting(n, a, m):
    try:
        return pow(m, a, n)
    except:
        return None
    
def convert_from_byte(byte_data):
    return "".join(chr(c) for c in byte_data)

def secret(byte_data, keys):
    test_print("secret()")
    
    secret_data = []
    for i in byte_data:
        counting_data = counting(keys[0], keys[1], i)
        secret_data.append(counting_data)
        test_print(f"[Nice] {i} --> {counting_data}", 0)

    return secret_data

byte_data_test = make_to_byte(original_data)
def make_sure_its_working(keys):
    test1 = [keys[0], keys[1]]
    test2 = [keys[0], keys[2]]
    secret_data1 = secret(byte_data_test, test1)
    if secret_data1 is not None:
        secret_data2 = secret(byte_data_test, test2)
        if secret_data2 is not None:
            decode_data1 = secret(secret_data1, test2)
            if convert_from_byte(decode_data1) == original_data:
                decode_data2 = secret(secret_data2, test1)
                if convert_from_byte(decode_data2) == original_data:
                    return True
                else:
                    test_print("[ERROR] 4 Something was WRONG and I dont know what!!! ------_______++++++++======", 2)
  

            
            else:
                 test_print("[ERROR] 3 Something was WRONG and I dont know what!!! ------_______++++++++======", 2)
  

        else: 
             test_print("[ERROR] 2 Something was not prime ------_______++++++++======", 2)

    else:
        test_print("[ERROR] 1 Something was not prime ------_______++++++++======" , 2)
    
    return False

def make_keys_run():
    test_print("make_keys_run()")
    while True:
        two_prime_numbers = get_two_prime_number()
        
        keys = get_keys_with_n(two_prime_numbers)
        if keys is None:
            continue
        
        # make a test!
        if make_sure_its_working(keys):
            break
  
    return keys


if __name__ == "__main__":
    for i in range(100):
        test_print(f"test{i}", 3)

        byte_data = make_to_byte(original_data)

        keys = make_keys_run()

        secret_data = secret(byte_data, [keys[0], keys[1]])

        decode = secret(secret_data, [keys[0], keys[2]])

        test_print(convert_from_byte(decode))



