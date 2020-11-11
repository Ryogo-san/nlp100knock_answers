s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s=s.replace(",","")
s=s.replace(".","")
# s=re.sub("[,\.]","",s)でも可

s_split=s.split()
ans=[len(i) for i in s_split]

print(ans)