# Line-bot  

### 2020/03/03
```
* 1318:  
	* 完成修改，網頁正常執行，加入Readme.txt  
```
### 2020/03/09
```
* 1509:  
	* 新增 data.csv 完整的資料csv檔
	* 修改 datalist.py 修改抓取資料的檔案，將cosurl -> data
	* 上傳Heroku 並完成執行測試
```
### 2020/03/10
```
* 0212:  
	* 修改 utoken.py 移出VER
	* 新增 使用者輸入後判定資料位置(level())
	* 當使用者輸入出現錯誤時可以直接點選其他選項，並可以直接覆蓋掉原有的選項
* 1230:
	* 移除 modelCode.py 移除(第一段)文字
	* 修改 modelCode.py aroma() label 文字增加 舉例文字(ex:...)
	* 修改 modelCode.py tenMod() 移除(還沒想到)按鈕
```
### 2020/03/11
```
* 1200:  
	* 檢查 Bug
	* 修改 app.py 將取得ID與輸入資料分隔出為一個方法 Opt()
	* 修改 app.py 將取得使用者名稱換成一個方法 Name()
```
### 2020/03/12
```
* 1230:  
	* data.csv 修改 項目選項修改
	* app.py 修改 將相同功能合併 Uid()、Name()、Ukey()、InMes()
```
### 2020/03/13
```
* 1207:  
	* modelCode.py 修改 tenMod()方法 精簡程式內容，原本取兩格數值-->現在只取得一格數值
	* modelCode.py 修改 single()方法 精簡程式內容
	* app.py 修改 移除原本選項判斷 foodk() 新增ckey()判斷 "ck"為前四部分 "pk"為顯示圖片
	* modelCode.py 修改 移除foodk()等相關內容 新增為 ckey()與model()分別為判斷訊息與顯示板型
	* app.py 新增 我的最愛新增成功時 顯示成功訊息
```
### 2020/03/14
```
* 2323:  
	* app.py 新增 使用者輸入與關鍵字不相同時，顯示引導訊息
	* modelCode.py 修改 mylove()修改"-"為刪除
```
### 2020/03/15
```
* 1825:  
	* googleSheet.py 新增 資料上傳與取得googlesheet資料
```
### 2020/03/19
```
* 2217:  
	* googleSheet.py 修改 將驗證區獨立出來為token()
	* googleSheet.py 修改 time 修改時區為GMT+8
```
### 2020/03/20
```
* 1900:  
	* googleSheet.py 新增 tmes()先清空googlesheet內資料將mylove.csv資料寫進googlesheet
	* love.py 修改 relove()程式內容修改
	* app.py 新增 當GO()之後直接把googlesheet資料寫進mylove.csv內
	* app.py 新增 MyLove 當新增最愛時 kmes()寫進googlesheet、gmes()寫進mylove.csv內
	* app.py 新增 re 當刪除最愛時跑進tmes()
```
### 2020/03/24
```
* 1400:  
	* app.py 修改 Go()當使用者點選開始後判斷mylove.csv 若無建立csv
	* googleSheet.py 修改 kmes()當使用者新增最愛時同步新增googlesheet與mylove.csv
```
