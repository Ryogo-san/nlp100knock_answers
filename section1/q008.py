def cipher(s):
    rep=[chr(219-ord(x)) if x.islower() else x for x in s]
    return ''.join(rep)

message="This is a pen"
message=cipher(message)
print("暗号化:",message)
message=cipher(message)
print("復号化:",message)