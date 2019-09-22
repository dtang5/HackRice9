with open("../HackRice9_Dataset/small_reviews_to_stars.txt") as f:
    for line in f:
        print float(line[-5:-2])
        print line[2:-7]
