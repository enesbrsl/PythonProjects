def count(sub,s):
    count = 0
    for i in range(len(s)):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count
count("is", "missipissi")
#%%
def remove(sub, s):
    new_s=s.replace(sub,"",1)
    return new_s
remove("an","banana")
        