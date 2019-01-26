#!/usr/bin/env python3
import requests, json

class n150_web_driver:
    def __init__(self,ip_address,password,ssid,passphrase,mac,time_out,wireless_interface):
        self.ip_address = ip_address
        self.password = password
        self.ssid = ssid
        self.passphrase = passphrase
        self.mac = mac
        self.time_out = time_out
        self.wireless_interface = wireless_interface

    def set_password(self, new_password):
        self.password = new_password
    def set_passphrase(self, new_passphrase):
        self.passphrase = new_passphrase
    def set_mac(self, new_mac):
        self.mac = new_mac
