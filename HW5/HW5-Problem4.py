
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 00:19:31 2022

@author: shayla
"""

import re
with open("contribs.txt",  "r") as file:
    file.readline()
    p = re.compile(r'\d+')
    p.findall(str(file))
    print(file.readline())
    print(p.findall(str(file)))

    
