import instaloader
import csv
import re

data = instaloader.Instaloader()
username_data = ['katrinakarele', 'virat.kohli','baibarunce']

for username in username_data:
    profile = instaloader.Profile.from_username(data.context, username)
    scrapped_data = {
        "Username ": profile.username,
        "Full Name ": profile.full_name,
        "User ID ": profile.userid,
        "Number of Posts ": profile.mediacount,
        "Followers Count ": profile.followers,
        "Following Count ": profile.followees,
        "Profile pic URL ": profile.profile_pic_url,
        "Bio ": profile.biography,
        "External URL ": profile.external_url,
        "IGTV count ": profile.igtvcount,
    }
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_regex, profile.biography)

    if len(matches) > 0:
        print(matches[0])
        print(scrapped_data)
        filename = "Scrapper.csv"
        with open(filename, 'a', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(scrapped_data.keys())
            csvwriter.writerow(scrapped_data.values())
    else:
        pass

