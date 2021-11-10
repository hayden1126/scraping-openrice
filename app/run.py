import requests
from bs4 import BeautifulSoup

currentPage = 1

def main():
    #https://www.openrice.com/zh/hongkong/restaurants?amenityId=1015&districtId=2010&page=2
    url = "https://www.openrice.com/zh/hongkong/restaurants/district/"
    districtName = "旺角"
    cateringType = "小食店"

    # districtName = districtName.encode('utf-8')
    # cateringType= cateringType.encode('utf-8')

    fullURL = "{}{}?what={}&page={}".format(url, districtName, cateringType, currentPage)
    fullURL = "https://unwire.hk/parent_category/product-review/page/2/"
    print(fullURL)
    res = requests.get(fullURL, headers={"content-type":"text"})#.content()
    print(res)
    # soup = BeautifulSoup(res, "html.parser")
    # print(soup)


if __name__ == "__main__":
    # execute only if run as a script
    main()