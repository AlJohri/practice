import requests, lxml.html, re, csv, datetime
from dateutil.parser import parse

posts = []

regex = re.compile(r"Set (\d+)")
other_counter = 1

for i in range(12, 0, -1):
    response = requests.get("http://www.geeksforgeeks.org/tag/amazon/page/%d/" % i)
    doc = lxml.html.fromstring(response.content)

    for item in doc.cssselect(".post-info"):
        title = item.cssselect('.post-title a')[0].text.replace("Amazon interview Experience", "").replace("Amazon Interview Experience", "").replace("Amazon Interview Questions", "").replace("Amazon Interview", "").replace("[TopTalent.in] ", "").replace(" | ", "").strip()
        title = (title[:70] + '..') if len(title) > 70 else title
        url = item.cssselect('.post-title a')[0].get('href')
        title_url = "[%s](%s)" % (title, url)
        
        try:
            date = parse(item.cssselect('.post-date')[0].text)
            datestr = date.strftime("%-m-%-d-%Y")
        except:
            date = None
            datestr = ""

        matches = re.findall(regex, title)
        if matches:
            posts.append(("set" + str(matches[0]).zfill(3), title_url, datestr, date))
        else:
            posts.append(("other" + str(other_counter).zfill(3), title_url, datestr, date))
            other_counter += 1

        inner_response = requests.get(url)
        inner_doc = lxml.html.fromstring(inner_response.content)
        filename = "content/" + posts[-1][0] + ".html"
        print(filename)
        with open(filename, "w") as f:
            content = lxml.html.tostring(inner_doc.cssselect("#post-content")[0])
            f.write(content.decode('utf-8'))

        print(posts[-1])

mindate = datetime.datetime(datetime.MINYEAR, 1, 1)
posts = sorted(posts, key=lambda x: x[3] or mindate, reverse=True)

f = open("posts.csv", "w")
writer = csv.writer(f)
writer.writerow(["Title", "Date"])
for post in posts:
    writer.writerow(post[1:3])
f.close()