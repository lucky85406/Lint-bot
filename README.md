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
