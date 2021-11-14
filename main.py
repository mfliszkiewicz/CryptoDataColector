from selenium import webdriver

url = "https://www.viewbase.com/exchange"
PATH = r"C:\Users\WONSZ\PycharmProjects\CryptoDataColector\drivers\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://www.viewbase.com/exchange")
print(browser.title)
browser.quit()
# ViewbaseExchangeFlow = requests.get(url).text

# soup = BeautifulSoup(ViewbaseExchangeFlow, 'lxml')
# tr_elements = soup.find_all('tr', class_='exchange_overview_row clickable-row')

# print(tr_elements)
