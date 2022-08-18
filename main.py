from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
with webdriver.Chrome(PATH) as driver:
    link = "https://lubimyczytac.pl/profil/1924129/kaka10052/biblioteczka/lista?shelfs=6745969"
    driver.get(link)
    with open("List_of_books.txt", "w") as file:
        try:
            actions = ActionChains(driver)
            accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            actions.move_to_element(accept_cookies).click().perform()
            actions.reset_actions()
            num_of_pages = int(driver.find_element(By.CLASS_NAME, "paginationList__info")
                               .find_element(By.TAG_NAME, "span").text)
            for page in range(num_of_pages):
                sleep(6)
                books_list = driver.find_elements(By.CLASS_NAME, "authorAllBooks__single")
                for book_div in books_list:
                    book_name = book_div.find_element(
                        By.CLASS_NAME, "authorAllBooks__singleTextTitle").text
                    book_author = book_div.find_element(
                        By.CLASS_NAME, "authorAllBooks__singleTextAuthor").\
                        find_element(By.TAG_NAME, "a").text
                    if book_author == "Thích Nhất Hạnh":
                        book_author = "Thich Nhat Hanh"
                    line = "\"{}\" - {}\n".format(book_name, book_author)
                    file.write(line)
                if page < num_of_pages-1:
                    next_page_a = driver.find_element(By.CLASS_NAME, "next-page")
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    actions.move_to_element(next_page_a).click().perform()
                    actions.reset_actions()

        finally:
            driver.quit()

