#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keyring
import config

host = config.getHost()
user = config.getUser()
p = keyring.get_password(host,user)
#import decrypt

#p = decrypt.decrypt_message()
print(p)