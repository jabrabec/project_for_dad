#!/usr/bin/env python

import random
import time

while True:
    with open('data/temp.txt', 'w') as file:
        file.write("{}".format(random.randint(1000, 9999)))
    time.sleep(0.25)
