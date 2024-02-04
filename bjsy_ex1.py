import sys
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

def format_date(date_str):
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])

    formatted_date = datetime(year, month, day).strftime("%Y-%m-%d")
    return formatted_date


def get_exchange_rate(date, currency_code):
    # 创建Edge浏览器对象
    driver = webdriver.Edge()
    
    try:
        # 打开中国银行外汇牌价网站
        driver.get('https://www.boc.cn/sourcedb/whpj/')
        
        # 等待页面加载完成
        time.sleep(1)

        # 转成日期格式
        date = format_date(date)
        print(date)
        
        # 下拉框筛选 --英转中
        if currency_code == 'USD':
            currency_code = '美元'
        if currency_code == 'EUR':
            currency_code = '欧元'

        # 输入日期 --ok
        element = driver.find_element(By.XPATH, '//*[@id="erectDate"]')
        element.clear()
        element.send_keys(date)
        element = driver.find_element(By.XPATH, '//*[@id="nothing"]')
        element.clear()
        element.send_keys(date)
        
        # 选择货币  --ok
        currency_select = driver.find_element(By.XPATH, '//*[@id="pjname"]')
        currency_select.click()
        currency_option = driver.find_element(By.XPATH, f'//*[@id="pjname"]/option[text()="{currency_code}"]')
        currency_option.click()
        
        # 点击查询按钮
        query_button = driver.find_element(By.XPATH, '//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input')
        query_button.click()
        
        # 等待查询结果加载完成
        time.sleep(1)
        
        # 获取现汇卖出价
        exchange_rate = driver.find_element(By.XPATH, '/html/body/div/div[4]/table/tbody/tr[2]/td[4]').text

        # 关闭浏览器
        # driver.quit()
        
        # 返回查询结果
        return exchange_rate
    
    except Exception as e:
        print(f'Error: {e}')
        
    finally:
        # 关闭浏览器
        driver.quit()

        

if __name__ == '__main__':
    # 获取命令行参数
    date = sys.argv[1]
    currency_code = sys.argv[2]
    # date = '20211231'
    # currency_code = 'USD'

    # 查询外汇牌价
    rate = get_exchange_rate(date, currency_code)
    
    # 将结果保存到result.txt文件
    with open('result.txt', 'w') as f:
        f.write(rate)
        f.close()