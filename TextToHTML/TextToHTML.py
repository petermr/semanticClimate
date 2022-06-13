txt = open("/Users/kaartik/Desktop/sometxt.txt", "r") #txt has the content of the file that we want to convert
with open("versionhtml.html", "w") as e: # making new file to write html code in
    for lines in txt.readlines():
        e.write(lines + "<br>\n")  # deals with paragraphing
