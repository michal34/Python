# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:24:51 2022

@author: Michal
"""
n = int(input())

old_ranges = [(0, 1)]

for i in range(n):
    new_ranges = []
    
    for przedzial in old_ranges:
        j = przedzial[0]
        k = przedzial[0] + (1/3) * (przedzial[1] - przedzial[0])

        n = przedzial[0] + (2/3) * (przedzial[1] - przedzial[0])
        m = przedzial[1]

        nowy_przedzial1 = (j, k)
        nowy_przedzial2 = (n, m)
        new_ranges.append(nowy_przedzial1)
        new_ranges.append(nowy_przedzial2)
    old_ranges = new_ranges
    
print(old_ranges)