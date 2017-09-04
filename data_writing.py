#!/usr/bin/env python

import random
import time

while True:
    with open('data/temp.txt', 'w') as file:
        file.write("{}".format(random.randint(1, 1000)).zfill(4))
    time.sleep(0.25)
