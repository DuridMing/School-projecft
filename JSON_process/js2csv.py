import jsonlines
import pandas as pd
import csv

def js2csv():
    with jsonlines.open('metrics.json' , "r") as jsnl_read:
        df = pd.DataFrame(jsnl_read) 
        jsnl_read.close()

    df_catch = df[['Rank-1' , 'Rank-5' , 'Rank-10' ,'mAP' ,'mINP']]
    df_catch = df_catch.dropna()

    df_catch = df_catch.reset_index(drop=True)

    print(df_catch)

    with open("m.csv" ,"w" , newline='') as csvw:
        csv = csv.writer(csvw)
        csv.writerow(["file" , "Rank-1" , "Rank-5" , "Rank-10" , "mAP" , "mINP"])
        for num in range(len(df_catch)):
            # print(df_catch['Rank-1'][num])
            csv.writerow(["a" ,df_catch['Rank-1'][num],
                            df_catch['Rank-5'][num],df_catch['Rank-10'][num]
                            ,df_catch['mAP'][num],df_catch['mINP'][num]])

if __name__ =='__main__' :
    js2csv()