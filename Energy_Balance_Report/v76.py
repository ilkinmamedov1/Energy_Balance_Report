import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from datetime import date, timedelta
import cx_Oracle
from tkinter import * 
from tkinter import messagebox
from time import sleep
import pandas as pd
from pandastable import Table
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np



con3 = cx_Oracle.connect('--------/-------@//--------------------------')
cur3 = con3.cursor()
con1 = cx_Oracle.connect('--------/-------@//--------------------------')
cur1 = con1.cursor()
con2 = cx_Oracle.connect('--------/-------@//--------------------------')
cur2 = con2.cursor()






















#################################################      ((  tab2 tm/ktm      ))



def tab2date1():
    def print_sel():    
        tmktmbutdate1['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    
def tab2date2():
    def print_sel():    
        tmktmbutdate2['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()



def tmktmserch():    ########################   tab2 tmktm axdarish methodu
    tmktmtreeser.delete(*tmktmtreeser.get_children())
    tmktmtreeser2.delete(*tmktmtreeser2.get_children())
    tmktmtreeser3.delete(*tmktmtreeser3.get_children())
    
    
    
    for widgets in rmktmfram1.winfo_children():
      widgets.destroy()
      
    
    for widgets in rmktmfram2.winfo_children():
      widgets.destroy()
      
      



    
    fg =  str(tmktmcombobox.get())
    x = fg[:2]
    
    
    gf = str(tmktmentry.get())
    
    
    
    if gf != '' and x == '00' :
        
        hbn = '%' + gf + '%'
        
        sql = """SELECT
    tbl_transformer.name,
    CRYL2UTF(tbl_division.name) AS name1,
    tbl_transformer_group.subjectid,
    tbl_transformer.group_id_seq
FROM
    tbl_transformer_group
    LEFT JOIN tbl_transformer ON tbl_transformer.group_id_seq = tbl_transformer_group.id_seq
    LEFT JOIN tbl_division ON tbl_division.divisionid = tbl_transformer.sales_divisionid
                              AND tbl_division.subjectid = tbl_transformer.sales_subjectid
                              
                              where tbl_transformer_group.name like :yashik   order by tbl_transformer.name """
        cur1.execute(sql,yashik = hbn)
        sefrf = cur1.execute(sql,yashik = hbn)
        for dt in sefrf: 
            tmktmtreeser.insert("", 'end',
                       values =(dt[0],dt[1],dt[2],dt[3])) 
            
            
    elif gf != '' and x != '00' :
        
        hbn = '%' + gf + '%'
        
        sql = """SELECT
    tbl_transformer.name,
    CRYL2UTF(tbl_division.name) AS name1,
    tbl_transformer_group.subjectid,
    tbl_transformer.group_id_seq
FROM
    tbl_transformer_group
    LEFT JOIN tbl_transformer ON tbl_transformer.group_id_seq = tbl_transformer_group.id_seq
    LEFT JOIN tbl_division ON tbl_division.divisionid = tbl_transformer.sales_divisionid
                              AND tbl_division.subjectid = tbl_transformer.sales_subjectid
                              
                              where tbl_transformer.subject = :salyeshka
                              
                              and tbl_transformer_group.name like :yashik    order by tbl_transformer.name """
        cur1.execute(sql,salyeshka = x,yashik = hbn)
        sefrf = cur1.execute(sql,salyeshka = x,yashik = hbn)
        for dt in sefrf: 
            tmktmtreeser.insert("", 'end',
                       values =(dt[0],dt[1],dt[2],dt[3])) 
    
    

    
    elif x == '00':

        
        sql = """SELECT
    tbl_transformer.name,
    CRYL2UTF(tbl_division.name) AS name1,
    tbl_transformer_group.subjectid,
    tbl_transformer.group_id_seq
FROM
    tbl_transformer_group
    LEFT JOIN tbl_transformer ON tbl_transformer.group_id_seq = tbl_transformer_group.id_seq
    LEFT JOIN tbl_division ON tbl_division.divisionid = tbl_transformer.sales_divisionid
                              AND tbl_division.subjectid = tbl_transformer.sales_subjectid    order by tbl_transformer.name"""
        cur1.execute(sql)
        sefrf = cur1.execute(sql)
        for dt in sefrf: 
            tmktmtreeser.insert("", 'end',
                       values =(dt[0],dt[1],dt[2],dt[3])) 
            
            
    elif gf == '':
        sql = """SELECT
    tbl_transformer.name,
    CRYL2UTF(tbl_division.name) AS name1,
    tbl_transformer_group.subjectid,
    tbl_transformer.group_id_seq
FROM
    tbl_transformer_group
    LEFT JOIN tbl_transformer ON tbl_transformer.group_id_seq = tbl_transformer_group.id_seq
    LEFT JOIN tbl_division ON tbl_division.divisionid = tbl_transformer.sales_divisionid
                              AND tbl_division.subjectid = tbl_transformer.sales_subjectid
                              
                              
                              
                              where tbl_transformer.subject = :yashik    order by tbl_transformer.name """
        cur1.execute(sql,yashik = x)
        sefrf = cur1.execute(sql,yashik = x)
        for dt in sefrf: 
            tmktmtreeser.insert("", 'end',
                       values =(dt[0],dt[1],dt[2],dt[3])) 
    
    
    
    
    

    


def tab2start():
    d1 = tmktmbutdate1['text']
    d2 = tmktmbutdate2['text']
    
    tmktmtreeser2.delete(*tmktmtreeser2.get_children())
    
    tmktmtreeser3.delete(*tmktmtreeser3.get_children())
    
    
    
    
    
    for widgets in rmktmfram1.winfo_children():
      widgets.destroy()
      
      
    for widgets in rmktmfram2.winfo_children():
      widgets.destroy()


    print(d1)
    print(d2)
    
    
    
    
    selected = tmktmtreeser.focus()
    temp = tmktmtreeser.item(selected, 'values')
    u = str(temp[3])
    
    
    print(u)
    
    
    if d1 == 'ILK_TARIX':
        messagebox.showinfo('tarix_sec')
    elif d2 == 'SON_TARIX':
        messagebox.showinfo('tarix_sec')
    else:
        print('saxi')
        
        
        ###### ahali   >>>>
        
        sql = """SELECT
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    COUNT(vw_subcontrol.kvth)
    
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >= TO_DATE(:nm1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:nm2,'YYYY-MM-DD')
GROUP BY
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur2.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur2.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdahalikw  =   pd.DataFrame(cazi1,columns = ['GROUP_ID','DATE','AHALI_KW','OXUNMA_AHALI'])
        
        print(pdahalikw)
        
        
        
        sql = """SELECT
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth)
    
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subother.ddate >= TO_DATE(:nm1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:nm2,'YYYY-MM-DD')
    AND NOT(vw_subother.otherid IN ('128'))
GROUP BY
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur2.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur2.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdahaliakt  =   pd.DataFrame(cazi1,columns = ['GROUP_ID','DATE','AHALI_AKT'])
        
        
        
        
        pdahaliall =    pd.merge(pdahalikw, pdahaliakt, on=['GROUP_ID','DATE'], how='outer')
        
        
        print(pdahaliall)
        
        
        ###########  >>> qahali
        
        
        sql = """SELECT
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    COUNT(vw_subcontrol.kvth)
    
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >= TO_DATE(:nm1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:nm2,'YYYY-MM-DD')
GROUP BY
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur1.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur1.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdqahalikw  =   pd.DataFrame(cazi1,columns = ['GROUP_ID','DATE','QAHALI_KW','OXUNMA_QAHALI'])
        
        
        pdrealiz1 =    pd.merge(pdahaliall, pdqahalikw, on=['GROUP_ID','DATE'], how='outer')
        
        
        sql = """SELECT
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth)
    
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subother.ddate >= TO_DATE(:nm1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:nm2,'YYYY-MM-DD')
    
GROUP BY
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur1.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur1.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdqahaliakt  =   pd.DataFrame(cazi1,columns = ['GROUP_ID','DATE','QAHALI_AKT'])
        
        
        
        
        pdrealiz2 =    pd.merge(pdrealiz1, pdqahaliakt, on=['GROUP_ID','DATE'], how='outer')
        
        
        print(pdrealiz2)
        
        
        
        ###########  TEXBAZA  >>>
        
        
        
        sql = """SELECT
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth)
    
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >= TO_DATE(:nm1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:nm2,'YYYY-MM-DD')
GROUP BY
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur3.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur3.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdtexbazdixkw  =   pd.DataFrame(cazi1,columns = ['GROUP_ID','DATE','ALINAN_KW'])
        
        
        pdrealiz3 =    pd.merge(pdrealiz2, pdtexbazdixkw, on=['GROUP_ID','DATE'], how='outer')
        
        
        sql = """SELECT
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth)
    
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subother.ddate >= TO_DATE(:nm1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:nm2,'YYYY-MM-DD')
    
GROUP BY
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur3.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur3.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdqahaliakt  =   pd.DataFrame(cazi1,columns = ['GROUP_ID','DATE','TEXBAZA_AKT'])
        
        
        
        
        pdrealiz4  =    pd.merge(pdrealiz3, pdqahaliakt, on=['GROUP_ID','DATE'], how='outer')
        
        
        print(pdrealiz4)
        
        pdrealiz4['AHALI_KW'] = pdrealiz4['AHALI_KW'].fillna(0)
        pdrealiz4['AHALI_AKT'] = pdrealiz4['AHALI_AKT'].fillna(0)
        pdrealiz4['OXUNMA_AHALI'] = pdrealiz4['OXUNMA_AHALI'].fillna(0)
        pdrealiz4['QAHALI_KW'] = pdrealiz4['QAHALI_KW'].fillna(0)
        pdrealiz4['QAHALI_AKT'] = pdrealiz4['QAHALI_AKT'].fillna(0)
        pdrealiz4['OXUNMA_QAHALI'] = pdrealiz4['OXUNMA_QAHALI'].fillna(0)
        
        
        pdrealiz4['ALINAN_KW'] = pdrealiz4['ALINAN_KW'].fillna(0)
        pdrealiz4['TEXBAZA_AKT'] = pdrealiz4['TEXBAZA_AKT'].fillna(0)
        
        pdrealiz4['REALIZASIYA'] = pdrealiz4['AHALI_KW'] + pdrealiz4['AHALI_AKT'] + pdrealiz4['QAHALI_KW'] + pdrealiz4['QAHALI_AKT'] 
        pdrealiz4['ALINAN'] = pdrealiz4['ALINAN_KW'] + pdrealiz4['TEXBAZA_AKT']
        
        pdrealiz4['FERQ'] = pdrealiz4['ALINAN'] - pdrealiz4['REALIZASIYA']
        pdrealiz4['%'] = pdrealiz4['FERQ'] * 100 / pdrealiz4['ALINAN']
        
        print(pdrealiz4)
        
        
        
   
        
        
        
        
        #gfgggvv1 = gfggg1.drop(columns=['FERQ', '%'])
        
        
        pdrealiz5 = pdrealiz4.drop(columns=['GROUP_ID'])
        
        
        
        xala = pdrealiz5.groupby(['DATE'])['AHALI_KW','OXUNMA_AHALI','AHALI_AKT','QAHALI_KW','OXUNMA_QAHALI','QAHALI_AKT','ALINAN_KW','TEXBAZA_AKT','ALINAN','REALIZASIYA','FERQ','%'].sum().reset_index(0)
        
        
        print(xala)
        
        
        xala['AHALI_KW'] = xala['AHALI_KW'].round().astype(int)
        xala['AHALI_AKT'] = xala['AHALI_AKT'].round().astype(int)
        xala['QAHALI_KW'] = xala['QAHALI_KW'].round().astype(int)
        xala['QAHALI_AKT'] = xala['QAHALI_AKT'].round().astype(int)
        xala['ALINAN_KW'] = xala['ALINAN_KW'].round().astype(int)
        xala['TEXBAZA_AKT'] = xala['TEXBAZA_AKT'].round().astype(int)
        xala['REALIZASIYA'] = xala['REALIZASIYA'].round().astype(int)
        xala['FERQ'] = xala['FERQ'].round().astype(int)
        xala['%'] = xala['%'].round(2)
        
        
        for index, row in xala.iterrows():
            tmktmtreeser2.insert("", 'end',  values=list(row))
            
            
        
        
        xala.set_index("DATE", inplace = True)
            
            
            
        figure2 = plt.Figure(figsize=(10,4), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, rmktmfram1)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        xala['ALINAN'].plot(kind='line', legend=True, ax=ax2, color='#06065F',marker='o', fontsize=10)
        xala['REALIZASIYA'].plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('TM vs Realizasiya aylar uzre')
        
        
        
        dsss =  int(xala['ALINAN'].sum())
        dsss2 = int(xala['REALIZASIYA'].sum())
        
        
        
        thisdictdd = {
        "ALINAN": [dsss],
        "REALIZASIYA": [dsss2]
        }
        
        
        
        meyitqatov = pd.DataFrame.from_dict(thisdictdd)
        
        
        
        
        figure5 = plt.Figure(figsize=(6.3,4.0), dpi=80)
        ax1 = figure5.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure5, rmktmfram2)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = meyitqatov
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=9)
        ax1.set_title('ALINAN VS REALIZASIYA secilen ay araliginda')
        
        
        ax1.legend(fontsize=8)
        
        
        sql = """SELECT
    'AHALI',
    vw_subother.ddate,
    vw_subscriber_transformer.subid,
    vw_subother.kvth,
    vw_subother.name
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subother.ddate >= TO_DATE(:nm1, 'YYYY-MM-DD')
    AND vw_subother.ddate <= TO_DATE(:nm2, 'YYYY-MM-DD')
    AND NOT ( vw_subother.otherid IN ( '128', '171', '172' ) ) """
        cur2.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur2.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdsubother  =   pd.DataFrame(cazi1,columns = ['AB_TYPE','DATE','AB_KOD','KVTH','AKT_NAME'])
        
        
        sql = """SELECT
    'QAHALI',
    vw_subother.ddate,
    vw_subscriber_transformer.subid,
    vw_subother.kvth,
    vw_subother.name
FROM
    vw_subscriber_transformer
    LEFT JOIN tbl_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
        tbl_transformer.group_id_seq = :grid
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subother.ddate >= TO_DATE(:nm1, 'YYYY-MM-DD')
    AND vw_subother.ddate <= TO_DATE(:nm2, 'YYYY-MM-DD')
     """
        cur1.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        cazi1 = cur1.execute(sql,grid = u ,nm1 = d1,nm2 = d2)
        pdsubother2  =   pd.DataFrame(cazi1,columns = ['AB_TYPE','DATE','AB_KOD','KVTH','AKT_NAME'])
        
        
        frames = [pdsubother, pdsubother2]

        result = pd.concat(frames)
        
        
        
        
        for index, row in result.iterrows():
            tmktmtreeser3.insert("", 'end',  values=list(row))
        
        
        
        dsss =  int(xala['ALINAN'].sum())
        dsss2 = int(xala['REALIZASIYA'].sum())
        
        dsferq = dsss - dsss2
        dsfzz = dsferq * 100 / dsss
        
        
        tmktmalinan1['text'] = 'TM_ALDIGI  ' + str(("{:,}".format(dsss)))
        tmktmalinan2['text'] = 'REALIZASIYA   ' + str(("{:,}".format(dsss2)))
        tmktmalinan3['text'] = 'FERQ   ' + str(("{:,}".format(dsferq)))
        tmktmalinan4['text'] = '%   ' + str(round(dsfzz, 2))

        
        
        
        
        

###############################################################   TAB 2    END   !!!!



###############################################################  TAB 3 NEZARETCI PERFORMANSI  >>>>>>>>>>>>>
tab3sahelist = []
tab3nazalist = []



def tab3date1():
    def print_sel():    
        nazabutadate1['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    
def tab3date2():
    def print_sel():    
        nazabutadate2['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()




def SAHECLEAR():
    

   
   nazatrv1.delete(*nazatrv1.get_children())
   nazacombo2.set('')
   nazacombo3.set('')
   
   for widgets in nazafr1.winfo_children():
     widgets.destroy()
     
   for widgets in nazafr2.winfo_children():
     widgets.destroy()
     
   for widgets in nazafr3.winfo_children():
     widgets.destroy()
   



def SAHE():
    for widgets in nazafr2.winfo_children():
      widgets.destroy()
      
    for widgets in nazafr3.winfo_children():
      widgets.destroy()
      
      
    for widgets in nazafr4.winfo_children():
      widgets.destroy()
    
    for widgets in nazafr1.winfo_children():
      widgets.destroy()
    nazatrv1.delete(*nazatrv1.get_children())
    tab3sahelist.clear()
    nazacombo3.set('')
    
    a =  str(nazacombo1.get())
    b = a[:2]
    print(b)
    
    sql = """SELECT CRYL2UTF((TBL_DIVISION.divisionid||'   --'||TBL_DIVISION.name)) FROM TBL_DIVISION  


where subjectid = :sax """
    cur1.execute(sql,sax = b)
    cezi = cur1.execute(sql,sax = b)
    for i in cezi:
        tab3sahelist.append(i)
    nazacombo2['values'] = tab3sahelist
    
    
def NEZARETCI():
    for widgets in nazafr2.winfo_children():
      widgets.destroy()
    
    for widgets in nazafr3.winfo_children():
      widgets.destroy()
    
    for widgets in nazafr1.winfo_children():
      widgets.destroy()
      
    for widgets in nazafr4.winfo_children():
      widgets.destroy()
      
    nazatrv1.delete(*nazatrv1.get_children())
    tab3nazalist.clear()
    ch = str(nazacombo1.get())
    chh = ch[:2]
    gh = str(nazacombo2.get())
    ghh = gh[1:3]
    
    if gh == '':
        sql = """SELECT
    DISTINCT(CRYL2UTF(tbl_personnels_transformer.personnel_id_seq||'      '||'   '||tbl_personnels.name))
FROM
    tbl_transformer
    LEFT JOIN tbl_personnels_transformer ON tbl_transformer.id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN tbl_personnels ON tbl_personnels_transformer.personnel_id_seq = tbl_personnels.id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_divisionid = tbl_division.divisionid
                              AND tbl_transformer.sales_subjectid = tbl_division.subjectid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND tbl_personnels.date_to IS NULL
    AND tbl_transformer.sales_subjectid = :ijk """
        cur1.execute(sql,ijk = chh)
        cezi = cur1.execute(sql,ijk = chh)
        for i in cezi:
            tab3nazalist.append(i)
        nazacombo3['values'] = tab3nazalist
    else:
        sql = """SELECT
    DISTINCT(CRYL2UTF(tbl_personnels_transformer.personnel_id_seq||'     '||'   '||tbl_personnels.name))
FROM
    tbl_transformer
    LEFT JOIN tbl_personnels_transformer ON tbl_transformer.id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN tbl_personnels ON tbl_personnels_transformer.personnel_id_seq = tbl_personnels.id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_divisionid = tbl_division.divisionid
                              AND tbl_transformer.sales_subjectid = tbl_division.subjectid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND tbl_personnels.date_to IS NULL
    AND tbl_transformer.sales_subjectid = :ijk
    AND tbl_division.divisionid = :koko """
        cur1.execute(sql,ijk = chh,koko = ghh)
        cezi = cur1.execute(sql,ijk = chh,koko = ghh)
        for i in cezi:
            tab3nazalist.append(i)
        nazacombo3['values'] = tab3nazalist
        
        
        
        
def tab3start():

    
    
    for widgets in nazafr1.winfo_children():
      widgets.destroy()
      
    for widgets in nazafr2.winfo_children():
      widgets.destroy()
      
    for widgets in nazafr3.winfo_children():
      widgets.destroy()
      
    for widgets in nazafr4.winfo_children():
      widgets.destroy()
      
      

      
      
      
      
     
      
    
    
    nazatrv1.delete(*nazatrv1.get_children())
    
    
    dat1 = nazabutadate1['text'] 
    dat2 = nazabutadate2['text'] 
    
    
    
    
    
    
    
    nzm = str(nazacombo3.get())
    nzmm = nzm[1:8]
    
    listgrupppp = []
    
    listtrrr    = []
    
    listgruppppkvth = []
    
    listgruppppakt  = []
    
    listtrkvth = []
    
    listtraktt = []
    
    
    
    
    
    if dat1 == 'ILK_TARIX':
        messagebox.showinfo('tarix_sec')
    elif dat2 == 'SON_TARIX':
        messagebox.showinfo('tarix_sec')
    elif  nzmm == '':
        messagebox.showinfo('nezaretci sec')
    else:
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI_KVTH',
    tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    COUNT(vw_subcontrol.kvth)
    
FROM
    tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND NOT ( tbl_transformer.group_id_seq IS NULL )
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcontrol.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subcontrol.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdqahaliqruplu  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI_KVTH',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    COUNT(vw_subcontrol.kvth)
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcontrol.ddate >= TO_DATE(:jn1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:jn2,'YYYY-MM-DD')	
    
GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdqahaliqrupsuz  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI_AKT',
    tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth),
    '   '
    
FROM
    tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND NOT ( tbl_transformer.group_id_seq IS NULL )
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subother.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subother.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdqahaliqrupluakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI_AKT',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth),
    '    '
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subother.ddate >= TO_DATE(:jn1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:jn2,'YYYY-MM-DD')	
    
GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdqahaliqrupsuzakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI_KVTH',
    tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    COUNT(vw_subcontrol.kvth)
    
FROM
    tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND NOT ( tbl_transformer.group_id_seq IS NULL )
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcontrol.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subcontrol.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdahaliqruplu  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI_KVTH',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    COUNT(vw_subcontrol.kvth)
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcontrol.ddate >= TO_DATE(:jn1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:jn2,'YYYY-MM-DD')	
    
GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate) """
        cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdahaliqrupsuz  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI_AKT',
    tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth),
    '   '
    
FROM
    tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND NOT ( tbl_transformer.group_id_seq IS NULL )
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subother.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subother.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')
    AND NOT(vw_subother.otherid IN ('128'))

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdahaliqrupluakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI_AKT',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth),
    '    '
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subother.ddate >= TO_DATE(:jn1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:jn2,'YYYY-MM-DD')	
    AND NOT(vw_subother.otherid IN ('128'))
    
GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate) """
        cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdahaliqrupsuzakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        #########chargee
        
        
        
        sql = """SELECT
    'YIGIM',
    'QAHALI_YIGIM',
    tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcharge.ddate),
    SUM(vw_subcharge.charge),
    '    '
    
FROM
    tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND NOT ( tbl_transformer.group_id_seq IS NULL )
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcharge.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subcharge.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcharge.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcharge.ddate) """
        cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdqahaliqrupluyigim  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'YIGIM',
    'QAHALI_YIGIM',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcharge.ddate),
    SUM(vw_subcharge.charge),
    '      '
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcharge.ddate >= TO_DATE(:jn1,'YYYY-MM-DD') AND vw_subcharge.ddate <= TO_DATE(:jn2,'YYYY-MM-DD')	
    
GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcharge.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcharge.ddate) """
        cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur1.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdqahaliqrupsuzyigim  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'YIGIM',
    'AHALI_YIGIM',
    tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcharge.ddate),
    SUM(vw_subcharge.charge),
    '    '
    
FROM
    tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND NOT ( tbl_transformer.group_id_seq IS NULL )
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcharge.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subcharge.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcharge.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcharge.ddate) """
        cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdahaliqrupluyigim  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'YIGIM',
    'AHALI_YIGIM',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcharge.ddate),
    SUM(vw_subcharge.charge),
    '     '
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_personnels_transformer.transformer_id_seq
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND vw_subscriber_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya
    AND vw_subcharge.ddate >= TO_DATE(:jn1,'YYYY-MM-DD') AND vw_subcharge.ddate <= TO_DATE(:jn2,'YYYY-MM-DD')	
    
GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcharge.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcharge.ddate) """
        cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        cezi = cur2.execute(sql,nazulya = nzmm,jn1 = dat1,jn2 = dat2)
        pdahaliqrupsuzyigim  =   pd.DataFrame(cezi,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])
        
        
        
        
        
        
        
        sql = """SELECT
    tbl_transformer.group_id_seq
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND not(tbl_transformer.group_id_seq IS NULL)
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya """
        cur1.execute(sql,nazulya = nzmm)
        cezi = cur1.execute(sql,nazulya = nzmm)
        for x in cezi:
            listgrupppp.append(x[0])
            
        sql = """SELECT
    tbl_transformer.id_seq
FROM
         tbl_personnels_transformer
    LEFT JOIN tbl_transformer ON tbl_personnels_transformer.transformer_id_seq = tbl_transformer.id_seq
WHERE
    tbl_personnels_transformer.date_to IS NULL
    AND tbl_transformer.group_id_seq IS NULL
    AND tbl_personnels_transformer.personnel_id_seq = :nazulya """
        cur1.execute(sql,nazulya = nzmm)
        cezi = cur1.execute(sql,nazulya = nzmm)
        for kl in cezi:
            listtrrr.append(kl[0])
            
        
        
        listgrupppp = list(dict.fromkeys(listgrupppp))
        
        
        
        
        for pl in listgrupppp:
            print(pl)
            sql = """SELECT
    'ALISH',
    'TEX_KVTH',
    (select gh.name from tbl_transformer_group@dp_QAHALI.barmek.az gh where gh.id_seq = tbl_transformer.group_id_seq) ,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    '    '
    
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE

     vw_subscriber_transformer.date_to IS NULL

    AND vw_subcontrol.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subcontrol.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')
    AND tbl_transformer.group_id_seq = :nazulya

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subcontrol.ddate)    """
            cur3.execute(sql,nazulya = pl,jn1 = dat1,jn2 = dat2)
            cezi = cur3.execute(sql,nazulya = pl,jn1 = dat1,jn2 = dat2)
            for gj in cezi:
                listgruppppkvth.append(gj)
                
                
        for lp in listgrupppp:
            sql = """SELECT
    'ALISH',
    'TEX_AKT',
    (select gh.name from tbl_transformer_group@dp_QAHALI.barmek.az gh where gh.id_seq = tbl_transformer.group_id_seq) ,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth),
    '    '
    
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group ON tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
WHERE

     vw_subscriber_transformer.date_to IS NULL

    AND vw_subother.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subother.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')
    AND tbl_transformer.group_id_seq = :nazulya

GROUP BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate)
    
ORDER BY tbl_transformer_group.name,
    tbl_transformer.group_id_seq,
    LAST_DAY(vw_subother.ddate) """
            cur3.execute(sql,nazulya = lp,jn1 = dat1,jn2 = dat2)
            cezi = cur3.execute(sql,nazulya = lp,jn1 = dat1,jn2 = dat2)
            for uj in cezi:
                listgruppppakt.append(uj)
            
       
        pdahaliqruplutexkw  =   pd.DataFrame(listgruppppkvth,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])    
        pdahaliqruplutexakt  =   pd.DataFrame(listgruppppakt,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])  
        
        
        
        
        
        
        listtrrr = list(dict.fromkeys(listtrrr))
        
        
        
        for bk in listtrrr:
            sql = """SELECT
    'ALISH',
    'TEX_KVTH',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate),
    SUM(vw_subcontrol.kvth),
    '    '
    
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
WHERE

     vw_subscriber_transformer.date_to IS NULL

    AND vw_subcontrol.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subcontrol.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')
    AND tbl_transformer.id_seq = :nazulya

GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subcontrol.ddate)     """
            cur3.execute(sql,nazulya = bk,jn1 = dat1,jn2 = dat2)
            cezi = cur3.execute(sql,nazulya = bk,jn1 = dat1,jn2 = dat2)
            for jn in cezi:
                listtrkvth.append(jn)
                
                
        for bk in listtrrr:
            sql = """SELECT
    'ALISH',
    'TEX_AKT',
    tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate),
    SUM(vw_subother.kvth),
    '    '
    
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON vw_subscriber_transformer.transformer_id_seq = tbl_transformer.id_seq
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
WHERE

     vw_subscriber_transformer.date_to IS NULL

    AND vw_subother.ddate >= TO_DATE(:jn1, 'YYYY-MM-DD')
    AND vw_subother.ddate <= TO_DATE(:jn2, 'YYYY-MM-DD')
    AND tbl_transformer.id_seq = :nazulya

GROUP BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate)
    
ORDER BY tbl_transformer.name,
    tbl_transformer.id_seq,
    LAST_DAY(vw_subother.ddate)      """
            cur3.execute(sql,nazulya = bk,jn1 = dat1,jn2 = dat2)
            cezi = cur3.execute(sql,nazulya = bk,jn1 = dat1,jn2 = dat2)
            for jn in cezi:
                listtraktt.append(jn)
                
        pdahaliqrupsuztexkw  =   pd.DataFrame(listtrkvth,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])    
        pdahaliqrupsuzexakt  =   pd.DataFrame(listtraktt,columns = ['KW_TIP','KV_TYPE','TR_NAME','TR_ID','DDATE','KVTH','OXUNMA'])  
        
        
        
        
                
                
                

        
        
        
        
        
        
        
        
        
        
        #pdqahaliqrupluyigim
        #pdqahaliqrupsuzyigim
        #pdahaliqrupluyigim
        #pdahaliqrupsuzyigim
        
        
        
        result1 = pd.concat([pdqahaliqruplu, pdqahaliqrupsuz, pdqahaliqrupluakt,pdqahaliqrupsuzakt,pdahaliqruplu,pdahaliqrupsuz,pdahaliqrupluakt,pdahaliqrupsuzakt,pdahaliqruplutexkw,pdahaliqruplutexakt,pdahaliqrupsuztexkw,pdahaliqrupsuzexakt,pdqahaliqrupluyigim,pdqahaliqrupsuzyigim,pdahaliqrupluyigim,pdahaliqrupsuzyigim])
        
        
        
        pdbar1all = result1.groupby(['KW_TIP','DDATE'])['KVTH'].sum().reset_index()
        
        
        
        
        
        
        
        #pdbar1all['KVTH'] = pdbar1all['KVTH'].fillna(0)
        
        print(pdbar1all)
        
        
        
        
        pdbar1all2 = pdbar1all.pivot(index='DDATE', columns='KW_TIP', values='KVTH')
        
        
        
        
        
        pdbar1all2['ALISH'] = pdbar1all2['ALISH'].fillna(0)
        pdbar1all2['REALIZASIYA'] = pdbar1all2['REALIZASIYA'].fillna(0)
        pdbar1all2['YIGIM'] = pdbar1all2['YIGIM'].fillna(0)
        
        
        pdbar1all2['FERQ'] = pdbar1all2['ALISH'] - pdbar1all2['REALIZASIYA']
        
        pdbar1all2['%'] = pdbar1all2['FERQ'] * 100 / pdbar1all2['ALISH']
        
        pdbar1all3 = pdbar1all2.reset_index()
        
        
        print(pdbar1all3)
        
        
        
        
        pdbar1all3['ALISH'] = pdbar1all3['ALISH'].round().astype(int)
        pdbar1all3['REALIZASIYA'] = pdbar1all3['REALIZASIYA'].round().astype(int)
        pdbar1all3['FERQ'] = pdbar1all3['FERQ'].round().astype(int)
        pdbar1all3['YIGIM'] = pdbar1all3['YIGIM'].round().astype(int)
        pdbar1all3['%'] = pdbar1all3['%'].round(2)
        
        
        
        
        
        
        for index, row in pdbar1all3.iterrows():
            nazatrv1.insert("", 'end',  values=list(row))
            
            
        pdbar1all3.set_index("DDATE", inplace = True)
            
            
            
        figure2 = plt.Figure(figsize=(5.88,3), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, nazafr1)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        pdbar1all3['ALISH'].plot(kind='line', legend=True, ax=ax2, color='#06065F',marker='o', fontsize=10)
        pdbar1all3['REALIZASIYA'].plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('NƏZARƏTCİNİN ALDİGİ VE SATDİGİ')
        
        
        
        #result1
        
        
        pdbar1allread = result1.groupby(['DDATE','KV_TYPE'])['OXUNMA'].sum().reset_index()
        
        
        pdbar1allread2 = pdbar1allread.pivot(index='DDATE', columns='KV_TYPE', values='OXUNMA')
        
        pdbar1allread3 = pdbar1allread2.reset_index()
        
        pdbar1allread3.set_index("DDATE", inplace = True)
            
            
            
        figure2 = plt.Figure(figsize=(5.88,2), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, nazafr2)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        pdbar1allread3['AHALI_KVTH'].plot(kind='line', legend=True, ax=ax2, color='#06065F',marker='o', fontsize=10)
        
        ax2.set_title('AHALI OXUNMA')
        
        
        
        
        figure2 = plt.Figure(figsize=(5.88,2), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, nazafr3)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        pdbar1allread3['QAHALI_KVTH'].plot(kind='line', legend=True, ax=ax2, color='#06065F',marker='o', fontsize=10)
        
        ax2.set_title('QAHALI OXUNMA')
        
        
        
        
        nazaalish111 = int(pdbar1all2['ALISH'].sum())
        nazarel11 = int(pdbar1all2['REALIZASIYA'].sum())
        nazamoneyy = int(pdbar1all2['YIGIM'].sum())
        
        nazarel11frq = nazaalish111 - nazarel11
        
        nazarel11frqfaiz = nazarel11frq * 100 / nazaalish111
        
        
        
        
        
        nazaallab1['text'] = 'ALINAN             :' + str(("{:,}".format(nazaalish111)))
        nazaallab2['text'] = 'REALIZASIYA   :' + str(("{:,}".format(nazarel11)))
        nazaallab3['text'] = 'FERQ                  :' + str(("{:,}".format(nazarel11frq)))
        nazaallab4['text'] = '%                       :' + str(round(nazarel11frqfaiz, 2))
        nazaallab5['text'] = 'YIGIM               :' + str(("{:,}".format(nazamoneyy)))
        
        
        
        pdbar1alltgm = result1.groupby(['KW_TIP','TR_NAME'])['KVTH'].sum().reset_index()
        
        pdbar1alltgm2 = pdbar1alltgm.pivot(index='TR_NAME', columns='KW_TIP', values='KVTH')
        
        
        
        print(pdbar1alltgm2)
        
        
        pdbar1alltgm2.drop(['YIGIM'], axis = 1, inplace = True)
        
        
        pdbar1alltgm3 = pdbar1alltgm2.reset_index()
        
        
        pdbar1alltgm4 =    pdbar1alltgm3.set_index('TR_NAME')
        
        
        print(pdbar1alltgm4)



        



        figure51 = plt.Figure(figsize=(11,4.5), dpi=100)
        ax1 = figure51.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure51, nazafr4)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = pdbar1alltgm4
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=6)
        ax1.set_title('TM VS REALIZASIYA SECILEN AY ARALIGINDA CEM')


        ax1.legend(fontsize=8)
        
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #with pd.ExcelWriter('TEST9222222333668338.xlsx') as writer:  
         #   pdbar1all2.to_excel(writer, sheet_name='1')
          #  result1.to_excel(writer, sheet_name='2')
            
        
        
       
        
        
#################################################################  tab3 nezaretci end





###################################################                  TAB 4 SAHE 



tab4sahelist = []

def tab4date1():
    def print_sel():    
        sahabutdate1['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    
def tab4date2():
    def print_sel():    
        sahabutdate2['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    
    
    
def SAHECLEARATB4():
    sahtrv1.delete(*sahtrv1.get_children())
    sahtrvnaza1.delete(*sahtrvnaza1.get_children())
    sahtrvktmm1.delete(*sahtrvktmm1.get_children())
    
    sahdaxilolmuyantrv.delete(*sahdaxilolmuyantrv.get_children())
    
    
    
    sahacombo2.set('')
    tab4sahelist.clear()
    
    
    for widgets in sahafr1.winfo_children():
      widgets.destroy()
      
      
    for widgets in sahafr2.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr3.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr4.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr5.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr6.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr7.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr8.winfo_children():
      widgets.destroy()
      
      
      
      
     
    
      
    
    
    
    
      
      
      
    

   
   
   
   

        
        
       



def SAHETAB4():
    
    sahacombo2.set('')
    tab4sahelist.clear()
    sahtrv1.delete(*sahtrv1.get_children())
    sahtrvnaza1.delete(*sahtrvnaza1.get_children())
    
    
    sahtrvktmm1.delete(*sahtrvktmm1.get_children())
    
    sahdaxilolmuyantrv.delete(*sahdaxilolmuyantrv.get_children())
    
    
    
    
    for widgets in sahafr1.winfo_children():
      widgets.destroy()
    
    
    for widgets in sahafr2.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr3.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr4.winfo_children():
      widgets.destroy()
      
      
    for widgets in sahafr5.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr6.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr7.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr8.winfo_children():
      widgets.destroy()
      
      
      
      
    
    
    aa =  str(sahacombo1.get())
    bb = aa[:2]
    print(bb)
    
    sql = """SELECT CRYL2UTF((TBL_DIVISION.divisionid||'   --'||TBL_DIVISION.name)) FROM TBL_DIVISION  


where subjectid = :sax """
    cur1.execute(sql,sax = bb)
    cezi = cur1.execute(sql,sax = bb)
    for i in cezi:
        tab4sahelist.append(i)
    sahacombo2['values'] = tab4sahelist
        
        
        
        
        
        
        
def TAB4START():
    
    for widgets in sahafr2.winfo_children():
      widgets.destroy()
    
    sahtrv1.delete(*sahtrv1.get_children())
    
    
    sahdaxilolmuyantrv.delete(*sahdaxilolmuyantrv.get_children())
    
    sahtrvktmm1.delete(*sahtrvktmm1.get_children())
    
    
    for widgets in sahafr1.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr3.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr4.winfo_children():
      widgets.destroy()
      
      
    for widgets in sahafr5.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr6.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr7.winfo_children():
      widgets.destroy()
      
    for widgets in sahafr8.winfo_children():
      widgets.destroy()
      
    
      
      
      
      
     
      
      
      
      
      
      
      
      
      
      
      
      
    
    
    
   
    
    chh = str(sahacombo1.get())
    chhh = chh[:2]
    ghh = str(sahacombo2.get())
    ghhh = ghh[1:3]
    
    
    print(chhh)
    print(ghhh)
    
    
    dat11 = sahabutdate1['text'] 
    dat21 = sahabutdate2['text'] 
    
    
    
    
    
    datoxunn =  dat21[:8] + '01'
    
    print(datoxunn)
    
    
    print(dat11)
    print(dat21)
    
    if ghhh == '':
        messagebox.showinfo('Diqqət','Sahə Secin')
    elif dat11 == 'ILK_TARIX':
        messagebox.showinfo('Diqqət','Tarix Secin')
    elif dat21 == 'SON_TARIX':
        messagebox.showinfo('Diqqət','Tarix Secin')
    else:
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI',
    'QAHALI_KVTH',
     LAST_DAY(vw_subcontrol.ddate) DDATE,
     tbl_transformer_group.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    COUNT(KVTH)
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcontrol.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq    """
        cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahqahalqruplukw  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI',
    'QAHALI_AKT',
     LAST_DAY(vw_subother.ddate) DDATE,
     tbl_transformer_group.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subother.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq """
        cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahqahalqrupluakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        #######
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI',
    'AHALI_KVTH',
     LAST_DAY(vw_subcontrol.ddate) DDATE,
     tbl_transformer_group.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    COUNT(KVTH)
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcontrol.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq    """
        cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqruplukw  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI',
    'AHALI_AKT',
     LAST_DAY(vw_subother.ddate) DDATE,
     tbl_transformer_group.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subother.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               AND NOT(vw_subother.otherid IN ('128'))
                               
                               
                               GROUP BY   LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq """
        cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqrupluakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        ###########
        
        
        sql = """SELECT
    'ALISH',
    'TEX_BAZA',
    'TEX_BAZA_KW',
     LAST_DAY(vw_subcontrol.ddate) DDATE,
     gj.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    COUNT(KVTH)
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group@dp_QAHALI.barmek.az gj on gj.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcontrol.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcontrol.ddate) ,
                               gj.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subcontrol.ddate) ,
                               gj.name,
    tbl_transformer.id_seq    """
        cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahtexqruplukw  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'ALISH',
    'TEX_BAZA',
    'TEX_BAZA_AKT',
     LAST_DAY(vw_subother.ddate) DDATE,
     gj.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group@dp_QAHALI.barmek.az gj on gj.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subother.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subother.ddate) ,
                               gj.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subother.ddate) ,
                               gj.name,
    tbl_transformer.id_seq """
        cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahaktqrupluakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        ###########################
        
        sql = """SELECT
    'YIGIM',
    'QAHALI',
    'QAHALI_YIGIM',
     LAST_DAY(vw_subcharge.ddate) DDATE,
     tbl_transformer_group.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(charge),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcharge.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcharge.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcharge.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subcharge.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq """
        cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdqhacharge  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'YIGIM',
    'AHALI',
    'AHALI_YIGIM',
     LAST_DAY(vw_subcharge.ddate) DDATE,
     tbl_transformer_group.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(charge),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
    LEFT JOIN tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcharge.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcharge.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND not(tbl_transformer.group_id_seq IS NULL)
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcharge.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq 
    
    ORDER BY LAST_DAY(vw_subcharge.ddate) ,
                               tbl_transformer_group.name,
    tbl_transformer.id_seq """
        cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdahacharge  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ####################  >>>>>>> QRUPSUZ
        
        
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI',
    'QAHALI_KVTH',
     LAST_DAY(vw_subcontrol.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    COUNT(KVTH)
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcontrol.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subcontrol.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahqahalqrupsuzkw  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'QAHALI',
    'QAHALI_AKT',
     LAST_DAY(vw_subother.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subother.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subother.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahqahalqrupsuzakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        #########################
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI',
    'AHALI_KVTH',
     LAST_DAY(vw_subcontrol.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    COUNT(KVTH)
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcontrol.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subcontrol.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqrupsuzkw  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'REALIZASIYA',
    'AHALI',
    'AHALI_AKT',
     LAST_DAY(vw_subother.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subother.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               AND NOT(vw_subother.otherid IN ('128'))
                               
                               
                               GROUP BY   LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subother.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqrupsuzakt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        
        
        #########################
        
        
        sql = """SELECT
    'ALISH',
    'TEX_BAZA',
    'TEX_BAZA_KW',
     LAST_DAY(vw_subcontrol.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    COUNT(KVTH)
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcontrol ON vw_subcontrol.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcontrol.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcontrol.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subcontrol.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqrupsuzalkw  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        sql = """SELECT
    'ALISH',
    'TEX_BAZA',
    'TEX_BAZA_AKT',
     LAST_DAY(vw_subother.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(KVTH),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subother ON vw_subother.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subother.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subother.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subother.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur3.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqrupsuzakttt  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        ############
        
        
        sql = """SELECT
    'YIGIM',
    'QAHALI',
    'QAHALI_YIGIM',
     LAST_DAY(vw_subcharge.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(charge),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcharge.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcharge.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcharge.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subcharge.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahqahalqrupsuzyig  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
        
        
        
        sql = """SELECT
    'YIGIM',
    'AHALI',
    'AHALI_YIGIM',
     LAST_DAY(vw_subcharge.ddate) DDATE,
     tbl_transformer.name TR_NAME,
    tbl_transformer.id_seq ID_SEQ,
    SUM(charge),
    '    '
FROM
         tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN tbl_division ON tbl_transformer.sales_subjectid = tbl_division.subjectid
                               AND tbl_transformer.sales_divisionid = tbl_division.divisionid
    LEFT JOIN vw_subcharge ON vw_subcharge.subid = vw_subscriber_transformer.subid
                               
                               
                               
                               WHERE vw_subscriber_transformer.date_to is null
                               AND vw_subcharge.ddate >= TO_DATE(:yh1,'YYYY-MM-DD') AND vw_subcharge.ddate <= TO_DATE(:yh2,'YYYY-MM-DD')
                               AND tbl_transformer.group_id_seq IS NULL
                               AND tbl_transformer.sales_subjectid = :sb
                               AND tbl_transformer.sales_divisionid = :dv
                               
                               
                               GROUP BY   LAST_DAY(vw_subcharge.ddate) ,
                               tbl_transformer.name ,
    tbl_transformer.id_seq 

    
    ORDER BY LAST_DAY(vw_subcharge.ddate) ,
    tbl_transformer.name ,
    tbl_transformer.id_seq """
        cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        cezi = cur2.execute(sql,sb = chhh,dv = ghhh,yh1 = dat11,yh2 = dat21)
        pdsahahalqrupsuzyig  =   pd.DataFrame(cezi,columns = ['KW_TIP','KW_TIP2','KW_TIP3','DATE','TR_NAME','TR_ID','KVTH','OXUNMA'])
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        result1 = pd.concat([pdsahqahalqruplukw, pdsahqahalqrupluakt, pdsahahalqruplukw, pdsahahalqrupluakt, pdsahtexqruplukw, pdsahaktqrupluakt,pdqhacharge,pdahacharge, pdsahqahalqrupsuzkw, pdsahqahalqrupsuzakt, pdsahahalqrupsuzkw, pdsahahalqrupsuzakt, pdsahahalqrupsuzalkw, pdsahahalqrupsuzakttt, pdsahqahalqrupsuzyig, pdsahahalqrupsuzyig])
        
        
        
        
        
        
        sql = """SELECT
    tbl_transformer.id_seq,
    CRYL2UTF((SELECT tbl_personnels.name from tbl_personnels where tbl_personnels.id_seq = tbl_personnels_transformer.personnel_id_seq and date_to is null)) personel_name
FROM
         tbl_transformer
    LEFT JOIN tbl_personnels_transformer ON tbl_transformer.id_seq = tbl_personnels_transformer.transformer_id_seq
    
    
    where tbl_transformer.sales_subjectid = :sb
    
    and tbl_transformer.sales_divisionid = :dv 
    and tbl_personnels_transformer.date_to  is null"""
        cur1.execute(sql,sb = chhh,dv = ghhh)
        cezi = cur1.execute(sql,sb = chhh,dv = ghhh)
        pdpersname  =   pd.DataFrame(cezi,columns = ['TR_ID','PERSONEL'])
            
            
        result2 = pd.merge(result1, pdpersname, on=['TR_ID'], how='left').reset_index()
        
        
        
        pdalishvssrel = result1.groupby(['KW_TIP','DATE'])['KVTH'].sum().reset_index()
        
        
        
        
        
        
        
        
        
        
        
        
        pdbar1all22 = pdalishvssrel.pivot(index='DATE', columns='KW_TIP', values='KVTH')
        
        
        
        pdbar1all22['ALISH'] = pdbar1all22['ALISH'].fillna(0)
        pdbar1all22['REALIZASIYA'] = pdbar1all22['REALIZASIYA'].fillna(0)
        pdbar1all22['YIGIM'] = pdbar1all22['YIGIM'].fillna(0)
        
        
        pdbar1all22['FERQ'] = pdbar1all22['ALISH'] - pdbar1all22['REALIZASIYA']
        
        pdbar1all22['%'] = pdbar1all22['FERQ'] * 100 / pdbar1all22['ALISH']
        
        pdbar1all222 = pdbar1all22.reset_index()
        
        
        
        
        
        
        
        pdbar1all222['ALISH'] = pdbar1all222['ALISH'].round().astype(int)
        pdbar1all222['REALIZASIYA'] = pdbar1all222['REALIZASIYA'].round().astype(int)
        pdbar1all222['FERQ'] = pdbar1all222['FERQ'].round().astype(int)
        pdbar1all222['YIGIM'] = pdbar1all222['YIGIM'].round().astype(int)
        pdbar1all222['%'] = pdbar1all222['%'].round(2)
        
        
        
        
        
        
        for index, row in pdbar1all222.iterrows():
            sahtrv1.insert("", 'end',  values=list(row))
            
            
        pdbar1all222.set_index("DATE", inplace = True)
            
            
            
        figure2 = plt.Figure(figsize=(5.88,2), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, sahafr1)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        pdbar1all222['ALISH'].plot(kind='line', legend=True, ax=ax2, color='#06065F',marker='o', fontsize=10)
        pdbar1all222['REALIZASIYA'].plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('SAHƏ ALDİGİ VE SATDİGİ')
            
            
            
        relaysqahavsaha = result1.groupby(['KW_TIP3','DATE'])['KVTH'].sum().reset_index()
        
        
        
        relaysqahavsaha2 = relaysqahavsaha.pivot(index='DATE', columns='KW_TIP3', values='KVTH')
        
        
        relaysqahavsaha2['AHALI_AKT'] = relaysqahavsaha2['AHALI_AKT'].fillna(0)
        relaysqahavsaha2['AHALI_KVTH'] = relaysqahavsaha2['AHALI_KVTH'].fillna(0)
        relaysqahavsaha2['AHALI_YIGIM'] = relaysqahavsaha2['AHALI_YIGIM'].fillna(0)
        relaysqahavsaha2['QAHALI_AKT'] = relaysqahavsaha2['QAHALI_AKT'].fillna(0)
        relaysqahavsaha2['QAHALI_KVTH'] = relaysqahavsaha2['QAHALI_KVTH'].fillna(0)
        relaysqahavsaha2['QAHALI_YIGIM'] = relaysqahavsaha2['QAHALI_YIGIM'].fillna(0)
        
        
        
        
        relaysqahavsaha2['AHALI_KW'] = relaysqahavsaha2['AHALI_AKT'] + relaysqahavsaha2['AHALI_KVTH']
        
        relaysqahavsaha2['QAHALI_KW'] = relaysqahavsaha2['QAHALI_AKT'] + relaysqahavsaha2['QAHALI_KVTH']
        
        
        
        
            
            
            
        figure2 = plt.Figure(figsize=(5.88,2), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, sahafr2)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        relaysqahavsaha2['AHALI_KW'].plot(kind='line', legend=True, ax=ax2, color='#A3AB1D',marker='o', fontsize=10)
        relaysqahavsaha2['QAHALI_KW'].plot(kind='line', legend=True, ax=ax2, color='#333511',marker='o', fontsize=10)
        ax2.set_title('AHALI VE Q/AHALI AYLAR UZRE')
        
        
        
        
        saxalish = int(pdbar1all222['ALISH'].sum())
        saxrell = int(pdbar1all222['REALIZASIYA'].sum())
        saxmoney = int(pdbar1all222['YIGIM'].sum())
        
        saxferqq = saxalish - saxrell
        
        saxfiz = saxferqq * 100 / saxalish
        
        
        
        
        
        sahlabb1['text'] = 'ALINAN             :' + str(("{:,}".format(saxalish)))
        sahlabb2['text'] = 'REALIZASIYA   :' + str(("{:,}".format(saxrell)))
        sahlabb3['text'] = 'FERQ                  :' + str(("{:,}".format(saxferqq)))
        sahlabb4['text'] = '%                       :' + str(round(saxfiz, 2))
        sahlabb5['text'] = 'YIGIM               :' + str(("{:,}".format(saxmoney)))
        
        
        
        pdalishreddd = result1.groupby(['KW_TIP3','DATE'])['OXUNMA'].sum().reset_index()
        
        
        
        
        
        
        
        
        
        
        
        
        pdalishreddd22 = pdalishreddd.pivot(index='DATE', columns='KW_TIP3', values='OXUNMA')
        
        
        
        
        
        figure2 = plt.Figure(figsize=(5.88,2), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, sahafr3)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        pdalishreddd22['AHALI_KVTH'].plot(kind='line', legend=True, ax=ax2, color='#A3AB1D',marker='o', fontsize=10)
        
        ax2.set_title('AHALI_OXUNMA')
        
        
        figure2 = plt.Figure(figsize=(5.88,2), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, sahafr4)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        pdalishreddd22['QAHALI_KVTH'].plot(kind='line', legend=True, ax=ax2, color='#333511',marker='o', fontsize=10)
        
        ax2.set_title('QAHALI_OXUNMA')
        
        
        
        
        
        
        #########
        
        
        dssssd =  saxalish
        dsss2sd = saxrell
        
        
        
        thisdictdd = {
        "ALINAN": [dssssd],
        "REALIZASIYA": [dsss2sd]
        }
        
        
        
        meyitqatov = pd.DataFrame.from_dict(thisdictdd)
        
        
        
        
        figure5 = plt.Figure(figsize=(6.3,4.0), dpi=80)
        ax1 = figure5.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure5, sahafr5)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = meyitqatov
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=9)
        ax1.set_title('ALINAN VS REALIZASIYA secilen ay araliginda')
        
        
        ax1.legend(fontsize=8)
        
        
        
        
        
        
        
        gh1 = int(relaysqahavsaha2['AHALI_AKT'].sum())
        gh2 = int(relaysqahavsaha2['AHALI_KVTH'].sum())
        gh3 = int(relaysqahavsaha2['QAHALI_AKT'].sum())
        gh4 = int(relaysqahavsaha2['QAHALI_KVTH'].sum())
        
        
        
        thisdictdd2 = {
        "AHALI_AKT": [gh1],
        "AHALI_KVTH": [gh2],
        "QAHALI_AKT": [gh3],
        "QAHALI_KVTH": [gh4],
        }
        
        
        
        meyitqatov2 = pd.DataFrame.from_dict(thisdictdd2)
        
        
        figure5 = plt.Figure(figsize=(6.3,4.0), dpi=80)
        ax1 = figure5.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure5, sahafr6)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = meyitqatov2
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=9)
        ax1.set_title('REALIZASIYA secilen ay araliginda')
        
        
        ax1.legend(fontsize=8)
        
        
        
        
        
        
        
        pdbar1alltgm333 = result2.groupby(['KW_TIP','PERSONEL'])['KVTH'].sum().reset_index()
        
        pdbar1alltgm333['KVTH'] = pdbar1alltgm333['KVTH'].fillna(0)
        
        
        pdbar1alltgm2333 = pdbar1alltgm333.pivot(index='PERSONEL', columns='KW_TIP', values='KVTH')
        
        
        
        print(pdbar1alltgm2333)
        
        
        
        
        
        
        #sahtrvnaza1
        
        ################
        pdbar1alltgm2333.drop(['YIGIM'], axis = 1, inplace = True)
        
        
        pdbar1alltgm3444 = pdbar1alltgm2333.reset_index()
        
        
        pdbar1alltgm4555 =    pdbar1alltgm3444.set_index('PERSONEL')
        
        
        print(pdbar1alltgm4555)



        



        figure51 = plt.Figure(figsize=(11,6), dpi=100)
        ax1 = figure51.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure51, sahafr7)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = pdbar1alltgm4555
        df1.plot(kind='barh', legend=True, ax=ax1,fontsize=6)
        ax1.set_title('TM VS REALIZASIYA SECILEN AY ARALIGINDA CEM')


        ax1.legend(fontsize=8)
        
        ########################################
        
        
        
        pdbar1alltgm233300 = pdbar1alltgm333.pivot(index='PERSONEL', columns='KW_TIP', values='KVTH')
        
        
        
        
        
        
        
        pdbar1alltgm233300['FERQ'] = pdbar1alltgm233300['ALISH'] - pdbar1alltgm2333['REALIZASIYA']
        pdbar1alltgm233300['%'] = pdbar1alltgm233300['FERQ'] * 100 / pdbar1alltgm2333['ALISH']
        
        
        pdbar1alltgm233300['ALISH'] = pdbar1alltgm233300['ALISH'].round().astype(int)
        pdbar1alltgm233300['REALIZASIYA'] = pdbar1alltgm233300['REALIZASIYA'].round().astype(int)
        pdbar1alltgm233300['FERQ'] = pdbar1alltgm233300['FERQ'].round().astype(int)
        pdbar1alltgm233300['YIGIM'] = pdbar1alltgm233300['YIGIM'].round().astype(int)
        pdbar1alltgm233300['%'] = pdbar1alltgm233300['%'].round(2)
        
        
        johnjones = pdbar1alltgm233300.reset_index()
        
        
        
        for index, row in johnjones.iterrows():
            sahtrvnaza1.insert("", 'end',  values=list(row))
            
            
        #############################
            
        

            
        pdbar1alltgm333456 = result1.groupby(['KW_TIP','TR_NAME','TR_ID'])['KVTH'].sum().reset_index()
        
        pdbar1alltgm3334565 = pdbar1alltgm333456.pivot(index=['TR_NAME','TR_ID'], columns='KW_TIP', values='KVTH')
        
        
        pdbar1alltgm33345653 = pdbar1alltgm3334565.groupby(['TR_NAME'])['ALISH','REALIZASIYA','YIGIM'].sum().reset_index()
        
        
        
        
        
        pdbar1alltgm33345653.drop(['YIGIM'], axis = 1, inplace = True)   #### yigimin legvi sahe uzre tmler baxishi
        
        
        pdbar1alltgm3334565344 = pdbar1alltgm33345653.reset_index()
        
        
        pdbar1alltgm333456534466 =    pdbar1alltgm3334565344.set_index('TR_NAME')
        
        
        
        pdbar1alltgm333456534466.drop(['index'], axis = 1, inplace = True)
        
        
        print(pdbar1alltgm333456534466)



        



        figure51 = plt.Figure(figsize=(15,6), dpi=120)
        ax1 = figure51.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure51, sahafr8)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = pdbar1alltgm333456534466
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=6)
        ax1.set_title('TM VS REALIZASIYA SECILEN AY ARALIGINDA CEM')
        
        
        
        pdbar1alltgm333456534466['FERQ'] = pdbar1alltgm333456534466['ALISH'] - pdbar1alltgm333456534466['REALIZASIYA']
        pdbar1alltgm333456534466['%'] = pdbar1alltgm333456534466['FERQ'] * 100 / pdbar1alltgm333456534466['ALISH']
        
        
        pdbar1alltgm333456534466['ALISH'] = pdbar1alltgm333456534466['ALISH'].round().astype(int)
        pdbar1alltgm333456534466['REALIZASIYA'] = pdbar1alltgm333456534466['REALIZASIYA'].round().astype(int)
        pdbar1alltgm333456534466['FERQ'] = pdbar1alltgm333456534466['FERQ'].round().astype(int)
        pdbar1alltgm333456534466['%'] = pdbar1alltgm333456534466['%'].round().round(2)
        
        
        
        johnjones2 = pdbar1alltgm333456534466.reset_index()
        
        
        
        for index, row in johnjones2.iterrows():
            sahtrvktmm1.insert("", 'end',  values=list(row))

        
            
            
            
        
        ######## daxil olmuyan !
        
        
        
        
        sql = """SELECT
    'TEX_BAZA',
    vw_subcontrol.subid,
    tbl_transformer.name,
    tbl_transformer.id_seq,
    vw_subscriber.status,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and vw_subscriber_meter.ddate = (select max(vw_subscriber_meter.ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid)) partmeter
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
    LEFT JOIN vw_subscriber ON vw_subscriber.subid = vw_subscriber_transformer.subid
WHERE
    vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate < TO_DATE(:vbn,'YYYY-MM-DD')
    AND tbl_transformer.sales_subjectid = :sb
    AND tbl_transformer.sales_divisionid = :dvx
    AND vw_subscriber.status != 'P'
MINUS
SELECT
     'TEX_BAZA',
    vw_subcontrol.subid,
    tbl_transformer.name,
    tbl_transformer.id_seq,
    vw_subscriber.status,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and vw_subscriber_meter.ddate = (select max(vw_subscriber_meter.ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid)) partmeter
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
    LEFT JOIN vw_subscriber ON vw_subscriber.subid = vw_subscriber_transformer.subid
WHERE
    vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >=TO_DATE(:vbn,'YYYY-MM-DD')
    AND tbl_transformer.sales_subjectid = :sb
    AND tbl_transformer.sales_divisionid = :dvx
    AND vw_subscriber.status != 'P' """
        cur3.execute(sql,sb = chhh,dvx = ghhh,vbn = datoxunn)
        cezi = cur3.execute(sql,sb = chhh,dvx = ghhh,vbn = datoxunn)
        pdnotreadtex  =   pd.DataFrame(cezi,columns = ['TYPE','SUBID','TR_NAME','TR_ID','STATUS','METER'])
        
        
        
        sql = """SELECT
    'qahali',
    vw_subcontrol.subid,
    tbl_transformer.name,
    tbl_transformer.id_seq,
    vw_subscriber.status,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and vw_subscriber_meter.ddate = (select max(vw_subscriber_meter.ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid)) partmeter
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
    LEFT JOIN vw_subscriber ON vw_subscriber.subid = vw_subscriber_transformer.subid
WHERE
    vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate < TO_DATE(:vbn,'YYYY-MM-DD')
    AND tbl_transformer.sales_subjectid = :sb
    AND tbl_transformer.sales_divisionid = :dvx
    AND vw_subscriber.status != 'P'
MINUS
SELECT
     'qahali',
    vw_subcontrol.subid,
    tbl_transformer.name,
    tbl_transformer.id_seq,
    vw_subscriber.status,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and vw_subscriber_meter.ddate = (select max(vw_subscriber_meter.ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid)) partmeter
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
    LEFT JOIN vw_subscriber ON vw_subscriber.subid = vw_subscriber_transformer.subid
WHERE
    vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >=TO_DATE(:vbn,'YYYY-MM-DD')
    AND tbl_transformer.sales_subjectid = :sb
    AND tbl_transformer.sales_divisionid = :dvx
    AND vw_subscriber.status != 'P' """
        cur1.execute(sql,sb = chhh,dvx = ghhh,vbn = datoxunn)
        cezi = cur1.execute(sql,sb = chhh,dvx = ghhh,vbn = datoxunn)
        pdnotreadqaha  =   pd.DataFrame(cezi,columns = ['TYPE','SUBID','TR_NAME','TR_ID','STATUS','METER'])
        
        
        
        sql = """SELECT
    'ahali',
    vw_subcontrol.subid,
    tbl_transformer.name,
    tbl_transformer.id_seq,
    vw_subscriber.status,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and vw_subscriber_meter.ddate = (select max(vw_subscriber_meter.ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid)) partmeter
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
    LEFT JOIN vw_subscriber ON vw_subscriber.subid = vw_subscriber_transformer.subid
WHERE
    vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate < TO_DATE(:vbn,'YYYY-MM-DD')
    AND tbl_transformer.sales_subjectid = :sb
    AND tbl_transformer.sales_divisionid = :dvx
    AND vw_subscriber.status != 'P'
MINUS
SELECT
     'ahali',
    vw_subcontrol.subid,
    tbl_transformer.name,
    tbl_transformer.id_seq,
    vw_subscriber.status,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and vw_subscriber_meter.ddate = (select max(vw_subscriber_meter.ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid)) partmeter
FROM
    tbl_transformer
    LEFT JOIN vw_subscriber_transformer ON tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
    LEFT JOIN vw_subscriber ON vw_subscriber.subid = vw_subscriber_transformer.subid
WHERE
    vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >=TO_DATE(:vbn,'YYYY-MM-DD')
    AND tbl_transformer.sales_subjectid = :sb
    AND tbl_transformer.sales_divisionid = :dvx
    AND vw_subscriber.status != 'P' """
        cur2.execute(sql,sb = chhh,dvx = ghhh,vbn = datoxunn)
        cezi = cur2.execute(sql,sb = chhh,dvx = ghhh,vbn = datoxunn)
        pdnotreadaha  =   pd.DataFrame(cezi,columns = ['TYPE','SUBID','TR_NAME','TR_ID','STATUS','METER'])
        
        
        
        
        
       
        result99 = pd.concat([pdnotreadtex , pdnotreadqaha, pdnotreadaha])
        
        
        result100 = pd.merge(result99, pdpersname, on=['TR_ID'], how='left')
        
        
        
        
        
        
        
        for index, row in result100.iterrows():
            sahdaxilolmuyantrv.insert("", 'end',  values=list(row))
        
        
        
        
        
        
        
        
        
        
        
        

            
        
        
        
        
        
        
        
        
        
        
        with pd.ExcelWriter('sahe_uzre.xlsx') as writer:  
            result1.to_excel(writer, sheet_name='r1')
            result2.to_excel(writer, sheet_name='r2')
            pdbar1all22.to_excel(writer, sheet_name='r3')  ###  SAHENIN UMUMI ALISHI VS REALIZASIYA AYLAR UZRE
            relaysqahavsaha2.to_excel(writer, sheet_name='r4')
            pdalishreddd22.to_excel(writer, sheet_name= 'r5')
            pdbar1alltgm233300.to_excel(writer, sheet_name= 'r6')
            pdbar1alltgm333456.to_excel(writer, sheet_name= 'r7')
            pdbar1alltgm3334565.to_excel(writer, sheet_name= 'r8')
            pdbar1alltgm33345653.to_excel(writer, sheet_name= 'r9')
            johnjones2.to_excel(writer, sheet_name= 'r10')
            result99.to_excel(writer, sheet_name= 'daxil_olmuyan_gosdericiler')
         
        
        
        
        

        
        
###################################################  tab 4 end  







######################################################   TAB   5 >>>>>>>>>>>>


def tab5date1():
    

    xetttrvsaxikurd.delete(*xetttrvsaxikurd.get_children())
    
    xetttrvnazulyabn.delete(*xetttrvnazulyabn.get_children())
    xetttrvfr1.delete(*xetttrvfr1.get_children())
    xetttrvfrgrtm.delete(*xetttrvfrgrtm.get_children())
    for widgets in xettfrrr1.winfo_children():
      widgets.destroy()
    for widgets in xettfrrr2.winfo_children():
      widgets.destroy()
      
    for widgets in xettdaxilolmuyandfgfd.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr3.winfo_children():
      widgets.destroy()
    
    for widgets in xettfrrrloss.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrgrtmfgr.winfo_children():
      widgets.destroy()
      
    for widgets in xettnazafrtfvbcv.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrsaxikurdo.winfo_children():
      widgets.destroy()
      
      
      

    def print_sel():    
        xettbutdate1['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    
def tab5date2():
    xetttrvnazulyabn.delete(*xetttrvnazulyabn.get_children())
    xetttrvfr1.delete(*xetttrvfr1.get_children())
    xetttrvfrgrtm.delete(*xetttrvfrgrtm.get_children())
    xetttrvsaxikurd.delete(*xetttrvsaxikurd.get_children())
    for widgets in xettfrrr1.winfo_children():
      widgets.destroy()
    for widgets in xettfrrr2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr3.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrgrtmfgr.winfo_children():
      widgets.destroy()
      
    for widgets in xettnazafrtfvbcv.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrsaxikurdo.winfo_children():
      widgets.destroy()
      
    for widgets in xettdaxilolmuyandfgfd.winfo_children():
      widgets.destroy()
      
      
    def print_sel():    
        xettbutdate2['text'] = cal.selection_get()         
        print(cal.selection_get())  
        top.destroy()      
    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2023, month=1, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()
    
def xetttrvbcllrr():
    xetttrvnazulyabn.delete(*xetttrvnazulyabn.get_children())
    xettserchtrvv.delete(*xettserchtrvv.get_children())
    xetttrvfr1.delete(*xetttrvfr1.get_children())
    xetttrvfrgrtm.delete(*xetttrvfrgrtm.get_children())
    
    xetttrvsaxikurd.delete(*xetttrvsaxikurd.get_children())
    
    for widgets in xettfrrrgrtmfgr.winfo_children():
      widgets.destroy()
      
    for widgets in xettdaxilolmuyandfgfd.winfo_children():
      widgets.destroy()
    
    
    for widgets in xettfrrr1.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr3.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss2.winfo_children():
      widgets.destroy()
      
    for widgets in xettnazafrtfvbcv.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrsaxikurdo.winfo_children():
      widgets.destroy()
        
        
        
        
def xetserchmt():    ########################   

    for widgets in xettdaxilolmuyandfgfd.winfo_children():
      widgets.destroy()
    xetttrvnazulyabn.delete(*xetttrvnazulyabn.get_children())
    xetttrvfr1.delete(*xetttrvfr1.get_children())
    
    xetttrvsaxikurd.delete(*xetttrvsaxikurd.get_children())

    xettserchtrvv.delete(*xettserchtrvv.get_children())
    
    xetttrvfrgrtm.delete(*xetttrvfrgrtm.get_children())
    
    for widgets in xettfrsaxikurdo.winfo_children():
      widgets.destroy()
    
    for widgets in xettnazafrtfvbcv.winfo_children():
      widgets.destroy()
    
    
    
    for widgets in xettfrrrloss.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss2.winfo_children():
      widgets.destroy()
    
    
    for widgets in xettfrrr1.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr3.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrgrtmfgr.winfo_children():
      widgets.destroy()
    
    
    
    
    
    fg =  str(xettcombo1.get())
    xvn = fg[:2]
    
    
    gfr = str(xettcombo2.get())
    
    
    
    
    if gfr == 'Xətt':
        sql = """select 
CRYL2UTF(st.matrix_name),
CRYL2UTF(st.name) ,
st.subid subid ,
st.status,
(select stm.partmeterno from vw_subscriber_meter@dp_texniki.barmek.az stm  where stm.subid = st.subid and stm.ddate = (select max(stm.ddate) from vw_subscriber_meter@dp_texniki.barmek.az stm where stm.subid = st.subid )) meter


from vw_subscriber@dp_texniki.barmek.az st 


where st.subject = :exo

and st.house = '0000'

and st.street in ( '006' , '010')


ORDER BY CRYL2UTF(st.matrix_name)"""
        cur2.execute(sql,exo = xvn)
        cezi = cur2.execute(sql,exo = xvn)
        for dt in cezi: 
            xettserchtrvv.insert("", 'end',
                       values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
        

    elif gfr == 'Birbasha':
        print('birbasha')
    else:
        messagebox.showinfo('diqqet','duzgun secim edin')
        
        
def xettstarrtt():
    xetttrvnazulyabn.delete(*xetttrvnazulyabn.get_children())
    xetttrvfr1.delete(*xetttrvfr1.get_children())
    xetttrvsaxikurd.delete(*xetttrvsaxikurd.get_children())
    
    for widgets in xettdaxilolmuyandfgfd.winfo_children():
      widgets.destroy()
    
    
    
    
    for widgets in xettfrsaxikurdo.winfo_children():
      widgets.destroy()
    
    #xetttrvfr1
    print('mamed')
    
    

    
    for widgets in xettnazafrtfvbcv.winfo_children():
      widgets.destroy()
    
    
    xetttrvfrgrtm.delete(*xetttrvfrgrtm.get_children())
    

    for widgets in xettfrrr1.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrr3.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrloss2.winfo_children():
      widgets.destroy()
      
    for widgets in xettfrrrgrtmfgr.winfo_children():
      widgets.destroy()
    
    
    
    
    selected = xettserchtrvv.focus()
    tempo = xettserchtrvv.item(selected, 'values')
    ush = str(tempo[2])
    
    print(ush)
    
    
    d1 = xettbutdate1['text']
    d2 = xettbutdate2['text']
    
    print(d1)
    print(d2)
    
    
    if d1 == 'ILK_TARIX':
        messagebox.showinfo('tarix_sec')
    elif d2 == 'SON_TARIX':
        messagebox.showinfo('tarix_sec')
    else:
        haci = ush



        listtrtex1 = []

        listtrtex2 = []

        listtrtex3 = []

        listtrtex4 = []

        listtrtex5 = []

        listtrtex6 = []

        listtrtex7 = []


        sql = """select 
            :hac ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :hac
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :hac ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :hac
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null
        """
        cezim = cur3.execute(sql,hac = haci)
        for x in cezim:
            listtrtex1.append(x)
            

            
            
        for pl in listtrtex1:
            sql = """select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :up1
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :up1
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null
         """
            cezim = cur3.execute(sql,up1 = pl[1],saleh = haci)
            for kl in cezim:
                listtrtex2.append(kl)
                


        for klo in listtrtex2:
            sql = """select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :up2
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :up2
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null """
            cezim = cur3.execute(sql,up2 = klo[1],saleh = haci)
            for klpp in cezim:
                listtrtex3.append(klpp)
                
                


        for klon in listtrtex3:
            sql = """select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :up3
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :up3
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null """
            cezim = cur3.execute(sql,up3 = klon[1],saleh = haci)
            for klppp in cezim:
                listtrtex4.append(klppp)
                

        for klonx in listtrtex4:
            sql = """select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :up4
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :up4
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null """
            cezim = cur3.execute(sql,up4 = klonx[1],saleh = haci)
            for klpppj in cezim:
                listtrtex5.append(klpppj)
                
                
        for klonxx in listtrtex5:
            sql = """select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :up5
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :up5
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null """
            cezim = cur3.execute(sql,up5 = klonxx[1],saleh = haci)
            for klpppjd in cezim:
                listtrtex6.append(klpppjd)
                
                
        for klonxxx in listtrtex6:
            sql = """select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            tbl_transformer_group.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq
            left join tbl_transformer_group on tbl_transformer_group.id_seq = tbl_transformer.group_id_seq

            where up_subid = :up6
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  not(tbl_transformer.group_id_seq is null)
        UNION ALL
        select 
            :saleh ,
            vw_subscriber_tree_up.down_subid,
            vw_subscriber_transformer.transformer_id_seq,
            vw_subscriber_transformer.name
            from vw_subscriber_tree_up
            left join vw_subscriber on vw_subscriber.subid = vw_subscriber_tree_up.down_subid
            left join vw_subscriber_transformer on vw_subscriber_transformer.subid = vw_subscriber_tree_up.down_subid
            left join tbl_transformer on tbl_transformer.id_seq = vw_subscriber_transformer.transformer_id_seq

            where up_subid = :up6
            and vw_subscriber_transformer.date_to is null
            and vw_subscriber_tree_up.date_to is null
            and  tbl_transformer.group_id_seq is null """
            cezim = cur3.execute(sql,up6 = klonxxx[1],saleh = haci)
            for klpppjd in cezim:
                listtrtex7.append(klpppjd)
                
                
                
        lastlisttr = listtrtex1 + listtrtex2 + listtrtex3 + listtrtex4 + listtrtex5 + listtrtex6 + listtrtex7 #upsubid - down_subid - tr


        ####################################XETT +   DOWN  _SUBID  + TR_ID   <<<<<<







        listtexbazakwaktplus = []  ###  alis||kw_tip||tr_id||date||kw_tex||kw_akt

        listqahaliibazakwaktplus = []  ###  alis||kw_tip||tr_id||date||kw_x||kw_akt

        listahaliibazakwaktplus = []  ###  alis||kw_tip||tr_id||date||kw_x||kw_akt



        for vbss in lastlisttr:
            sql = """SELECT
            'tm_alish',
            'tex_kw',
            vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subcontrol.ddate),
            sum(NVL(vw_subcontrol.kvth,0)) kw_tex,
            0 kw_akt,
            0 
        FROM
                 vw_subscriber_transformer
            LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
            
            
            WHERE vw_subscriber_transformer.transformer_id_seq = :anb
            AND vw_subcontrol.ddate >= TO_DATE(:t1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:t2,'YYYY-MM-DD')
            and vw_subscriber_transformer.date_to is null
            
            group by  vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subcontrol.ddate)
        UNION ALL
        SELECT
            'tm_alish',
            'tex_akt',
            vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subother.ddate),
            0 kw_tex,
            sum(NVL(vw_subother.kvth,0)) kw_akt,
            0
        FROM
                 vw_subscriber_transformer
            LEFT JOIN vw_subother ON vw_subscriber_transformer.subid = vw_subother.subid
            
            
            WHERE vw_subscriber_transformer.transformer_id_seq = :anb
            AND vw_subother.ddate >= TO_DATE(:t1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:t2,'YYYY-MM-DD')
            and vw_subscriber_transformer.date_to is null
            
            group by  vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subother.ddate) """
            cezim = cur3.execute(sql,t1 = d1,t2 = d2,anb = vbss[2])
            for jn in cezim:
                listtexbazakwaktplus.append(jn)
                
        ######################################################
        for vbssw in lastlisttr:
            sql = """SELECT
            'REALIZASIYA',
            'QAHALI_KW',
            vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subcontrol.ddate),
            sum(ROUND(NVL(vw_subcontrol.kvth,0))) kw_tex,
            0 kw_akt,
            count(ROUND(NVL(vw_subcontrol.kvth,0))) oxunma
        FROM
                 vw_subscriber_transformer
            LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
            
            
            WHERE vw_subscriber_transformer.transformer_id_seq = :anb
            AND vw_subcontrol.ddate >= TO_DATE(:t1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:t2,'YYYY-MM-DD')
            and vw_subscriber_transformer.date_to is null
            
            group by  vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subcontrol.ddate)
        UNION ALL
        SELECT
            'REALIZASIYA',
            'QAHALI_AKT',
            vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subother.ddate),
            0 kw_tex,
            sum(ROUND(NVL(vw_subother.kvth,0))) kw_akt,
            0
        FROM
                 vw_subscriber_transformer
            LEFT JOIN vw_subother ON vw_subscriber_transformer.subid = vw_subother.subid
            
            
            WHERE vw_subscriber_transformer.transformer_id_seq = :anb
            AND vw_subother.ddate >= TO_DATE(:t1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:t2,'YYYY-MM-DD')
            and vw_subscriber_transformer.date_to is null
            
            group by  vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subother.ddate) """
            cezim = cur1.execute(sql,t1 = d1,t2 = d2,anb = vbssw[2])
            for jdn in cezim:
                listqahaliibazakwaktplus.append(jdn)
                
        ###################################################   
        for vbssww in lastlisttr:
            sql = """SELECT
            'REALIZASIYA',
            'AHALI_KW',
            vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subcontrol.ddate),
            sum(ROUND(NVL(vw_subcontrol.kvth,0))) kw_tex,
            0 kw_akt,
            count(ROUND(NVL(vw_subcontrol.kvth,0))) kw_tex
        FROM
                 vw_subscriber_transformer
            LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
            
            
            WHERE vw_subscriber_transformer.transformer_id_seq = :anb
            AND vw_subcontrol.ddate >= TO_DATE(:t1,'YYYY-MM-DD') AND vw_subcontrol.ddate <= TO_DATE(:t2,'YYYY-MM-DD')
            and vw_subscriber_transformer.date_to is null
            
            group by  vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subcontrol.ddate)
        UNION ALL
        SELECT
            'REALIZASIYA',
            'AHALI_AKT',
            vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subother.ddate),
            0 kw_tex,
            sum(ROUND(NVL(vw_subother.kvth,0))) kw_akt,
            0
        FROM
                 vw_subscriber_transformer
            LEFT JOIN vw_subother ON vw_subscriber_transformer.subid = vw_subother.subid
            
            
            WHERE vw_subscriber_transformer.transformer_id_seq = :anb
            AND vw_subother.ddate >= TO_DATE(:t1,'YYYY-MM-DD') AND vw_subother.ddate <= TO_DATE(:t2,'YYYY-MM-DD')
            and vw_subscriber_transformer.date_to is null
            and not(vw_subother.otherid in ('128'))
            
            group by  vw_subscriber_transformer.transformer_id_seq,
            last_day(vw_subother.ddate) """
            cezim = cur2.execute(sql,t1 = d1,t2 = d2,anb = vbssww[2])
            for jdnf in cezim:
                listahaliibazakwaktplus.append(jdnf)
                
                
        listallkwwallbaz = listtexbazakwaktplus + listqahaliibazakwaktplus + listahaliibazakwaktplus




            
            
        pandaskwallall  =   pd.DataFrame(listallkwwallbaz,columns = ['KW_TIP','KW_TIP2','TR_ID','DATE','KW','AKT','OXUNMA'])

        pandasxettdownsub1 = pd.DataFrame(lastlisttr,columns = ['UP_SUBID','DOWN_SUBID','TR_ID','TR_NAME'])


        result1 = pd.merge(pandaskwallall, pandasxettdownsub1, on=['TR_ID'], how='left')


        ####################################XETT +   DOWN  _SUBID  + TR_ID   <<<<<<


        listsaxagroupnm = []    ####   tr_id    ||  sahe   ||   group_name

        listperonxttdf = []     ####   tr_id   ||  person _name

        for vbsser in lastlisttr:
            sql = """SELECT
            tbl_transformer.id_seq,
            CRYL2UTF(tbl_division.name),
            tbl_transformer_group.name AS name1
        FROM
            tbl_transformer
            LEFT JOIN tbl_division ON tbl_transformer.sales_divisionid = tbl_division.divisionid
                                      AND tbl_transformer.sales_subjectid = tbl_division.subjectid
            LEFT JOIN tbl_transformer_group ON tbl_transformer.group_id_seq = tbl_transformer_group.id_seq
            where tbl_transformer.id_seq = :yhj """
            cezim = cur1.execute(sql,yhj = vbsser[2])
            for knm in cezim:
                listsaxagroupnm.append(knm)
                
                
        for vbsserx in lastlisttr:
            sql = """SELECT
            tbl_transformer.id_seq,
           CRYL2UTF( (SELECT NAME FROM TBL_PERSONNELS WHERE TBL_PERSONNELS.ID_SEQ = tbl_personnels_transformer.PERSONNEL_ID_SEQ ) ) PERSONEL
        FROM
            tbl_transformer
            LEFT JOIN tbl_personnels_transformer ON tbl_transformer.id_seq = tbl_personnels_transformer.transformer_id_seq
        WHERE
            tbl_personnels_transformer.date_to IS NULL
            AND tbl_transformer.id_seq = :hlk """
            cezim = cur1.execute(sql,hlk = vbsserx[2])
            for knmx in cezim:
                listperonxttdf.append(knmx)
            
                
                

                
        pdsaxaxty = pd.DataFrame(listsaxagroupnm,columns = ['TR_ID','SAHE','TR_GROUP'])


        pdpersoxtpd = pd.DataFrame(listperonxttdf,columns = ['TR_ID','NEZARETCI'])


        result2 = pd.merge(result1, pdsaxaxty, on=['TR_ID'], how='left')

        result3 = pd.merge(result2, pdpersoxtpd, on=['TR_ID'], how='left')




        sql = """SELECT
            subid,
            LAST_DAY(ddate),
            SUM(round(nvl(pack_subscriber.get_number_from_vstring(string, 'CPW'), 0))) kvth
        FROM
            (
                SELECT
                    subcontrol.subid,
                    subcontrol.ddate,
                    subcontrol.metervalue,
                    pack_subscriber.consumed_values_pack(subcontrol.subid, subcontrol.ddate, subcontrol.metervalue, subcontrol.r_metervalue,
                                                         'N') string,
                    subcontrol.fare,
                    subcontrol.r_fare,
                    subcontrol.verified_ch,
                    subcontrol.r_metervalue,
                    subcontrol.vat_percent,
                    subcontrol.personnel_id_seq
                FROM
                    subcontrol
                WHERE
                        subcontrol.subid = :tom
                    AND subcontrol.ddate >= TO_DATE(:lk1, 'YYYY-MM-DD')
                    AND subcontrol.ddate <= TO_DATE(:lk2, 'YYYY-MM-DD')
            )
        GROUP BY
            subid,
            LAST_DAY(ddate)
            
        UNION ALL

        SELECT
             vw_subother.subid,
            last_day(vw_subother.ddate),
            SUM(ROUND(NVL(vw_subother.kvth,0)))
        FROM
            vw_subother
        WHERE
            vw_subother.subid = :tom
            AND vw_subother.ddate >= TO_DATE(:lk1, 'YYYY-MM-DD')
                    AND vw_subother.ddate <= TO_DATE(:lk2, 'YYYY-MM-DD')
        GROUP BY
            vw_subother.subid,
            last_day(vw_subother.ddate) """
        cezim = cur3.execute(sql,tom = haci,lk1 = d1,lk2 = d2)
        xettkwplusakt = pd.DataFrame(cezim,columns = ['XETT','DATE','XETT_KW'])


        xettkwplusakt2 = xettkwplusakt.groupby(['XETT','DATE'])['XETT_KW'].sum().reset_index()



        result3['KW'] = result3['KW'].fillna(0)
        result3['AKT'] = result3['AKT'].fillna(0)
        result3['KW_LAST'] = result3['KW'] + result3['AKT']


        result4 = result3.groupby(['DATE','KW_TIP'])['KW_LAST'].sum().reset_index()


        result5 = result4.pivot(index='DATE', columns='KW_TIP', values='KW_LAST')


        result6 = pd.merge(xettkwplusakt2, result5, on=['DATE'], how='outer')

        result7 = result6[['DATE', 'XETT_KW','tm_alish','REALIZASIYA']]   
        
        result7['FERQ_TMLER'] = result7['XETT_KW'] - result7['tm_alish']
        result7['FERQ_REALIZASIYA'] = result7['XETT_KW'] - result7['REALIZASIYA']
        result7['%_TMLER'] = result7['FERQ_TMLER'] * 100 / result7['XETT_KW']
        result7['%_REALIZASIYA'] = result7['FERQ_REALIZASIYA'] * 100 / result7['XETT_KW']
        
        
        result7['%_TMLER'] = result7['%_TMLER'].round(2)
        result7['%_REALIZASIYA'] = result7['%_REALIZASIYA'].round(2)
        
        
        result7['FERQ_TMLER'] = result7['FERQ_TMLER'].round().astype(int)
        result7['FERQ_REALIZASIYA'] = result7['FERQ_REALIZASIYA'].round().astype(int)
        
        
        
        
        
        
        ###############
        for index, row in result7.iterrows():
            xetttrvfr1.insert("", 'end',  values=list(row))
            
            
            
       
        
        
        result7.set_index("DATE", inplace = True)
        
        
        figure2 = plt.Figure(figsize=(5.88,2.7), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, xettfrrr1)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        result7['XETT_KW'].plot(kind='line', legend=True, ax=ax2, color='#2EB02E',marker='o', fontsize=10)
        result7['tm_alish'].plot(kind='line', legend=True, ax=ax2, color='#2E67B0',marker='o', fontsize=10)
        result7['REALIZASIYA'].plot(kind='line', legend=True, ax=ax2, color='#AA2A45',marker='o', fontsize=10)
        
        ax2.set_title('XƏTT // TMLER // REALİZASİYA')
        
        
        
        figure2 = plt.Figure(figsize=(5.88,2.7), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, xettfrrrloss)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        result7['FERQ_TMLER'].plot(kind='line', legend=True, ax=ax2, color='#810E26',marker='o', fontsize=10)
        
        
        ax2.set_title('XƏTT VƏ TM ARASİNDA İTGİ')
        
        
        
        figure2 = plt.Figure(figsize=(5.88,2.7), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, xettfrrrloss2)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        result7['FERQ_REALIZASIYA'].plot(kind='line', legend=True, ax=ax2, color='#810E26',marker='o', fontsize=10)
        
        
        ax2.set_title('XƏTT VƏ REALİZASİYA İTGİ')
        
        
        
        
        resultreadxxx = result3.groupby(['DATE','KW_TIP2'])['OXUNMA'].sum().reset_index()


        resultreadxxx2 = resultreadxxx.pivot(index='DATE', columns='KW_TIP2', values='OXUNMA')
        
        
        
        
        
        
        figure2 = plt.Figure(figsize=(5.88,2.7), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, xettfrrr2)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        resultreadxxx2['QAHALI_KW'].plot(kind='line', legend=True, ax=ax2, color='#810E26',marker='o', fontsize=10)
        
        
        ax2.set_title('QAHALİ_OXUNMA')
        
        
        
        
        
        
        
        xettlab1 = int(result7['XETT_KW'].sum())
        xettlab2 = int(result7['tm_alish'].sum())
        xettlab3 = int(result7['REALIZASIYA'].sum())
        
        xettlab4 = xettlab1 - xettlab2
        xettlab5 = xettlab1 - xettlab3
        xettlab6 = xettlab2 - xettlab3
        
        xettlab7 = xettlab4 * 100 / xettlab1  ## tm uzre itgi
        xettlab8 = xettlab5 * 100 / xettlab1  ## xett realizasiya uzre itgi
        xettlab9 = xettlab6 * 100 / xettlab2  ## tmlerin itgisi fazile
        
        
        
        
        
        xetlba1['text'] = 'XƏTT ALDİGİ                                 :' + str(("{:,}".format(xettlab1)))
        xetlba2['text'] = 'TMLER UZRE ALİNAN                    :' + str(("{:,}".format(xettlab2)))
        xetlba3['text'] = 'REALİZASİYA                                :' + str(("{:,}".format(xettlab3)))
        xetlba4['text'] = 'XƏTT VƏ TM FƏRQİ                        :' + str(("{:,}".format(xettlab4)))
        xetlba5['text'] = 'XƏTT VƏ REALİZASİYA FƏRQİ       :' + str(("{:,}".format(xettlab5)))
        xetlba6['text'] = 'TM VƏ REALİZASİYA FƏRQİ           :' + str(("{:,}".format(xettlab6)))
        xetlba7['text'] = 'XETT VS TM   %                             :' + str(round(xettlab7, 2))
        xetlba8['text'] = 'XETT VS REALİZASİYA   %            :' + str(round(xettlab8, 2))
        xetlba9['text'] = 'TM VS REALİZASİYA   %               :' + str(round(xettlab9, 2))
        
        
        
        listxettdgsbhbk = []

        for vbsserxyh in lastlisttr:
            sql = """SELECT
    tbl_transformer.id_seq,
    tbl_transformer.subject,
    (select CRYL2UTF(SUBJECT.NAME) from SUBJECT where SUBJECT.SUBJECTID = tbl_transformer.subject)
FROM
    tbl_transformer
WHERE
    tbl_transformer.id_seq = :salyeshka """
            cezim = cur1.execute(sql,salyeshka = vbsserxyh[2] )
            for cezami in cezim:
                listxettdgsbhbk.append(cezami)
            
        

        pddgsdhbkkps = pd.DataFrame(listxettdgsbhbk,columns = ['TR_ID','SUBJECT','RAYON'])

        result100 = pd.merge(result3, pddgsdhbkkps, on=['TR_ID'], how='outer')
        
        
        
        fazail = ush[:2]
        
        conditions = [
    (result100['SUBJECT'] != fazail),
    (result100['SUBJECT'] == fazail)
]

        values = ['OTURULEN','RAYONUN_SATDIGI']

        result100['TR_RAYON'] = np.select(conditions, values)
        
        
        resultxetttrgr = result100.groupby(['TR_GROUP','KW_TIP'])['KW_LAST'].sum().reset_index()


        resultxetttrgr2 = resultxetttrgr.pivot(index='TR_GROUP', columns='KW_TIP', values='KW_LAST')
        
        resultxetttrgr2['FERQ'] = resultxetttrgr2['tm_alish'] - resultxetttrgr2['REALIZASIYA']
        
        resultxetttrgr2['%'] = resultxetttrgr2['FERQ'] * 100 / resultxetttrgr2['tm_alish']

        
        #resultxetttrgr3 = resultxetttrgr2[['TR_GROUP','tm_alish','REALIZASIYA','FERQ','%']]
        
        
        #xetttrvfrgrtm
        
        resultxetttrgr3 = resultxetttrgr2.reset_index()
        
        #resultxetttrgr4 = resultxetttrgr3[['TR_GROUP','tm_aslih','REALIZASIYA','FERQ','%']]
        
        
        
        resultxetttrgr3['%'] = resultxetttrgr3['%'].round(2)
        
        for index, row in resultxetttrgr3.iterrows():
            xetttrvfrgrtm.insert("", 'end',  values=list(row))
            
            
            
            
       
        
        resultxetttrgr3.drop(['FERQ','%'], axis = 1, inplace = True)
        
        
        
        resultxetttrgr4 = resultxetttrgr3.set_index(['TR_GROUP'])
       



        



        figure51 = plt.Figure(figsize=(15,5), dpi=100)
        ax1 = figure51.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure51, xettfrrrgrtmfgr)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = resultxetttrgr4
        df1.plot(kind='bar', legend=True, ax=ax1,fontsize=6)
        ax1.set_title('TM VS REALIZASIYA SECILEN AY ARALIGINDA CEM')
        
        
        
        
        ##################
        
        resultxetttrnazulya= result100.groupby(['NEZARETCI','KW_TIP'])['KW_LAST'].sum().reset_index()


        resultxetttrnazulya2 = resultxetttrnazulya.pivot(index='NEZARETCI', columns='KW_TIP', values='KW_LAST')
        
        resultxetttrnazulya2['FERQ'] = resultxetttrnazulya2['tm_alish'] - resultxetttrnazulya2['REALIZASIYA']
        
        resultxetttrnazulya2['%'] = resultxetttrnazulya2['FERQ'] * 100 / resultxetttrnazulya2['tm_alish']
        
        resultxetttrnazulya2.reset_index()
        
        #resultxetttrnazulya3 = resultxetttrnazulya2[['NEZARETCI','tm_alish','REALIZASIYA','FERQ','%']]
        
        
        resultxetttrnazulya3 = resultxetttrnazulya2.reset_index()
        
        
        
        resultxetttrnazulya3['%'] = resultxetttrnazulya3['%'].round(2)
        
    
        for index, row in resultxetttrnazulya3.iterrows():
            xetttrvnazulyabn.insert("", 'end',  values=list(row))
            
            
            
        resultxetttrnazulya3.drop(['FERQ','%'], axis = 1, inplace = True)
        
        
        
        resultxetttrnazulya4 = resultxetttrnazulya3.set_index(['NEZARETCI'])
       



        



        figure51 = plt.Figure(figsize=(8,5), dpi=100)
        ax1 = figure51.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure51, xettnazafrtfvbcv)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = resultxetttrnazulya4
        df1.plot(kind='barh', legend=True, ax=ax1,fontsize=6)
        ax1.set_title('NEZARETCI ALDIGI VE OXUDUGU')
        
        
        
        
        
        ###########
        
        resultxettsaxa= result100.groupby(['SAHE','KW_TIP'])['KW_LAST'].sum().reset_index()


        resultxettsax2 = resultxettsaxa.pivot(index='SAHE', columns='KW_TIP', values='KW_LAST')
        
        resultxettsax2['FERQ'] = resultxettsax2['tm_alish'] - resultxettsax2['REALIZASIYA']
        
        resultxettsax2['%'] = resultxettsax2['FERQ'] * 100 / resultxettsax2['tm_alish']
        
        resultxettsax2.reset_index()
        
        
        resultxettsax2['%'] = resultxettsax2['%'].round(2)
        
        
        resultxettsax3 = resultxettsax2.reset_index()
        
        for index, row in resultxettsax3.iterrows():
            xetttrvsaxikurd.insert("", 'end',  values=list(row))
            
            
        #xettfrsaxikurdo
        
        
        resultxettsax3.drop(['FERQ','%'], axis = 1, inplace = True)
        
        
        
        resultxettsax4 = resultxettsax3.set_index(['SAHE'])
       



        



        figure51 = plt.Figure(figsize=(8,5), dpi=100)
        ax1 = figure51.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure51, xettfrsaxikurdo)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = resultxettsax4
        df1.plot(kind='barh', legend=True, ax=ax1,fontsize=6)
        ax1.set_title('SAHE ALDIGI VE OXUDUGU')
        
        
        
        datecezimov =  d2[:8] + '01'
        
        
        listxettdaxilolmuy = []
        
       
        
        for sqw in lastlisttr:
            sql = """SELECT
    'QAHALI',
    vw_subscriber_transformer.subid,
    vw_subscriber_transformer.transformer_id_seq,
    vw_subscriber_transformer.name,
    (select CRYL2UTF(vw_subscriber.surname) from vw_subscriber where vw_subscriber.subid = vw_subscriber_transformer.subid ) surname,
    (select max(vw_subcontrol.ddate) from vw_subcontrol where vw_subcontrol.subid = vw_subscriber_transformer.subid and vw_subscriber_transformer.date_to is null ) son_oxunma,
    (select vw_subscriber_meter.partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) meter,
     (select vw_subscriber_meter.metertype from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) saygac_tip,
    (select vw_subscriber_meter.volt from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) volt,
     (select vw_subscriber_meter.amper from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) amper
FROM
    vw_subscriber_transformer
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
WHERE
        vw_subscriber_transformer.transformer_id_seq = :buxta
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate < TO_DATE(:gunel, 'YYYY-MM-DD')
MINUS
SELECT
     'QAHALI',
    vw_subscriber_transformer.subid,
    vw_subscriber_transformer.transformer_id_seq,
    vw_subscriber_transformer.name,
    (select CRYL2UTF(vw_subscriber.surname) from vw_subscriber where vw_subscriber.subid = vw_subscriber_transformer.subid ) surname,
    (select max(vw_subcontrol.ddate) from vw_subcontrol where vw_subcontrol.subid = vw_subscriber_transformer.subid and vw_subscriber_transformer.date_to is null ) son_oxunma,
    (select partmeterno from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) meter,
    (select vw_subscriber_meter.metertype from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) saygac_tip,
    (select vw_subscriber_meter.volt from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) volt,
     (select vw_subscriber_meter.amper from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid and  vw_subscriber_meter.ddate = (select max(ddate) from vw_subscriber_meter where vw_subscriber_meter.subid = vw_subscriber_transformer.subid )) amper
FROM
    vw_subscriber_transformer
    LEFT JOIN vw_subcontrol ON vw_subscriber_transformer.subid = vw_subcontrol.subid
WHERE
        vw_subscriber_transformer.transformer_id_seq = :buxta
    AND vw_subscriber_transformer.date_to IS NULL
    AND vw_subcontrol.ddate >= TO_DATE(:gunel, 'YYYY-MM-DD') """
            cezim = cur1.execute(sql,buxta = sqw[2],gunel = datecezimov )
            for trcb in cezim:
                listxettdaxilolmuy.append(trcb)
                
                
        
                
                
        pdxettdaxilolynbvg = pd.DataFrame(listxettdaxilolmuy,columns = ['TYPE','KOD','TR_ID','TR_NAME','SURNAME','SON_GOS','METER','METERTIP','VOLT','AMPER'])
                
            
            
            
        #xettdaxilolmuyandfgfd
        
        
        frame = tk.Frame(xettdaxilolmuyandfgfd)
        frame.pack(side = 'bottom',fill='both', expand=True)

        ptwe = Table(frame, showtoolbar=True, showstatusbar=True ,dataframe=pdxettdaxilolynbvg)
        ptwe.show()
        
        
        
        
        
        
        
       
            
            
            
            
        ###############################
            


        
            
            
            
        figure2 = plt.Figure(figsize=(5.88,2.7), dpi=80)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, xettfrrr3)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        resultreadxxx2['AHALI_KW'].plot(kind='line', legend=True, ax=ax2, color='#2EB02E',marker='o', fontsize=10)
        
        
        ax2.set_title('AHALİ_OXUNMA')
            
    
    
    














##################












root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')















tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)



tabControl.add(tab1, text ='Subscriber')
tabControl.add(tab2, text ='TM/KTM')
tabControl.add(tab3, text ='NƏZARƏTÇİ_PERFORMANSI')
tabControl.add(tab4, text ='SAHE_PERFORMANSI')
tabControl.add(tab5, text ='XƏTT')
tabControl.add(tab6, text ='YARIMSTANSIYA')


tabControl.pack(expand = 1, fill ="both")

choose2 =[
'01__  Binəqədi',
'02__  Qaradağ',
'03__  Xəzər',
'04__  Yasamal',
'05__  Sabail',
'06__  Nərimanov',
'07__  Nəsimi',
'08__  Nizami',
'09__  Sabunçu',
'11__  Suraxanı',
'12__  Xətai',
'14__  Cəbrayıl',
'15__  Cəlilabad',
'16__  Daşkəsən',
'17__  Şabran',
'18__  Şirvan',
'19__  Fizuli',
'20__  Gəncə',
'21__  Gədəbəy',
'22__  Goranboy',
'23__  Goycay',
'24__  Hacıqabul',
'25__  Goygol',
'27__  Xacmaz',
'28__  Xocavənd',
'29__  Bağlar',
'30__  İmişli',
'31__  İsmayıllı',
'32__  Kəlbəcər',
'33__  Kürdəmir',
'34__  Qax',
'35__  Qazax',
'36__  Qəbələ',
'37__  Qobustan',
'38__  Qusar',
'39__  Qubadlı',
'40__  Quba',
'41__  Lacin',
'42__  Lənkəran',
'43__  Lerik',
'44__  Masallı',
'45__  Mingəcevir',
 '46__  Naftalan',
'47__  Neftcala',
'48__  Oguz',
'49__  Saatlı',
 '50__  Sumqayıt',
 '51__  Samux',
 '52__  Salyan',
 '53__  Siyəzən',
 '54__  Sabirabad',
'55__  Şəki',
'56__  Şamaxı',
 '57__  Şəmkir',
'58__  Şuşa',
'59__  Tərtər',
'60__  Tovuz',
'61__  Ucar',
'62__  Zaqatala',
'63__  Zərdab',
'64__  Zəngilan',
 '65__  Yardımlı',
'66__  Yevlax',
'73__  Xızı',
'80__  Agdam',
'81__  Agdaş',
'82__  Agcabədi',
'83__  Agstafa',
'84__  Agsu',
 '85__  Astara',
'86__  Balakən',
'87__  Bərdə',
 '88__  Beyləqan',
'89__  Biləsuvar',
'90__  Xırdalan']





################  tab1 subscriber >>>

subscribercombobox1 = ttk.Combobox(tab1, values=choose2,width=33) 
subscribercombobox1.place(x= 0 , y =10)
subscribercombobox1.current(0)


subscriberentry1kod = ttk.Entry(tab1,width = 35)
subscriberentry1kod.place(x = 0, y = 40)


subscriberbut1 = ttk.Button(tab1,text = 'SEARCH')   #########   tab 1 subscriber axdarish buton
subscriberbut1.place(x = 0, y = 70)



###################################################################      TAB2 TM/KTM >>>


tmktmcombobox = ttk.Combobox(tab2, values=choose2,width=33) 
tmktmcombobox.place(x= 0 , y =10)
tmktmcombobox.current(0)

tmktmentry = ttk.Entry(tab2,width = 35)
tmktmentry.place(x = 0, y = 40)

tmktmbut1 = ttk.Button(tab2,text = 'SEARCH',command = tmktmserch)   #########   tab 2  TM AXDARİSH BUT
tmktmbut1.place(x = 0, y = 70)


tmktmbut2 = ttk.Button(tab2,text = 'START',command = tab2start)   #########   tab 2 START
tmktmbut2.place(x = 80, y = 70)

tmktmbutdate1 = ttk.Button(tab2,text = 'ILK_TARIX',command = tab2date1 )   #########   tab 2 START
tmktmbutdate1.place(x = 160, y = 70)

tmktmbutdate2 = ttk.Button(tab2,text = 'SON_TARIX',command = tab2date2)   #########   tab 2 START
tmktmbutdate2.place(x = 240, y = 70)




rmktmfram1 = ttk.Frame(tab2)
rmktmfram1.place(x = 0 , y = 290)


rmktmfram2 = ttk.Frame(tab2)
rmktmfram2.place(x = 730 , y = 290)




tmktmbutahalicount = ttk.Label(tab2,text = "",font = 'Verdana 12 bold')
tmktmbutahalicount.place(x = 0,y = 300)



tmktmalinan1 = ttk.Label(tab2,text = "TM_ALDIGI:",font ="Verdana 10 bold")
tmktmalinan1.place(x = 350, y = 0)



tmktmalinan2 = ttk.Label(tab2,text = "REALIZASIYA:",font ="Verdana 10 bold")
tmktmalinan2.place(x = 590, y = 0)

tmktmalinan3 = ttk.Label(tab2,text = "FERQ:",font ="Verdana 10 bold")
tmktmalinan3.place(x = 830, y = 0)



tmktmalinan4 = ttk.Label(tab2,text = "%:",font ="Verdana 10 bold")
tmktmalinan4.place(x = 1070, y = 0)






tmktmtreeser = ttk.Treeview(tab2, columns=(1, 2, 3, 4), show='headings', height=8)
tmktmtreeser.place(x = 0, y = 100)


tmktmtreeser.heading(1, text="TR_NAME")
tmktmtreeser.heading(2, text="SAHƏ")
tmktmtreeser.heading(3, text="RAYON_İD")
tmktmtreeser.heading(4, text="GROUP_İD")





tmktmtreeser.column("1", width = 100, anchor ='c')     
tmktmtreeser.column("2", width = 120, anchor ='c')  
tmktmtreeser.column("3", width = 50, anchor ='c')  
tmktmtreeser.column("4", width = 80, anchor ='c')  





tmktmtreeser2 = ttk.Treeview(tab2, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show='headings', height=8)
tmktmtreeser2.place(x = 360, y = 100)


tmktmtreeser2.heading(1, text="DATE")
tmktmtreeser2.heading(2, text="AHALI_KW")
tmktmtreeser2.heading(3, text="OXUNMA_AHALI")
tmktmtreeser2.heading(4, text="AHALI_AKT")
tmktmtreeser2.heading(5, text="QAHALI_KW")
tmktmtreeser2.heading(6, text="OXUNMA_QAHALI")
tmktmtreeser2.heading(7, text="QAHALI_AKT")
tmktmtreeser2.heading(8, text="TEXBAZA_KW")
tmktmtreeser2.heading(9, text="TEXBAZA_AKT")
tmktmtreeser2.heading(10, text="ALINAN")
tmktmtreeser2.heading(11, text="REALIZASIYA")
tmktmtreeser2.heading(12, text="FERQ")
tmktmtreeser2.heading(13, text="%")







tmktmtreeser2.column("1", width = 67, anchor ='c')     
tmktmtreeser2.column("2", width = 80, anchor ='c')  
tmktmtreeser2.column("3", width = 80, anchor ='c')  
tmktmtreeser2.column("4", width = 80, anchor ='c')  
tmktmtreeser2.column("5", width = 80, anchor ='c')  
tmktmtreeser2.column("6", width = 80, anchor ='c')  
tmktmtreeser2.column("7", width = 80, anchor ='c')  
tmktmtreeser2.column("8", width = 80, anchor ='c')  
tmktmtreeser2.column("9", width = 80, anchor ='c')  
tmktmtreeser2.column("10", width = 80, anchor ='c')  
tmktmtreeser2.column("11", width = 80, anchor ='c')  
tmktmtreeser2.column("12", width = 80, anchor ='c')  
tmktmtreeser2.column("13", width = 80, anchor ='c')  




labfram111 = tk.LabelFrame(tab2,text = 'AKTLAR',width = 420,height = 320,bg = "#FFFFFF",font = "Verdana 10 bold",fg = "black")
labfram111.place(x = 1220,y = 290)




tmktmtreeser3 = ttk.Treeview(labfram111, columns=(1, 2, 3, 4, 5), show='headings', height=8)
tmktmtreeser3.place(x = 10, y = 10)


tmktmtreeser3.heading(1, text="AB_TYPE")
tmktmtreeser3.heading(2, text="DATE")
tmktmtreeser3.heading(3, text="AB_KOD")
tmktmtreeser3.heading(4, text="KVTH")
tmktmtreeser3.heading(5, text="AKT_NOVU")


tmktmtreeser3.column("1", width = 67, anchor ='c')     
tmktmtreeser3.column("2", width = 67, anchor ='c')  
tmktmtreeser3.column("3", width = 70, anchor ='c')  
tmktmtreeser3.column("4", width = 70, anchor ='c')  
tmktmtreeser3.column("5", width = 80, anchor ='c')






#####################################################################   TAB   2  END


#####################################################################   TAB   3 NEZARETCI PERF   >>>>>>>>>



nazacombo1 = ttk.Combobox(tab3, values=choose2,width=37,postcommand = SAHECLEAR) 
nazacombo1.place(x= 0 , y =10)
nazacombo1.current(0)


nazacombo2 = ttk.Combobox(tab3, width = 37,postcommand = SAHE)   ######SAHE
nazacombo2.place(x = 0 , y = 30)

#SAHE

nazacombo3 = ttk.Combobox(tab3, width = 37,postcommand = NEZARETCI   ) ######## NEZARETCI
nazacombo3.place(x = 0 , y = 50)
                            
                            #postcommand=house)
                            
nazabutadate1 = ttk.Button(tab3,text = 'ILK_TARIX',command = tab3date1 )   #########   
nazabutadate1.place(x = 80, y = 70)

nazabutadate2 = ttk.Button(tab3,text = 'SON_TARIX',command = tab3date2 )   #########  
nazabutadate2.place(x = 160, y = 70)

nazabutstart = ttk.Button(tab3,text = 'START' ,command = tab3start)   #########  
nazabutstart.place(x = 0, y = 70)



nazatrv1 = ttk.Treeview(tab3, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)
nazatrv1.place(x = 245, y = 10)


nazatrv1.heading(1, text="DATE")
nazatrv1.heading(2, text="ALISH")
nazatrv1.heading(3, text="REALIZASIYA")
nazatrv1.heading(4, text="YIGIM")
nazatrv1.heading(5, text="FERQ")
nazatrv1.heading(6, text="%")








nazatrv1.column("1", width = 67, anchor ='c')     
nazatrv1.column("2", width = 80, anchor ='c')  
nazatrv1.column("3", width = 80, anchor ='c')  
nazatrv1.column("4", width = 80, anchor ='c')  
nazatrv1.column("5", width = 80, anchor ='c') 
nazatrv1.column("6", width = 80, anchor ='c') 



nazafr1 = ttk.Frame(tab3)
nazafr1.place(x = 245 , y = 200)



nazafr2 = ttk.Frame(tab3)
nazafr2.place(x = 245 , y = 440)


nazafr3 = ttk.Frame(tab3)
nazafr3.place(x = 245 , y = 600)


nazafr4 = ttk.Frame(tab3)
nazafr4.place(x = 800 , y = 10)




nazaallab1 = ttk.Label(tab3,text = "ALINAN :",font ="Verdana 10 bold")
nazaallab1.place(x = 0, y = 200)


nazaallab2 = ttk.Label(tab3,text = "REALIZASIYA:",font ="Verdana 10 bold")
nazaallab2.place(x = 0, y = 220)

nazaallab3 = ttk.Label(tab3,text = "FƏRQ:",font ="Verdana 10 bold")
nazaallab3.place(x = 0, y = 240)

nazaallab4 = ttk.Label(tab3,text = "İTGİ %:",font ="Verdana 10 bold")
nazaallab4.place(x = 0, y = 260)


nazaallab5 = ttk.Label(tab3,text = "YIĞIM:",font ="Verdana 10 bold")
nazaallab5.place(x = 0, y = 280)


####################################
####################################
####################################








############################################    tab 4



tabControl3 = ttk.Notebook(tab4)
tabx81 = ttk.Frame(tabControl3)
tabx82 = ttk.Frame(tabControl3)
tabx83 = ttk.Frame(tabControl3)
tabx84 = ttk.Frame(tabControl3)




tabControl3.add(tabx81, text ='Sahə Ümumi')
tabControl3.add(tabx82, text ='Nəzarətçilər')
tabControl3.add(tabx83, text ='TM/KTM')
tabControl3.add(tabx84, text ='Sahə üzrə daxil olmayan gos')


tabControl3.pack(expand = 1, fill ="both")



nazabutstart = ttk.Button(tabx81,text = 'START',command = TAB4START )   #########  
nazabutstart.place(x = 0, y = 51)


sahabutdate1 = ttk.Button(tabx81,text = 'ILK_TARIX',command = tab4date1 )   #########   
sahabutdate1.place(x = 80, y = 51)

sahabutdate2 = ttk.Button(tabx81,text = 'SON_TARIX',command = tab4date2 )   #########  
sahabutdate2.place(x = 160, y = 51)


sahacombo1 = ttk.Combobox(tabx81, values=choose2,width=37,postcommand = SAHECLEARATB4) 
sahacombo1.place(x= 0 , y =10)
sahacombo1.current(0)


sahacombo2 = ttk.Combobox(tabx81, width = 37,postcommand = SAHETAB4)   ######SAHE
sahacombo2.place(x = 0 , y = 30)





sahtrv1 = ttk.Treeview(tabx81, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)
sahtrv1.place(x = 245, y = 10)


sahtrv1.heading(1, text="DATE")
sahtrv1.heading(2, text="ALISH")
sahtrv1.heading(3, text="REALIZASIYA")
sahtrv1.heading(4, text="YIGIM")
sahtrv1.heading(5, text="FERQ")
sahtrv1.heading(6, text="%")











sahtrv1.column("1", width = 67, anchor ='c')     
sahtrv1.column("2", width = 80, anchor ='c')  
sahtrv1.column("3", width = 80, anchor ='c')  
sahtrv1.column("4", width = 80, anchor ='c')  
sahtrv1.column("5", width = 80, anchor ='c') 
sahtrv1.column("6", width = 80, anchor ='c') 



sahafr1 = ttk.Frame(tabx81)
sahafr1.place(x = 245 , y = 200)


sahafr2 = ttk.Frame(tabx81)
sahafr2.place(x = 245 , y = 360)

sahafr3 = ttk.Frame(tabx81)
sahafr3.place(x = 245 , y = 520)

sahafr4 = ttk.Frame(tabx81)
sahafr4.place(x = 245 , y = 680)

sahafr5 = ttk.Frame(tabx81)
sahafr5.place(x = 720 , y = 10)



sahafr6 = ttk.Frame(tabx81)
sahafr6.place(x = 1250 , y = 10)



########


sahafr7 = ttk.Frame(tabx82)
sahafr7.place(x = 0 , y = 200)





sahlabb1 = ttk.Label(tabx81,text = "ALINAN :",font ="Verdana 10 bold")
sahlabb1.place(x = 0, y = 200)


sahlabb2 = ttk.Label(tabx81,text = "REALIZASIYA:",font ="Verdana 10 bold")
sahlabb2.place(x = 0, y = 220)

sahlabb3 = ttk.Label(tabx81,text = "FƏRQ:",font ="Verdana 10 bold")
sahlabb3.place(x = 0, y = 240)

sahlabb4 = ttk.Label(tabx81,text = "İTGİ %:",font ="Verdana 10 bold")
sahlabb4.place(x = 0, y = 260)


sahlabb5 = ttk.Label(tabx81,text = "YIĞIM:",font ="Verdana 10 bold")
sahlabb5.place(x = 0, y = 280)


sahtrvnaza1 = ttk.Treeview(tabx82, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)
sahtrvnaza1.place(x = 0, y = 10)


sahtrvnaza1.heading(1, text="NEZARETCI")
sahtrvnaza1.heading(2, text="ALISH")
sahtrvnaza1.heading(3, text="REALIZASIYA")
sahtrvnaza1.heading(4, text="YIGIM")
sahtrvnaza1.heading(5, text="FERQ")
sahtrvnaza1.heading(6, text="%")











sahtrvnaza1.column("1", width = 200, anchor ='c')     
sahtrvnaza1.column("2", width = 100, anchor ='c')  
sahtrvnaza1.column("3", width = 100, anchor ='c')  
sahtrvnaza1.column("4", width = 100, anchor ='c')  
sahtrvnaza1.column("5", width = 100, anchor ='c') 
sahtrvnaza1.column("6", width = 100, anchor ='c') 


sahtrvktmm1 = ttk.Treeview(tabx83, columns=(1, 2, 3, 4, 5), show='headings', height=8)
sahtrvktmm1.place(x = 0, y = 10)


sahtrvktmm1.heading(1, text="TM/KTM")
sahtrvktmm1.heading(2, text="ALISH")
sahtrvktmm1.heading(3, text="REALIZASIYA")
sahtrvktmm1.heading(4, text="FERQ")
sahtrvktmm1.heading(5, text="%")











sahtrvktmm1.column("1", width = 200, anchor ='c')     
sahtrvktmm1.column("2", width = 100, anchor ='c')  
sahtrvktmm1.column("3", width = 100, anchor ='c')  
sahtrvktmm1.column("4", width = 100, anchor ='c')  
sahtrvktmm1.column("5", width = 100, anchor ='c') 




sahafr8 = ttk.Frame(tabx83)
sahafr8.place(x = 0 , y = 200)



sahdaxilolmuyantrv = ttk.Treeview(tabx84, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=8)
sahdaxilolmuyantrv.place(x = 0, y = 10)


sahdaxilolmuyantrv.heading(1, text="TYPE")
sahdaxilolmuyantrv.heading(2, text="SUBID")
sahdaxilolmuyantrv.heading(3, text="TR_NAME")
sahdaxilolmuyantrv.heading(4, text="TR_ID")
sahdaxilolmuyantrv.heading(5, text="STATUS")
sahdaxilolmuyantrv.heading(6, text="METER")
sahdaxilolmuyantrv.heading(7, text="NEZARETCI")











sahdaxilolmuyantrv.column("1", width = 150, anchor ='c')     
sahdaxilolmuyantrv.column("2", width = 150, anchor ='c')  
sahdaxilolmuyantrv.column("3", width = 150, anchor ='c')  
sahdaxilolmuyantrv.column("4", width = 150, anchor ='c')  
sahdaxilolmuyantrv.column("5", width = 150, anchor ='c') 
sahdaxilolmuyantrv.column("6", width = 150, anchor ='c') 
sahdaxilolmuyantrv.column("7", width = 150, anchor ='c')
#####################################################################   TAB 4 END



###########################################################>>>>>>>>>> TAB 5 XETT >>>>>>>>>>


choose3 =[
'Xətt',
'Birbasha'
]


tabControl4 = ttk.Notebook(tab5)
tabx811 = ttk.Frame(tabControl4)
tabx822 = ttk.Frame(tabControl4)
tabx833 = ttk.Frame(tabControl4)
tabx844 = ttk.Frame(tabControl4)
tabx855 = ttk.Frame(tabControl4)




tabControl4.add(tabx811, text ='XETT Ümumi')
tabControl4.add(tabx822, text ='TMLER_GROUP')
tabControl4.add(tabx833, text ='TMLER_ID UZRE')
tabControl4.add(tabx844, text ='NEZARETCI + SAHE')
tabControl4.add(tabx855, text ='DAXIL_OLMUYAN_GOS')


tabControl4.pack(expand = 1, fill ="both")



xettcombo1 = ttk.Combobox(tabx811, values=choose2,width=37, postcommand = xetttrvbcllrr) 
xettcombo1.place(x= 0 , y =10)
xettcombo1.current(0)


xettcombo2 = ttk.Combobox(tabx811, values=choose3, width = 37, postcommand = xetttrvbcllrr)   
xettcombo2.place(x = 0 , y = 30)
xettcombo2.current(0)




xetbut1 = ttk.Button(tabx811,text = 'SEARCH',command = xetserchmt)   #########   
xetbut1.place(x = 0, y = 52)


xetbut2 = ttk.Button(tabx811,text = 'START',command = xettstarrtt)   #########   
xetbut2.place(x = 80, y = 52)

xettbutdate1 = ttk.Button(tabx811,text = 'ILK_TARIX',command = tab5date1 )   #########  
xettbutdate1.place(x = 160, y = 52)

xettbutdate2 = ttk.Button(tabx811,text = 'SON_TARIX',command = tab5date2)   #########   
xettbutdate2.place(x = 240, y = 52)





xettserchtrvv = ttk.Treeview(tabx811, columns=(1, 2, 3, 4, 5), show='headings', height=8)
xettserchtrvv.place(x = 0, y = 83)


xettserchtrvv.heading(1, text="YS")
xettserchtrvv.heading(2, text="XƏTT")
xettserchtrvv.heading(3, text="SUBİD")
xettserchtrvv.heading(4, text="STATUS")
xettserchtrvv.heading(5, text="METER")





xettserchtrvv.column("1", width = 170, anchor ='c')     
xettserchtrvv.column("2", width = 140, anchor ='c')  
xettserchtrvv.column("3", width = 100, anchor ='c')  
xettserchtrvv.column("4", width = 30, anchor ='c')  
xettserchtrvv.column("5", width = 100, anchor ='c')  



xetttrvfr1 = ttk.Treeview(tabx811, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=8)
xetttrvfr1.place(x = 550, y = 83)


xetttrvfr1.heading(1, text="DATE")
xetttrvfr1.heading(2, text="XETT_KW")
xetttrvfr1.heading(3, text="TMLER_UZRE_ALISH")
xetttrvfr1.heading(4, text="REALIZASIYA")
xetttrvfr1.heading(5, text="FERQ_TMLER")
xetttrvfr1.heading(6, text="FERQ_REALIZASIYA")
xetttrvfr1.heading(7, text="%_TM")
xetttrvfr1.heading(8, text="%_REALIZASIYA")






xetttrvfr1.column("1", width = 69, anchor ='c')     
xetttrvfr1.column("2", width = 120, anchor ='c')  
xetttrvfr1.column("3", width = 120, anchor ='c')  
xetttrvfr1.column("4", width = 120, anchor ='c')  
xetttrvfr1.column("5", width = 120, anchor ='c') 
xetttrvfr1.column("6", width = 120, anchor ='c') 
xetttrvfr1.column("7", width = 120, anchor ='c') 
xetttrvfr1.column("8", width = 120, anchor ='c') 




xettfrrr1 = ttk.Frame(tabx811)
xettfrrr1.place(x = 400 , y = 275)


xettfrrr2 = ttk.Frame(tabx811)
xettfrrr2.place(x = 400 , y = 500)


xettfrrr3 = ttk.Frame(tabx811)
xettfrrr3.place(x = 400 , y = 725)


xettfrrrloss = ttk.Frame(tabx811)
xettfrrrloss.place(x = 890 , y = 275)

xettfrrrloss2 = ttk.Frame(tabx811)
xettfrrrloss2.place(x = 890 , y = 500)



xetlba1 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba1.place(x = 0, y = 310)


xetlba2 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba2.place(x = 0, y = 330)

xetlba3 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba3.place(x = 0, y = 350)

xetlba4 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba4.place(x = 0, y = 370)


xetlba5 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba5.place(x = 0, y = 390)

xetlba6 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba6.place(x = 0, y = 410)

xetlba7 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba7.place(x = 0, y = 430)

xetlba8 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba8.place(x = 0, y = 450)

xetlba9 = ttk.Label(tabx811,text = "",font ="Verdana 8 bold")
xetlba9.place(x = 0, y = 470)



xetttrvfrgrtm = ttk.Treeview(tabx822, columns=(1, 2, 3, 4, 5), show='headings', height=8)
xetttrvfrgrtm.place(x = 0, y = 10)


xetttrvfrgrtm.heading(1, text="TR_NAME")
xetttrvfrgrtm.heading(2, text="REALIZASIYA")
xetttrvfrgrtm.heading(3, text="TM_ALISH")
xetttrvfrgrtm.heading(4, text="FERQ")
xetttrvfrgrtm.heading(5, text="%")







xetttrvfrgrtm.column("1", width = 120, anchor ='c')     
xetttrvfrgrtm.column("2", width = 120, anchor ='c')  
xetttrvfrgrtm.column("3", width = 120, anchor ='c')  
xetttrvfrgrtm.column("4", width = 120, anchor ='c')  
xetttrvfrgrtm.column("5", width = 120, anchor ='c') 




xettfrrrgrtmfgr = ttk.Frame(tabx822)
xettfrrrgrtmfgr.place(x = 0 , y = 300)



xetttrvnazulyabn = ttk.Treeview(tabx844, columns=(1, 2, 3, 4, 5), show='headings', height=8)
xetttrvnazulyabn.place(x = 0, y = 10)


xetttrvnazulyabn.heading(1, text="NEZARETCI")
xetttrvnazulyabn.heading(2, text="REALIZASIYA")
xetttrvnazulyabn.heading(3, text="TM_ALISH")
xetttrvnazulyabn.heading(4, text="FERQ")
xetttrvnazulyabn.heading(5, text="%")







xetttrvnazulyabn.column("1", width = 120, anchor ='c')     
xetttrvnazulyabn.column("2", width = 120, anchor ='c')  
xetttrvnazulyabn.column("3", width = 120, anchor ='c')  
xetttrvnazulyabn.column("4", width = 120, anchor ='c')  
xetttrvnazulyabn.column("5", width = 120, anchor ='c') 


xettnazafrtfvbcv = ttk.Frame(tabx844)
xettnazafrtfvbcv.place(x = 0 , y = 300)


xetttrvsaxikurd = ttk.Treeview(tabx844, columns=(1, 2, 3, 4, 5), show='headings', height=8)
xetttrvsaxikurd.place(x = 1100, y = 10)


xetttrvsaxikurd.heading(1, text="SAHE")
xetttrvsaxikurd.heading(2, text="REALIZASIYA")
xetttrvsaxikurd.heading(3, text="TM_ALISH")
xetttrvsaxikurd.heading(4, text="FERQ")
xetttrvsaxikurd.heading(5, text="%")







xetttrvsaxikurd.column("1", width = 120, anchor ='c')     
xetttrvsaxikurd.column("2", width = 120, anchor ='c')  
xetttrvsaxikurd.column("3", width = 120, anchor ='c')  
xetttrvsaxikurd.column("4", width = 120, anchor ='c')  
xetttrvsaxikurd.column("5", width = 120, anchor ='c') 



xettfrsaxikurdo = ttk.Frame(tabx844)
xettfrsaxikurdo.place(x = 1100 , y = 300)



xettdaxilolmuyandfgfd = ttk.Frame(tabx855,width = 1920 , height = 1080)
xettdaxilolmuyandfgfd.place(x = 0 , y = 0)








root.title('Enerji Alish və Balans İdarəsi')
root.state('zoom')
root.mainloop()












































