import time
import requests
import pandas as pd
import random
from bs4 import BeautifulSoup, Comment

class DetailPageToList:
    def detail_page_list(self, url):
        #page = "mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=brd&selUpjong=&selIndus=&pageUnit=1&pageIndex=1"
        page = "mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=brd&selUpjong=&selIndus=&pageUnit=30000"
        page_list = []

        response = requests.get(url + page)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            div = soup.find('div', {'id':'txt'})
            a_all = div.find_all('a', {'class':'authCtrl'})

            for a in a_all:
                detail_page = a.attrs['onclick']
                detail_page = detail_page.replace("fn_view('", "").replace("');", "")
                page_list.append(detail_page)
        else:
            print(response.status_code)

        page_list = list(set(page_list))

        return page_list

class DetailPageCrawler:
    def table_crawler(self, franc_df, table, table_num):
        # print(table_num, "\n", table)
        if table_num == 0:
            td_all = table.find_all('td')
            franc_df.loc[0, 'COMPANY'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace("상호", "")
            franc_df.loc[0, 'BRAND'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace("영업표지", "")
            franc_df.loc[0, 'CEO'] = td_all[2].text.replace("\n", "").replace("\t", "").replace("\r", "").replace("대표자", "")
            franc_df.loc[0, 'TPIND_NM'] = td_all[3].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'COR_FND_DATE'] = td_all[4].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'BIZ_FND_DATE'] = td_all[5].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'REF_TEL'] = td_all[6].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'FAX'] = td_all[7].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'FRANCHISE_NO'] = td_all[8].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'FIRST_DATE'] = td_all[9].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'END_DATE'] = td_all[10].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 1:
            td_all = table.find_all('td')
            franc_df.loc[0, 'ADDRESS'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "")
            franc_df.loc[0, 'BIZ_TYPE'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'CORNUMBER'] = td_all[2].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'BIZCODE'] = td_all[3].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 4:
            td_all = table.find_all('td')
            franc_df.loc[0, 'BRAND_CNT'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'REL_BIZ_CNT'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 5:
            td_all = table.find_all('td')
            franc_df.loc[0, 'INIT_DATE'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 9:
            td_all = table.find_all('td')
            franc_df.loc[0, 'RGN_HQ_CNT'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 11:
            td_all = table.find_all('td')
            franc_df.loc[0, 'SHREXPNS_DIV'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'BALANCE_MBRBS'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 12:
            td_all = table.find_all('td')
            franc_df.loc[0, 'FTC_CATE_CD'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'CIVIL'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'SENTENCED'] = td_all[2].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 13:
            td_all = table.find_all('td')
            franc_df.loc[0, 'MEMBERSHIP'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'EDUCOST'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'DEPOSIT'] = td_all[2].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'OTHERCOST'] = td_all[3].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'TOTAL'] = td_all[4].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 14:
            td_all = table.find_all('td')
            franc_df.loc[0, 'SICOST'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'STOREAREA'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'INTERIORCOST'] = td_all[2].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
        elif table_num == 15:
            td_all = table.find_all('td')
            franc_df.loc[0, 'INITIAL'] = td_all[0].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")
            franc_df.loc[0, 'EXTENDED'] = td_all[1].text.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")

        #print(franc_df)
        return franc_df

    def retry_fail_page(self, url, page_list):
        fail_list = []
        fail_df = pd.DataFrame()
        page_num = 1
        for page in page_list:
            print(page_num, " / ", len(page_list), " / ", page)
            franc_df = pd.DataFrame()
            response = requests.get(url + page)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                # -- html 주석제거
                comments = soup.findAll(text=lambda text: isinstance(text, Comment))
                [comment.extract() for comment in comments]
                # -- html 주석제거 끝
                div = soup.find('div', {'id': 'txt'})
                table_all = div.find_all('table')

                table_num = 0
                for table in table_all:
                    franc_df = self.table_crawler(franc_df, table, table_num)
                    table_num += 1

            else:
                print(response.status_code)
                print("ERROR Page Add to Fail_list / ", page_num, " / ", len(page_list), " / ", page)
                fail_list.append(page)

            fail_df = pd.concat([fail_df, franc_df])
            page_num += 1
            rnadom_time = random.uniform(0.5, 1.0)
            time.sleep(rnadom_time)

        return fail_df, fail_list

    def detail_page_creawlling(self, url, page_list):
        merge_df = pd.DataFrame()
        fail_list = []
        #fail_list = ['/mnu/00013/program/userRqst/view.do?firMstSn=419426', '/mnu/00013/program/userRqst/view.do?firMstSn=124620', '/mnu/00013/program/userRqst/view.do?firMstSn=419008', '/mnu/00013/program/userRqst/view.do?firMstSn=100404', '/mnu/00013/program/userRqst/view.do?firMstSn=120010', '/mnu/00013/program/userRqst/view.do?firMstSn=403408', '/mnu/00013/program/userRqst/view.do?firMstSn=115760', '/mnu/00013/program/userRqst/view.do?firMstSn=74437', '/mnu/00013/program/userRqst/view.do?firMstSn=101023', '/mnu/00013/program/userRqst/view.do?firMstSn=421460', '/mnu/00013/program/userRqst/view.do?firMstSn=116870', '/mnu/00013/program/userRqst/view.do?firMstSn=426654', '/mnu/00013/program/userRqst/view.do?firMstSn=127162']
        page_num = 1
        for page in page_list:
            print(page_num, " / ", len(page_list), " / ", page)
            franc_df = pd.DataFrame()
            response = requests.get(url + page)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                comments = soup.findAll(text=lambda text: isinstance(text, Comment))
                [comment.extract() for comment in comments]
                div = soup.find('div', {'id': 'txt'})
                table_all = div.find_all('table')

                table_num = 0
                for table in table_all:
                    franc_df = self.table_crawler(franc_df, table, table_num)
                    table_num += 1

            else:
                print(response.status_code)
                print("ERROR Page Add to Fail_list / ", page_num, " / ", len(page_list), " / ", page)
                fail_list.append(page)

            merge_df = pd.concat([merge_df, franc_df])
            page_num += 1
            rnadom_time = random.uniform(0.5, 1.0)
            time.sleep(rnadom_time)

        while True:
            if len(fail_list) == 0:
                print("Success Crawling")
                merge_df.to_csv("./download/Save_FranChise.csv", encoding='utf-8-sig', index=False)
                merge_df.to_csv("./download/FranChise.csv", encoding='utf-8-sig', index=False)
                break
            else:
                print("Fail List : ", len(fail_list), fail_list)
                url = "https://franchise.ftc.go.kr/"
                fail_df, fail_list = self.retry_fail_page(url, fail_list)
                merge_df = pd.concat([merge_df, fail_df])