from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import  datetime , timezone , timedelta
from selenium.webdriver.common.action_chains import ActionChains

## list of symbols ##
our_symbols = ['SPX','NVDA','ASTS','PANW','VKTX','SPY']

## list of scraped twitter accounts ##
twitter_accounts = [
        'TriggerTrades', 'RoyLMattox', 'Mr_Derivatives', 'warrior_0719', 'ChartingProdigy', 
        'allstarcharts', 'yuriymatso', 'AdamMancini4', 'CordovaTrades','Barchart',]

## check time and pinned or reteweeted and search for tickers ## 
def loop_in_tweets(driver,tweets , previous_posts , returned_dictionary):
    ## initialize time in utc and range of time ##
    time_now_utc = datetime.now(timezone.utc)
    time_end_range = time_now_utc - timedelta(hours=10)
    ## boolean condition variable ##
    condition_variable = True
    for tweet in tweets:
        previous_posts.append(tweet)
        time.sleep(3)
        ### check if tweet is pinned or retweeted ###
        try:
            try:
                ## for pinned ##
                pined = tweet.find_element(By.XPATH , './/div[@data-testid="socialContext"]')
                continue
            except:
                ## for retweeted ##
                retweet = tweet.find_element(By.XPATH , './/span[@data-testid="socialContext"]')
                continue
        except:
            datetime_tweet = tweet.find_element(By.TAG_NAME,'time').get_attribute('datetime')
            time.sleep(2)
            parsed_datetime = datetime.strptime(datetime_tweet, "%Y-%m-%dT%H:%M:%S.%fZ")
            # Convert both dt and time_end_range to the same format
            dt_formatted = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            time_end_range_formatted = time_end_range.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            if time_end_range_formatted < dt_formatted:
                time.sleep(3)
                ### to open the tweet on new tab ###
                ActionChains(driver).move_to_element(tweet).key_down(Keys.CONTROL).click(tweet).key_up(Keys.CONTROL).perform()
                time.sleep(2)
                ## switch driver to the new opened window ##
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)
                article = driver.find_element(By.XPATH,"//div[@class='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-1inkyih r-16dba41 r-bnwqim r-135wba7']")
                time.sleep(3)
                tickers_symbols = article.find_elements(By.XPATH,".//span[@class='r-18u37iz']")
                time.sleep(3)
                if tickers_symbols != []:
                    time.sleep(2)
                    for symbol in tickers_symbols:
                        time.sleep(2)
                        if symbol.text.startswith('$') and symbol.text.upper()[1:] in our_symbols:
                            time.sleep(2)
                            symbol_string = symbol.text.upper()[1:]
                            if symbol.text.upper()[1:] in returned_dictionary.keys():
                                returned_dictionary[f'{symbol_string}'] += 1
                                print(returned_dictionary)
                            else:
                                returned_dictionary[f'{symbol_string}'] = 1
                                print(returned_dictionary)
                    ## close the new opened tab and switch to origin first tab ##
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                else:
                    ## close the new opened tab and switch to origin first tab ##
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue
            else:
                condition_variable = False
                return  previous_posts , condition_variable
    return  previous_posts , condition_variable

def twitter_scraper():
    ## initialize returend dictionary ##
    returned_dictionary = {}
    driver = webdriver.Chrome()
    ## log in process ##
    driver.get("https://x.com/i/flow/login")
    ######
    username_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))
    username_input.send_keys('soma94375')
    ## click next button ##
    next_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")))
    next_button.click()
    ## add email ##
    try:
        email_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))
        email_input.send_keys('asemgeeklabs@gmail.com')
        time.sleep(3)
        ## click next button ##
        next_button2 = driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
        next_button2.click()
        time.sleep(3)
    ####
    finally:
        password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))
        password.send_keys('ASEMgeeklabs2024@')
        ## click log in button ##
        login_button = driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
        login_button.click()
        time.sleep(2)
        for account in twitter_accounts:
            print(account)
            driver.get(f'https://x.com/{account}')
            time.sleep(5)
            ##########################################
            ######### END OF LOG IN process ##########
            ##########################################
            previous_posts = [] ## initialize previuos posts ##
            ### infinte loop till get tweet out of 6 hours range ###
            condition_variable = True ### initialize condition loopin ###
            while condition_variable: 
                time.sleep(2)
                ## get all tweets elements ##
                tweets = driver.find_elements(By.TAG_NAME , 'article')
                time.sleep(5)
                ## check if tweets is in previous posts or new (te reduce the duplication) ##
                if previous_posts == []:
                    ## start looping ##
                    previous_posts , condition_variable = loop_in_tweets(driver,tweets,previous_posts,returned_dictionary)
                else:
                    time.sleep(5)
                    new_tweets = [item for item in tweets if item not in previous_posts] ### reduce the duplicated tweets from new scrolled tweets ###
                    time.sleep(5) 
                    previous_posts , condition_variable = loop_in_tweets(driver,new_tweets,previous_posts,returned_dictionary)
                ### scrolling to get more tweets ##
                driver.execute_script("scrollBy(0,2000)")
            # else:
        driver.close()
    return returned_dictionary

final_dictionary = twitter_scraper()
print(final_dictionary)