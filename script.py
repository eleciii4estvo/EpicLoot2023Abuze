import time
from selenium import webdriver
from selenium.webdriver.common.by import By

input('Перед тем как начать проверь!\n1. У тебя скачан хром и ты выполнил в нем авторизацию на сайте епиклут\n2. У тебя отключены все расширения в хроме\n3. Ты закрыл хром\nЕсли все это сделано - нажми Enter')

user = input("Введите имя пользователя Windows, которое указано в C:\Пользователи(по умолчанию - user)")
if(len(user)<2):
    user='user'

count = 0
try:
    while True:
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)

        url = 'https://epicloot.in/event'

        try: 
            print('Награды подоспели, забираем!')
            driver.get(url=url)
            time.sleep(2)
            try:
                driver.find_element(By.CSS_SELECTOR, '.header-auth__button-steam').click()
                time.sleep(2)
                driver.find_element(By.CLASS_NAME, 'btn_green_white_innerfade').click()
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, '.header-menu__item.battle-pass').click()
                print('Повторная авторизация прошла успешно!')
            except:
                print('Вход успешно выполнен')
            try:
                time.sleep(2)
                gifts = driver.find_element(By.CLASS_NAME, 'game-actions__online').text
                driver.find_element(By.CLASS_NAME, 'game-gift__take').click()
                print('Награда получена!')
                count +=1
                gifts = driver.find_element(By.CLASS_NAME, 'game-actions__online').text
                print(f'Всего наград: {gifts}')
                print(f'За время выполнения скрипта получено: {count}')
                print(f'Ждем час...')
            except:
                print('Видимо ты уже забрал награду( Жду час и забираю сам')
                print(f'Всего наград: {gifts}')
        except Exception as ex:
            print('Видимо ты не закрыл браузер... Попробуй еще раз, но перед этим закрой браузер. Если не поможет - напиши разработчику (контакты есть в гите)')
        finally:
            driver.close()
            driver.quit()
        for i in range(1,61):
            print(f'Осталось ждать:{61-i} минут', end='\r')
            time.sleep(60)  
except:
    print('Видимо ты не закрыл браузер или не выключил расширения\nПопробуй еще раз, но перед этим выполни все рекомендации, которые указаны в инструкции.\nЕсли не поможет - напиши разработчику (контакты есть в гите)')
    driver.close()
    driver.quit()    

  