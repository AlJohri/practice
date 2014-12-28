import requests, lxml.html, re, csv

posts = []

regex = re.compile(r"Set (\d+)")
other_counter = 1

for i in range(12, 0, -1):
    response = requests.get("http://www.geeksforgeeks.org/tag/amazon/page/%d/" % i)
    doc = lxml.html.fromstring(response.content)
    # post-date
    for item in doc.cssselect(".post-info"):
        title = item.cssselect('.post-title a')[0].text.replace("Amazon interview Experience", "").replace("Amazon Interview Experience", "").replace("Amazon Interview Questions", "").replace("Amazon Interview", "").replace(" | ", "").strip()
        url = item.cssselect('.post-title a')[0].get('href')
        date = item.cssselect('.post-date')[0]
        matches = re.findall(regex, title)
        if matches:
            posts.append(("set" + str(matches[0]).zfill(3), title, url, date.text))
        else:
            posts.append(("other" + str(other_counter).zfill(3), title, url, date.text))
            other_counter += 1
        print(posts[-1])

f = open("posts.csv", "w")
writer = csv.writer(f)
writer.writerow(["Title", "URL", "Date"])
for post in posts:
    writer.writerow(post[1:])
f.close()