from collections import Counter
init_d = Counter({
    "closed_time": Counter(
        {'mon': Counter({str(x): 0 for x in range(24)}), 'tue': Counter({str(x): 0 for x in range(24)}),
         'wed': Counter({str(x): 0 for x in range(24)}), 'thu': Counter({str(x): 0 for x in range(24)}),
         'fri': Counter({str(x): 0 for x in range(24)}), 'sat': Counter({str(x): 0 for x in range(24)}),
         'sun': Counter({str(x): 0 for x in range(24)})}),
    "created_time": Counter(
        {'mon': Counter({str(x): 0 for x in range(24)}), 'tue': Counter({str(x): 0 for x in range(24)}),
         'wed': Counter({str(x): 0 for x in range(24)}), 'thu': Counter({str(x): 0 for x in range(24)}),
         'fri': Counter({str(x): 0 for x in range(24)}), 'sat': Counter({str(x): 0 for x in range(24)}),
         'sun': Counter({str(x): 0 for x in range(24)})})
})
print(init_d)

new_dict = {outer_key: Counter({str(x): 0 for x in range(24)}) for outer_key in
            Counter({week_day: Counter() for week_day in ["mon", "tue", "wen", "thu", "fri", "sat", "sun"]})}
print(new_dict)

