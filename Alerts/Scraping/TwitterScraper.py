from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import  datetime , timezone , timedelta
from django.core.cache import cache
from ..models import Ticker
from Alerts.models import Alert
from ..consumers import WebSocketConsumer
from .RedditScraper import Reddit_API_Response
import time

## get all tickers in cache ##
def get_cached_queryset():
    queryset = cache.get("tickerlist")
    if not queryset:
        queryset = Ticker.objects.all()
        cache.set("tickerlist", queryset, timeout=86400)
    return queryset

## method to get all symbols ##
def get_symbols():
    all_tickers = get_cached_queryset()
    all_symbols = [ticker.symbol for ticker in all_tickers]
    return all_symbols

## method for login ##
def login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-infobars")
    chromedriver_path = '/usr/bin/chromedriver'
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service , options=options)
    ## log in process ##
    driver.get("https://x.com/i/flow/login")                                                                                    
    username_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))
    username_input.send_keys('ahmedgeeklabs')
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    ## add email ##
    try:
        email_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')))
        email_input.send_keys('ahmedtahageeklab@gmail.com')
        ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    except:
        pass
    finally: 
        password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")))
        password.send_keys('Polo_1991')
        
        ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        
        try:
            email_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')))
            
            email_input.send_keys('ahmedtahageeklab@gmail.com')
            ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            time.sleep(2)
        except:  
            time.sleep(2)
        try:
            button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-16y2uox r-6gpygo r-1a11zyx r-1udh08x r-1udbk01 r-3s2u2q r-1glkqn6 r-peo1c r-1ps3wis r-cxgwc0 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")))
            button.click()
            
        except:
            
            pass
        return driver

## list of symbols ##
our_symbols = get_symbols()

## list of scraped twitter accounts ##
twitter_accounts = [
        'TriggerTrades', 'RoyLMattox', 'Mr_Derivatives', 'warrior_0719', 'ChartingProdigy', 
        'allstarcharts', 'yuriymatso', 'AdamMancini4', 'CordovaTrades','Barchart']

## check time and pinned or reteweeted and search for tickers ## 
def loop_in_tweets(driver,tweets , previous_posts , returned_dictionary):
    ## initialize time in utc and range of time ##
    time_now_utc = datetime.now(timezone.utc)
    time_end_range = time_now_utc - timedelta(hours=23)
    time_end_range_formatted = time_end_range.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    ## boolean condition variable ##
    condition_variable = True
    for tweet in tweets:
        previous_posts.append(tweet)
        ### check if tweet is pinned or retweeted ###
        try:
            ## for pinned ##
            pined = tweet.find_element(By.XPATH , './/div[@data-testid="socialContext"]')
            continue
        except:
            try:
                ## for retweeted ##
                retweet = tweet.find_element(By.XPATH , './/span[@data-testid="socialContext"]')
                continue
            except NoSuchElementException:
                ...
        datetime_tweet = WebDriverWait(tweet,10).until(EC.presence_of_element_located((By.TAG_NAME,'time')))
        datetime_tweet = datetime_tweet.get_attribute('datetime')
        parsed_datetime = datetime.strptime(datetime_tweet, "%Y-%m-%dT%H:%M:%S.%fZ")
        # Convert both dt and time_end_range to the same format
        dt_formatted = parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        if time_end_range_formatted < dt_formatted:
            ## specify only text of tweet to click on it ##
            tweet_text = WebDriverWait(tweet,10).until(EC.presence_of_element_located((By.XPATH,'.//div[@class="css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim"]')))
            ### to open the tweet on new tab ###
            ActionChains(driver).move_to_element(tweet_text).key_down(Keys.CONTROL).click(tweet_text).key_up(Keys.CONTROL).perform()
            ## switch driver to the new opened window ##
            driver.switch_to.window(driver.window_handles[-1])
            
            try:
                article = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-1inkyih r-16dba41 r-bnwqim r-135wba7']")))
                tickers_symbols = WebDriverWait(article,10).until(EC.presence_of_all_elements_located((By.XPATH,".//span[@class='r-18u37iz']")))
                if tickers_symbols != []:
                    for symbol in tickers_symbols:
                        symbol_string = symbol.text.upper()[1:]
                        if symbol.text.startswith('$') and symbol_string in our_symbols:
                            if symbol_string in returned_dictionary.keys():
                                returned_dictionary[f'{symbol_string}'] += 1
                            else:
                                returned_dictionary[f'{symbol_string}'] = 1
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue
            except Exception as e :
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
        else:
            condition_variable = False
            return  previous_posts , condition_variable , returned_dictionary 
    return  previous_posts , condition_variable , returned_dictionary  

## method to gives alerts ##
def get_alerts(returned_dictionary):
    if returned_dictionary != {}:
        for key , value in returned_dictionary.items():
            if value >=10 :
                ticker = Ticker.objects.get(symbol=key)
                alert = Alert.objects.create(ticker= ticker, strategy= "People's Opinion", shares_quantity= value )
                alert.save()
                WebSocketConsumer.send_new_alert(alert)

def twitter_scraper():
    driver = login()
    while True:
        ## initialize returend dictionary ##
        returned_dictionary = {} 
        for account in twitter_accounts:
                driver.get(f'https://x.com/{account}/')
                ######### END OF LOG IN process ##########
                previous_posts = [] ## initialize previuos posts ##
                condition_variable = True ### initialize condition loopin ###
                ### infinte loop till get tweet aout of 6 hours range ###
                while condition_variable: 
                    try:
                        ## get all tweets elements ##
                        tweets = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME,'article')))
                        ## check if tweets is in previous posts or new (te reduce the duplication) ##
                        if previous_posts == []:
                            ## start looping ##
                            previous_posts , condition_variable , returned_dictionary = loop_in_tweets(driver,tweets,previous_posts,returned_dictionary)
                        else:
                            new_tweets = [item for item in tweets if item not in previous_posts] ### reduce the duplicated tweets from new scrolled tweets ###
                            previous_posts , condition_variable , returned_dictionary = loop_in_tweets(driver,new_tweets,previous_posts,returned_dictionary)
                        ### scrolling to get more tweets ##
                        driver.execute_script("scrollBy(0,2000)")
                    except:
                        break
                else:
                    continue
        returned_dictionary = Reddit_API_Response(returned_dict=returned_dictionary, our_symbol= our_symbols)
        get_alerts(returned_dictionary)
        time.sleep(1800)

