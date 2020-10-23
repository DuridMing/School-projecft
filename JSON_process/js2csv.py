import jsonlines
import pandas as pd
import csv as Csv
import glob
import os


class trans():
    def __init__(self, origin_path):
        self.ori_path = origin_path
        self.df_f = pd.DataFrame()
        self.dir_cache = []

    def js2csv(self, file, dir_name):
        with jsonlines.open(file, "r") as jsnl_read:
            df = pd.DataFrame(jsnl_read)
            jsnl_read.close()

        df_catch = df[['Rank-1', 'Rank-5', 'Rank-10', 'mAP', 'mINP']]
        df_catch = df_catch.dropna()

        df_catch = df_catch.reset_index(drop=True)

        print(df_catch)

        with open("metrics.csv", "w", newline='') as csvw:
            csv = Csv.writer(csvw)
            csv.writerow(["name", "Rank-1", "Rank-5",
                          "Rank-10", "mAP", "mINP"])
            for num in range(len(df_catch)):
                # print(df_catch['Rank-1'][num])
                csv.writerow([dir_name, df_catch['Rank-1'][num],
                              df_catch['Rank-5'][num], df_catch['Rank-10'][num], df_catch['mAP'][num], df_catch['mINP'][num]])
            csvw.close()

    def js2csv_in_one(self, file):
        with jsonlines.open(file, "r") as jsnl_read:
            df = pd.DataFrame(jsnl_read)
            jsnl_read.close()

        df_catch = df[['Rank-1', 'Rank-5', 'Rank-10', 'mAP', 'mINP']]
        df_catch = df_catch.dropna()

        df_catch = df_catch.reset_index(drop=True)

        temp = df_catch.tail(1)
        self.df_f = self.df_f.append(temp, ignore_index=True)
        # print(self.df_f)

    def write_one_csv(self):
        print(self.df_f)
        with open("metrics.csv", "w", newline='') as csvw:
            csv = Csv.writer(csvw)
            csv.writerow(["name", "Rank-1", "Rank-5",
                          "Rank-10", "mAP", "mINP"])
            for num in range(len(self.df_f)):
                # print(self.df_f['Rank-1'][num])
                csv.writerow([self.dir_cache[num], self.df_f['Rank-1'][num],
                              self.df_f['Rank-5'][num], self.df_f['Rank-10'][num], self.df_f['mAP'][num], self.df_f['mINP'][num]])

    def trans_file(self, one_file=True):
        for dirname in glob.glob('*'):
            if os.path.isdir(dirname):

                os.chdir(dirname)
                file = "metrics.json"
                if os.path.isfile("metrics.json"):
                    self.dir_cache.append(dirname)
                    print(os.getcwd())
                    if one_file:
                        self.js2csv_in_one(file=file)
                    else:
                        self.js2csv(dir_name=dirname, file=file)
                os.chdir("..")
            if one_file:
                self.write_one_csv()


if __name__ == '__main__':
    trans = trans(origin_path=os.getcwd)
    trans.trans_file(one_file=True)
