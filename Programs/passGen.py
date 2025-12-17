import random 
import string
import time

# Initialize password variable
PASS_DONE = []

# COMPLEXITY OPTION 1 - Letters and numbers only
def pass_letter_num():
    global PASS_DONE

    usr_pass_len = input("Enter a preferred length for your password: ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)

    char_pool_lower = string.ascii_lowercase
    char_pool_upper = string.ascii_uppercase
    int_pool = string.digits
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)
        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)
        random_int = random.choice(int_pool)
        PASS_DONE.append(random_int)
    else:
        pass
    # Print generated password
    print(''.join(PASS_DONE))


# COMPLEXITY OPTION 2 - Uppercase letters only
def pass_letter_up():
    global PASS_DONE

    usr_pass_len = input("Enter a preferred length for your password: ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_upper = string.ascii_uppercase
    while len(PASS_DONE) < usr_pass_len:
        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)
    else:
        pass
    # Print generated password
    print(''.join(PASS_DONE))


# COMPLEXITY OPTION 3 - Lowercase letters only
def pass_letter_low():
    global PASS_DONE

    usr_pass_len = input("Enter a preferred length for your password: ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_lower = string.ascii_uppercase
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)
    else:
        pass
    # Print generated password
    print(''.join(PASS_DONE))


# COMPLEXITY OPTION 4 - Letters and special characters only
def pass_letter_wild():
    global PASS_DONE

    usr_pass_len = input("Enter a preferred length for your password (minimum: 3): ")
    print('=' * 60)
    usr_pass_len = int(usr_pass_len)
    char_pool_lower = string.ascii_lowercase
    char_pool_upper = string.ascii_uppercase
    char_pool_wild = string. punctuation
    while len(PASS_DONE) < usr_pass_len:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)
        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)
        random_wild = random.choice(char_pool_wild)
        PASS_DONE.append(random_wild)    
    else:
        pass
    print(''.join(PASS_DONE))

def pass_gen_all():
    global PASS_DONE

    wild_char = string.punctuation
    int_pool = string.digits
    char_pool_lower = string.ascii_lowercase
    char_pool_upper = string.ascii_uppercase

    while len(PASS_DONE) < 12:
        random_low = random.choice(char_pool_lower)
        PASS_DONE.append(random_low)

        random_int = random.choice(int_pool)
        PASS_DONE.append(random_int)

        random_up = random.choice(char_pool_upper)
        PASS_DONE.append(random_up)

        random_wild = random.choice(wild_char)
        PASS_DONE.append(random_wild)
    else:
        pass
    print(''.join(PASS_DONE))


def main():
    print('=' * 60) 
    print("--- Password Complexity Options ---")
    print('=' * 60)
    print("Only letters and numbers - 1")
    print("Only uppercase letters - 2")
    print("Only lowercase letters - 3")
    print("Only letters and special characters - 4")
    print("Use all available parameters (most complex and secure) - 5")
    print('=' * 60) 
    usr_pass_param = input("Enter password complexity parameter (1-5): ")
    usr_pass_param = int(usr_pass_param)
    print('=' * 60)
    try:
        if usr_pass_param == 1:
            pass_letter_num()
        elif usr_pass_param == 2:
            pass_letter_up()
        elif usr_pass_param == 3:
            pass_letter_low()
        elif usr_pass_param == 4:
            pass_letter_wild()
        elif usr_pass_param == 5:
            pass_gen_all()
        else:
            print('Exiting Program...')
            time.sleep(0.5)
            return
    except ValueError:
        print("INVALID INPUT!")
        

if __name__ == '__main__':
    main()