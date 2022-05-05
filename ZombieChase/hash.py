import hashlib as h
m = h.sha256()
m.update(b"hi")
message = m.hexdigest()

with open("authentication.txt","w") as f:
	f.write(message)
