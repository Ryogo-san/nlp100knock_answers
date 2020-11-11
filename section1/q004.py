s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s_split=s.split()
ans={}
one=[1,5,6,7,8,9,15,16,19]

for i,word in enumerate(s_split):
    if i+1 in one:
        ans[word[:1]]=i+1
    else:
        ans[word[:2]]=i+1
    
print(ans)