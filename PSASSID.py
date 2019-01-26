#!/usr/bin/env python3
import sys, json, requests, hashlib, random, string
from collections import deque
from classes.n150_web_driver import n150_web_driver

SETTINGS_FILE = "n150_settings.json"
PASSWORD_MAX_LENGTH = 12
MAC_MAX_LENGTH = 6
PASSPHRASE_MAX_LENGTH = 63

def main():
    settings = read_settings(SETTINGS_FILE)

    driver = n150_web_driver(settings["ip_address"],
                             settings["password"],
                             settings["ssid"],
                             settings["passphrase"],
                             settings["mac"],
                             settings["time_out"],
                             settings["wireless_interface"])

    new_mac = generate_random_mac()
    new_password = generate_secure_password(PASSWORD_MAX_LENGTH)
    new_passphrase = generate_secure_password(PASSPHRASE_MAX_LENGTH)

    print("New Password Generated: " + new_password)
    print("New Mac Generated: " + new_mac)
    print("New Passphrase Generated: " + new_passphrase)

    driver.set_mac(new_mac)
    driver.set_password(new_password)
    driver.set_passphrase(new_passphrase)

    #write_settings(new_mac,new_password,new_passphrase)

def read_settings(settings_file_location):
    try:
        with open(settings_file_location, "r") as settings_location:
            settings = json.load(settings_location)
            return settings
    except Exception as e:
        print(e)
        return False
def write_settings(new_mac,new_password,new_passphrase):

    try:
        with open(SETTINGS_FILE,"w") as settings_location:
            settings = json.loads(settings_location)
            settings["password"] = new_password
            settings["mac"] = new_mac
            settings["passphrase"] = new_passphrase

            json.dump(settings,settings_location)
    except Exception as e:
        print(e)
        return False

def generate_secure_password(length):
    secure_password = ""

    ascii_lowercase = deque(string.ascii_lowercase)
    ascii_uppercase = deque(string.ascii_uppercase)
    ascii_symbols = deque(string.punctuation)

    ascii_list = [ascii_lowercase,ascii_uppercase,ascii_symbols]

    for x in range(length):
        random_ascii_list = ascii_list[random.randint(0,int(len(ascii_list))-1)]
        random_value = random.randint(0,int(len(random_ascii_list))-1)
        secure_password = secure_password + str(random_ascii_list[random_value])
        random_offset = random.randint(0,int(len(random_ascii_list))-1)
        random_ascii_list.rotate(random_offset)

    return secure_password

def generate_random_mac():
    random_mac = ""

    ascii_uppercase = deque(string.ascii_uppercase[:6])
    ascii_numbers = deque(string.digits[:9])

    ascii_list = [ascii_uppercase,ascii_numbers]

    for x in range(MAC_MAX_LENGTH):
        for x in range(2):
            random_ascii_list = ascii_list[random.randint(0,int(len(ascii_list))-1)]
            random_value = random.randint(0,int(len(random_ascii_list))-1)
            random_mac = random_mac + str(random_ascii_list[random_value])
            random_offset = random.randint(0,int(len(random_ascii_list))-1)
            random_ascii_list.rotate(random_offset)
        random_mac = random_mac + ":"

    random_mac = random_mac[:-1]
    return random_mac

main()