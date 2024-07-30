import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon'
response = requests.get(url)
response.encoding = 'utf-8'

# 상태 코드 확인
if response.status_code == 200:
    print("웹페이지가 성공적으로 로드되었습니다.")
else:
    print(f"웹페이지 로드에 실패했습니다. 상태 코드: {response.status_code}")

html = response.text
soup = BeautifulSoup(html, 'html.parser')

webtoon = []

for i in range(0,7):
    webtoon.append(soup.select(f"#container > div.component_wrap.type2 > div.WeekdayMainView__daily_all_wrap--UvRFc > div:nth-child({i}) > ul > li"))

# 데이터 로드 확인
if len(webtoon) > 0:
    print("키노라이츠 랭킹 데이터가 성공적으로 로드되었습니다.")
else:
    print("키노라이츠 랭킹 데이터를 로드하는 데 실패했습니다.")

# 확인용 출력
print(webtoon)
#container > div.component_wrap.type2 > div.WeekdayMainView__daily_all_wrap--UvRFc > div:nth-child(6) > ul > li:nth-child(3) > div > a > span
#container > div.component_wrap.type2 > div.WeekdayMainView__daily_all_wrap--UvRFc > div:nth-child(4) > ul > li:nth-child(1) > div > a > span > span