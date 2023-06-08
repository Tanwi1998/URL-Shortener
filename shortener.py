import pyshorteners

link=input("Enter the link:")

shortener=pyshorteners.Shortener()

short_link=shortener.tinyurl.short(link)

print(short_link)
Additional content.
Additional content.