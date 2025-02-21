words = ["has","kills."]
with open("lazy type\lazy.txt","r") as f, open("lazy type\lazy2.csv", "w+") as f2:
    f2.write("name,kills\n")
    for i in f:
        update1 = i.replace("kills.","")
        update2 = update1.replace("has",",")
        update3 = update2.replace(" ","")
        f2.write(update3)

