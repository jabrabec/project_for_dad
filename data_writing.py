#!/usr/bin/env python

import random
import time

while True:
    with open('data/temp.txt', 'w') as file:
        file.write("{}\n".format(random.random()))
    time.sleep(0.25)
