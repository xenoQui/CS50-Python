# input into a string

extn = input("File name: ").strip().lower()


# print depending on extension

if extn.endswith(".gif"):
    print("image/gif")
elif extn.endswith(".jpeg") or extn.endswith(".jpg"):
    print("image/jpeg")
elif extn.endswith(".png"):
    print("image/png")
elif extn.endswith(".pdf"):
    print("application/pdf")
elif extn.endswith(".txt"):
    print("text/plain")
elif extn.endswith(".zip"):
    print("application/zip")
elif extn.endswith(".bin"):
    print("application/octet-stream")
else:
    print("application/octet-stream")
