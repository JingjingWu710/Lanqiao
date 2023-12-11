def findRadius(houses:list,heaters:list):

    houses.sort()
    heaters.sort()
    # 建立一个表格储存离所有房子最近的供暖器，以供最后选出最大的半径
    radius =[]
    # 遍历所有房子，用二分查找法查找离每个房子近的供暖器
    for i in houses:
        l = 0
        r = len(heaters)-1
        while l < r:
            mid = (l + r) // 2
            # 已经有了一个供暖器在这个房子里
            if heaters[mid] == i:
                radius.append(0)
                break
            # 别的情况
            elif heaters[mid] > i:
                r = mid
            else:
                l = mid + 1
        # 但是只是找出了相对靠近房子的供暖器，附近的供暖器有可能离房子更近
        # 先防止l是heaters列表的头尾
        if len(heaters) == 1:
            return max(abs(heaters[l]-min(houses)),abs(heaters[l]-max(houses)))
        # 如果l是heaters的最左边
        elif l == 0:
            radius.append(min(abs(heaters[l]-i),abs(heaters[l+1]-i)))
        # 如果它在heaters列表最后一个，往回找
        elif l == len(heaters) - 1 or heaters[l] > i:
            radius.append(min(abs(heaters[l]-i),abs(heaters[l-1]-i)))
        else:
            radius.append(min(abs(heaters[l]-i),abs(heaters[l+1]-i)))
    print(radius)
    return max(radius)
    # # 如果只有一个供暖器，检查它到房子两端的最大距离就好了
    # if len(heaters) == 1:
    #     return max(abs(heaters[0]-min(houses)),abs(heaters[0]-max(houses)))
    # else:
    #     # 如果所有供暖器在房子左边，只用算最靠近第一个房子的供暖器到最远的房子的距离
    #     if min(houses) >= max(heaters):
    #         return max(houses) - max(heaters)
    #     # 反之亦然
    #     elif max(houses) <= min(heaters):
    #         return min(heaters) - min(houses)
    #     # 其它情况：
    #     while l < r:
    #         if len(heaters) == 2:
    #             if max(heaters) >= max(houses)+len(houses)-1:
    #                 return max(houses) - min(heaters)
    #             else:
    #                 return (max(heaters)-min(heaters)) // 2
    #         heaters_m = (l+r)//2
    #         if heaters[heaters_m] >= houses[houses_m]:
    #             r = heaters_m - 1
    #         else:
    #             l = heaters_m
    #     print(houses[houses_m],heaters[l])
    #     if heaters[l] != heaters[0] and heaters[l] != heaters[-1]:
    #         return min([abs(heaters[l]-houses[houses_m]),abs(heaters[l-1]-houses[houses_m]),abs(heaters[l+1]-houses[houses_m])])
    #     elif l == 0:
    #         return heaters[l] - min(houses)
    #     else:
    #         return max(houses) - heaters[l]
        

print(findRadius([63,132,195,224,263,344,361,449,480,528,593,641,662,726,754,841,882,929,976,1017,1054,1141,1197,1211,1261,1321,1365,1446,1496,1513,1564,1619,1699,1711,1765,1830,1860,1938,1995,2008,2085,2123,2198,2213,2254,2347,2378,2425,2464,2503,2582,2618,2658,2724,2764,2800,2876,2902,2979,3003,3053,3149,3153,3221,3283,3346,3367,3428,3489,3504,3586,3648,3659],
                 [21,49,75,88,112,126,142,170,192,207,227,243,273,280,310,338,358,378,390,404,429,440,471,498,507,526,543,562,598,604,636,654,670,696,700,732,751,763,795,800,832,847,860,889,910,925,952,968,997,1015,1032,1054,1061,1092,1102,1127,1150,1175,1197,1214,1231,1246,1262,1284,1313,1321,1358,1376,1397,1407,1429,1445,1464,1489,1511,1531,1554,1563,1584,1604,
                   1620,1656,1670,1683,1703,1722,1746,1774,1789,1807,1829,1855,1879,1892,1908,1934,1947,1967,1991,2008,2026,2043,2075,2094,2117,2127,2157,2175,2192,2215,2220,2254,2279,2285,2309,2328,2342,2376,2391,2406,2422,2445,2461,2480,2519,2525,2543,2564,2588,2609,2621,2656,2661,2691,2710,2727,2750,2762,2799,2816,2833,2842,2861,2885,2905,2928,2957,2979,2989,3005,
                   3030,3059,3073,3099,3114,3139,3154,3169,3185,3200,3239,3248,3266,3295,3303,3322,3345,3371,3385,3408,3428,3457,3461,3497,3508,3534,3548,3570,3583,3618,3622,3642,3671,3699,3703,3720,3746,3764,3787,3802,3836,3850,3866,3887,3906,3922,3940,3978,3993,4012,4035,4040,4071,4090,4107,4133,4143,4167,4180,4213,4229,4259,4265,4291,4308,4324,4353,4373,4385,4404,4437,4452,4462,4495,4504,4538,4548,4561,4594,4616,4628,4648,4679,4692,4718,4722,4756,4766,4794,4801,4820,4843,4861,4894,4911,4928,4950,4960,4984,5007,5035,5041,5066,5085,5107,5137,5145,5171,5197,5208,5225,5245,5267,5291,5310,5336,5352,5368,5391,5400,5428,5440,5470,5492,5517,5524,5543,5561,5582,5601,5626,5652,5675,5697,5717,5733,5754,5769,5782,5813,5821,5852,5860,5899,5907,5924,5958,5963,5986,6009,6023,6044,6071,6094,6104,6130,6155,6173,6192,6208,6225,6257,6273,6299,6302,6336,6346,6368,6380,6412,6438,6443,6474,6482,6503,6522,6559,6579,6590,6619,6633,6652,6677,6689,6702,6730,6746,6779,6786,6812,6839,6848,6875,6887,6911,6934,6955,6961,6989,7018,7035,7046,7079,7090,7119,7129,7141,7168,7183,7217,7221,7244,7270,7281,7319,7320,7344,7375,7399,7401,7427,7446,7477,7483,7517,7537,7559,7568,7584,7618,7632,7648,7666,7694,7708,7720,7741,7779,7789,7805,7821,7850,7875,7898,7905,7932,7956,7977,7992,8019,8033,8059,8078,8094,8115,8126,8145,8165,8180,8203,8221,8240,8269,8289,8305,8327,8358,8364,8399,8403,8422,8442,8476,8487,8500,8521,8551,8566,8581,8605,8629,8659,8675,8681,8705,8724,8752,8761,8784,8819,8829,8852,8869,8892,8904,8938,8958,8975,8997,9005,9036,9059,9063,9086,9111,9122,9154,9172,9187,9207,9230,9247,9278,9292,9316,9332,9355,9370,9386,9409,9425,9449,9471,9480,9511,9531,9552,9560,9592,9607,9639,9640,9666,9683,9713,9728,9759,9776,9780,9816,9838,9851,9865,9898,9911,9926,9955,9975,9995,10018,10030,10040,10065,10088,10118,10131,10149,10168,10182,10205,10237]))