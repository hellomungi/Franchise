import pandas as pd

from Class.detail_page_crawler import DetailPageToList
from Class.detail_page_crawler import DetailPageCrawler
from Class.Separator import DataPreprocessing

if __name__ == '__main__':
    DPL = DetailPageToList()
    url = "https://franchise.ftc.go.kr/"
    detail_page_list = DPL.detail_page_list(url)

    DPC = DetailPageCrawler()
    DPC.detail_page_creawlling(url, detail_page_list)

    FIX = DataPreprocessing()
    ori_df = pd.read_csv("./download/FranChise.csv", sep='|')
    fix_df = FIX.DATA_FIX(ori_df)

    fix_df.to_csv('./download/sep_FranChise_Pipe.csv', sep='|', encoding='utf-8-sig', index=False)
    fix_df.to_csv('./download/sep_FranChise.csv', encoding='utf-8-sig', index=False)
