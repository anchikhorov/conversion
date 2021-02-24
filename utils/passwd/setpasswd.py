#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyring
import config
import getpass

p = getpass.getpass()
host = config.getHost()
user = config.getUser()
keyring.set_password(host,user,p)