#! /usr/bin/env python3

import getpass
print("Print Current Username: {}".format(getpass.getuser()))

import os
print("Print Current Username: {}".format(os.getlogin()))
