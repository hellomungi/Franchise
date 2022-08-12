import pandas as pd
import re


class DataPreprocessing:
    def FIX_TEL(self, df):
        print("FIX_TEL DataProcessing..")
        for idx, TEL in enumerate(df['REF_TEL']):
            #print("##############################\n", "idx : ", idx, "TEL : ", TEL)
            Split_Tels = TEL.split("-")
            REF_TEL = ''
            TEL_NUM = 0
            for Tels in Split_Tels:
                #print("--------------------------\n", "Tels.strip() : ", Tels.strip(), " / len : ", len(Tels.strip()), "/ TEL NUM : ", TEL_NUM)
                if len(Tels.strip()) == 0:
                    continue
                if TEL_NUM == 0:
                    REF_TEL = Tels.strip()
                    TEL_NUM += 1
                    continue
                else:
                    REF_TEL = REF_TEL + "-" + Tels.strip()
                    TEL_NUM += 1
            df.loc[idx, 'REF_TEL'] = REF_TEL
        return df

    def FIX_FAX(self, df):
        print("FIX_FAX DataProcessing..")
        for idx, FAX in enumerate(df['FAX']):
            #print("##############################\n", "idx : ", idx, "TEL : ", TEL)
            Split_FAXs = FAX.split("-")
            FAX_fix = ''
            FAX_NUM = 0
            for FAXs in Split_FAXs:
                #print("--------------------------\n", "Tels.strip() : ", Tels.strip(), " / len : ", len(Tels.strip()), "/ TEL NUM : ", TEL_NUM)
                if len(FAXs.strip()) == 0:
                    continue
                if FAX_NUM == 0:
                    FAX_fix = FAXs.strip()
                    FAX_NUM += 1
                    continue
                else:
                    FAX_fix = FAX_fix + "-" + FAXs.strip()
                    FAX_NUM += 1

            df.loc[idx, 'FAX'] = FAX_fix
        return df

    def FIX_FRANCHISE_NO(self, df):
        print("FIX_FRANCHISE_NO DataProcessing..")
        df['FRANCHISE_NO'] = df.FRANCHISE_NO.astype(str)
        for idx, FRANCHISE_NO in enumerate(df['FRANCHISE_NO']):
            df.loc[idx, 'FRANCHISE_NO'] = FRANCHISE_NO.replace('.0', '')
        return df

    def FIX_ADDRESS(self, df):
        print("FIX_ADDRESS DataProcessing..")
        for idx, address in enumerate(df['ADDRESS']):
            Split = address.split(" ")
            mailnumber_compile = re.compile("([0-9][0-9][0-9][0-9][0-9])+")
            mailnumber = mailnumber_compile.search(Split[2])
            if mailnumber is None:
                mailnumber_compile = re.compile("([0-9][0-9][0-9][0-9][0-9])+")
                mailnumber = mailnumber_compile.search(Split[3])
                if mailnumber is None:
                    df.loc[idx, 'ADDRESS'] = address.replace("우 : ", "")
                    df.loc[idx, 'ZIPCODE'] = '-'
                    # print(Split)
                    # print(address)
                else:
                    df.loc[idx, 'ADDRESS'] = address.replace("우 : ", "").replace(Split[3]+" ", "")
                    df.loc[idx, 'ZIPCODE'] = Split[3]
            else:
                df.loc[idx, 'ADDRESS'] = address.replace("우 : ", "").replace(Split[2]+" ", "")
                df.loc[idx, 'ZIPCODE'] = Split[2]
        return df

    def CORNUMBER(self, df):
        print("CORNUMBER DataProcessing..")
        for idx, cornumber in enumerate(df['CORNUMBER']):
            cornumber = cornumber.replace("\xa0", "")
            df.loc[idx, 'CORNUMBER'] = cornumber
            """ 데이터 검증 1자리~14자리
            if len(cornumber) != 14 and len(cornumber) > 1:
                print(df.loc[idx, 'BRAND'], " / ", idx, " / ", cornumber, " / ", len(cornumber))"""
            data = re.compile("([0-9][0-9][0-9][0-9][0-9][0-9])+")
            data_search = data.search(cornumber)
            if data_search == None:
                # None 데이터 확인
                # print(cornumber, " / ", df.loc[idx, 'BRAND'], " / ", idx, " / ",  len(cornumber), " / ", data_search)
                df.loc[idx, 'CORNUMBER'] = '-'
        return df

    def BIZCODE(self, df):
        print("BIZCODE DataProcessing..")
        for idx, bizcode in enumerate(df['BIZCODE']):
            bizcode = bizcode.replace("\xa0", "")
            df.loc[idx, 'BIZCODE'] = bizcode
            data = re.compile("([0-9][0-9][0-9]-)+")
            data_search = data.search(bizcode)
            if data_search == None:
                print("Bizcode is not Match")
                print("bizcode:", bizcode, " / ", "BARND:", df.loc[idx, 'BRAND'], " / ", "index:", idx, " / ",  len(bizcode), " / ", data_search)
        return df

    def BRAND_CNT(self, df):
        print("BRAND_CNT DataProcessing..")
        df['BRAND_CNT'] = df.BRAND_CNT.astype(str)
        for idx, BRAND_CNT in enumerate(df['BRAND_CNT']):
            df.loc[idx, 'BRAND_CNT'] = BRAND_CNT.replace('.0', '')
        return df

    def REL_BIZ_CNT(self, df):
        print("REL_BIZ_CNT DataProcessing..")
        df['REL_BIZ_CNT'] = df.REL_BIZ_CNT.astype(str)
        for idx, REL_BIZ_CNT in enumerate(df['REL_BIZ_CNT']):
            df.loc[idx, 'REL_BIZ_CNT'] = REL_BIZ_CNT.replace('.0', '')
        return df

    def INIT_DATE(self, df):
        print("INIT_DATE DataProcessing..")
        df.INIT_DATE.fillna('-', inplace=True)
        df['INIT_DATE'] = df.INIT_DATE.astype(str)
        for idx, date in enumerate(df['INIT_DATE']):
            date = date.replace("\xa0", "")
            df.loc[idx, 'INIT_DATE'] = date
            """ 데이터 검증
            data = re.compile("(-)")
            data_search = data.match(date)
            if data_search != None:
                print("INIT_DATE is not Match")
                print("date:", date, "match:", data_search)
                print("INIT_DATE:", date, " / ", "BARND:", df.loc[idx, 'BRAND'], " / ", "index:", idx, " / ", len(date), " / ", data_search)"""
        return df

    def RGN_HQ_CNT(self, df):
        print("RGN_HQ_CNT DataProcessing..")
        df.RGN_HQ_CNT.fillna('0', inplace=True)
        df['RGN_HQ_CNT'] = df.RGN_HQ_CNT.astype(str)
        for idx, RGN_HQ_CNT in enumerate(df['RGN_HQ_CNT']):
            rgn_hq = RGN_HQ_CNT.replace("\xa0", "")
            rgn_hq = rgn_hq.replace("개", "")
            df.loc[idx, 'RGN_HQ_CNT'] = rgn_hq
        return df

    def BALANCE_MBRBS(self, df):
        print("BALANCE_MBRBS DataProcessing..")
        df.BALANCE_MBRBS.fillna('-', inplace=True)
        df['BALANCE_MBRBS'] = df.BALANCE_MBRBS.astype(str)
        for idx, BALANCE_MBRBS in enumerate(df['BALANCE_MBRBS']):
            df.loc[idx, 'BALANCE_MBRBS'] = BALANCE_MBRBS.replace(',', '')
            Split = BALANCE_MBRBS.split(",")
            BALANCE_MBRBS_fix = ''
            BALANCE_MBRBS_NUM = 0
            for BALANCE_MBRBSs in Split:
                if len(BALANCE_MBRBSs.strip()) == 0:
                    continue
                if BALANCE_MBRBS_NUM == 0:
                    BALANCE_MBRBS_fix = BALANCE_MBRBSs.strip()
                    BALANCE_MBRBS_NUM += 1
                    continue
                else:
                    BALANCE_MBRBS_fix = BALANCE_MBRBS_fix + BALANCE_MBRBSs.strip()
                    BALANCE_MBRBS_NUM += 1
            df.loc[idx, 'BALANCE_MBRBS'] = BALANCE_MBRBS_fix
        return df

    def FTC_CATE_CD(self, df):
        print("FTC_CATE_CD DataProcessing..")
        df.FTC_CATE_CD.fillna('0', inplace=True)
        df['FTC_CATE_CD'] = df.FTC_CATE_CD.astype(int)
        df['FTC_CATE_CD'] = df.FTC_CATE_CD.astype(str)
        return df

    def CIVIL(self, df):
        print("CIVIL DataProcessing..")
        df.CIVIL.fillna('0', inplace=True)
        df['CIVIL'] = df.CIVIL.astype(int)
        df['CIVIL'] = df.CIVIL.astype(str)
        return df

    def SENTENCED(self, df):
        print("SENTENCED DataProcessing..")
        df.SENTENCED.fillna('0', inplace=True)
        df['SENTENCED'] = df.SENTENCED.astype(int)
        df['SENTENCED'] = df.SENTENCED.astype(str)
        return df

    def MEMBERSHIP(self, df):
        print("MEMBERSHIP DataProcessing..")
        df['MEMBERSHIP'] = df.MEMBERSHIP.astype(str)
        for idx, MEMBERSHIP in enumerate(df['MEMBERSHIP']):
            df.loc[idx, 'MEMBERSHIP'] = MEMBERSHIP.replace(',', '')
            Split = MEMBERSHIP.split(",")
            MEMBERSHIP_fix = ''
            MEMBERSHIP_NUM = 0
            for MEMBERSHIPs in Split:
                if len(MEMBERSHIPs.strip()) == 0:
                    continue
                if MEMBERSHIP_NUM == 0:
                    MEMBERSHIP_fix = MEMBERSHIPs.strip()
                    MEMBERSHIP_NUM += 1
                    continue
                else:
                    MEMBERSHIP_fix = MEMBERSHIP_fix + MEMBERSHIPs.strip()
                    MEMBERSHIP_NUM += 1
            df.loc[idx, 'MEMBERSHIP'] = MEMBERSHIP_fix
        return df

    def EDUCOST(self, df):
        print("EDUCOST DataProcessing..")
        df['EDUCOST'] = df.EDUCOST.astype(str)
        for idx, EDUCOST in enumerate(df['EDUCOST']):
            df.loc[idx, 'EDUCOST'] = EDUCOST.replace(',', '')
            Split = EDUCOST.split(",")
            EDUCOST_fix = ''
            EDUCOST_NUM = 0
            for EDUCOSTs in Split:
                if len(EDUCOSTs.strip()) == 0:
                    continue
                if EDUCOST_NUM == 0:
                    EDUCOST_fix = EDUCOSTs.strip()
                    EDUCOST_NUM += 1
                    continue
                else:
                    EDUCOST_fix = EDUCOST_fix + EDUCOSTs.strip()
                    EDUCOST_NUM += 1
            df.loc[idx, 'EDUCOST'] = EDUCOST_fix
        return df

    def DEPOSIT(self, df):
        print("DEPOSIT DataProcessing..")
        df['DEPOSIT'] = df.DEPOSIT.astype(str)
        for idx, DEPOSIT in enumerate(df['DEPOSIT']):
            df.loc[idx, 'DEPOSIT'] = DEPOSIT.replace(',', '')
            Split = DEPOSIT.split(",")
            DEPOSIT_fix = ''
            DEPOSIT_NUM = 0
            for DEPOSITs in Split:
                if len(DEPOSITs.strip()) == 0:
                    continue
                if DEPOSIT_NUM == 0:
                    DEPOSIT_fix = DEPOSITs.strip()
                    DEPOSIT_NUM += 1
                    continue
                else:
                    DEPOSIT_fix = DEPOSIT_fix + DEPOSITs.strip()
                    DEPOSIT_NUM += 1
            df.loc[idx, 'DEPOSIT'] = DEPOSIT_fix
        return df

    def OTHERCOST(self, df):
        print("OTHERCOST DataProcessing..")
        df['OTHERCOST'] = df.OTHERCOST.astype(str)
        for idx, OTHERCOST in enumerate(df['OTHERCOST']):
            df.loc[idx, 'OTHERCOST'] = OTHERCOST.replace(',', '')
            Split = OTHERCOST.split(",")
            OTHERCOST_fix = ''
            OTHERCOST_NUM = 0
            for OTHERCOSTs in Split:
                if len(OTHERCOSTs.strip()) == 0:
                    continue
                if OTHERCOST_NUM == 0:
                    OTHERCOST_fix = OTHERCOSTs.strip()
                    OTHERCOST_NUM += 1
                    continue
                else:
                    OTHERCOST_fix = OTHERCOST_fix + OTHERCOSTs.strip()
                    OTHERCOST_NUM += 1
            df.loc[idx, 'OTHERCOST'] = OTHERCOST_fix
        return df

    def TOTAL(self, df):
        print("TOTAL DataProcessing..")
        df['TOTAL'] = df.TOTAL.astype(str)
        for idx, TOTAL in enumerate(df['TOTAL']):
            df.loc[idx, 'TOTAL'] = TOTAL.replace(',', '')
            Split = TOTAL.split(",")
            TOTAL_fix = ''
            TOTAL_NUM = 0
            for TOTALs in Split:
                if len(TOTALs.strip()) == 0:
                    continue
                if TOTAL_NUM == 0:
                    TOTAL_fix = TOTALs.strip()
                    TOTAL_NUM += 1
                    continue
                else:
                    TOTAL_fix = TOTAL_fix + TOTALs.strip()
                    TOTAL_NUM += 1
            df.loc[idx, 'TOTAL'] = TOTAL_fix
        return df

    def SICOST(self, df):
        print("SICOST DataProcessing..")
        df['SICOST'] = df.SICOST.astype(str)
        for idx, SICOST in enumerate(df['SICOST']):
            df.loc[idx, 'SICOST'] = SICOST.replace(',', '')
            Split = SICOST.split(",")
            SICOST_fix = ''
            SICOST_NUM = 0
            for SICOSTs in Split:
                if len(SICOSTs.strip()) == 0:
                    continue
                if SICOST_NUM == 0:
                    SICOST_fix = SICOSTs.strip()
                    SICOST_NUM += 1
                    continue
                else:
                    SICOST_fix = SICOST_fix + SICOSTs.strip()
                    SICOST_NUM += 1
            df.loc[idx, 'SICOST'] = SICOST_fix
        return df

    def INTERIORCOST(self, df):
        print("INTERIORCOST DataProcessing..")
        df['INTERIORCOST'] = df.INTERIORCOST.astype(str)
        for idx, INTERIORCOST in enumerate(df['INTERIORCOST']):
            df.loc[idx, 'INTERIORCOST'] = INTERIORCOST.replace(',', '')
            Split = INTERIORCOST.split(",")
            INTERIORCOST_fix = ''
            INTERIORCOST_NUM = 0
            for INTERIORCOSTs in Split:
                if len(INTERIORCOSTs.strip()) == 0:
                    continue
                if INTERIORCOST_NUM == 0:
                    INTERIORCOST_fix = INTERIORCOSTs.strip()
                    INTERIORCOST_NUM += 1
                    continue
                else:
                    INTERIORCOST_fix = INTERIORCOST_fix + INTERIORCOSTs.strip()
                    INTERIORCOST_NUM += 1
            df.loc[idx, 'INTERIORCOST'] = INTERIORCOST_fix
        return df

    def INITIAL(self, df):
        print("INITIAL DataProcessing..")
        df.INITIAL.fillna('0', inplace=True)
        df['INITIAL'] = df.INITIAL.astype(int)
        df['INITIAL'] = df.INITIAL.astype(str)
        return df

    def EXTENDED(self, df):
        print("EXTENDED DataProcessing..")
        df.EXTENDED.fillna('0', inplace=True)
        df['EXTENDED'] = df.EXTENDED.astype(int)
        df['EXTENDED'] = df.EXTENDED.astype(str)
        return df

    def DATA_FIX(self, df):
        df = self.FIX_TEL(df)
        df = self.FIX_FAX(df)
        df = self.FIX_FRANCHISE_NO(df)
        df = self.FIX_ADDRESS(df)
        df = self.CORNUMBER(df)
        df = self.BIZCODE(df)
        df = self.BRAND_CNT(df)
        df = self.REL_BIZ_CNT(df)
        df = self.INIT_DATE(df)
        df = self.RGN_HQ_CNT(df)
        df = self.BALANCE_MBRBS(df)
        df = self.FTC_CATE_CD(df)
        df = self.CIVIL(df)
        df = self.SENTENCED(df)
        df = self.MEMBERSHIP(df)
        df = self.EDUCOST(df)
        df = self.DEPOSIT(df)
        df = self.OTHERCOST(df)
        df = self.TOTAL(df)
        df = self.SICOST(df)
        df = self.INTERIORCOST(df)
        df = self.INITIAL(df)
        df = self.EXTENDED(df)

        print("fix_df : \n", df.dtypes)
        print(df)
        return df

if __name__ == '__main__':
    FIX = DataPreprocessing()

    ori_df = pd.read_csv("./download/FranChise.csv", sep='|')
    #ori_df = ori_df.drop(['Unnamed: 0'], axis='columns')
    #print("ori_df \n", ori_df.dtypes)
    fix_df = FIX.DATA_FIX(ori_df)

    fix_df.to_csv('./download/sep_FranChise_Pipe.csv', sep='|', encoding='utf-8-sig', index=False)
    fix_df.to_csv('./download/sep_FranChise.csv', encoding='utf-8-sig', index=False)