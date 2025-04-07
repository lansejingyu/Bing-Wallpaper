# Bing-Wallpaper
个人博客图库 Bing Wallpaper-Bing每日壁纸

Bing壁纸官方 API 的接口：  
1.分辨率：1920×1080  
https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN  
2.分辨率：3840×2160  
https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1614319565639&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160  

主要有 format、idx、n、mkt 四个参数：  
|  参数   | 含义  |
|  :-:  | :-:  |
| format  | 返回数据形式 js - json xml - xml |
| idx  | 返回 ≥0 天前的图片，截止天数 0-今天 1-截止至昨天 2--截止至前天，以此类推|
| n  | 	返回数量 |
| mkt  | 地区 zh-CN - 国区 |

1：Bing 4k超高清UHD原图 直链图片：'后面可拼上 '&rf=LaDigue_UHD.jpg',可与官网保持一致'  
https://cn.bing.com + bing壁纸官方 API2 中的接口响应中的 urlbase 的值中 + _UHD.jpg  
如：`https://cn.bing.com/th?id=OHR.UtahBadlands_ZH-CN9174002963_UHD.jpg`  
或者：`https://cn.bing.com/th?id=OHR.UtahBadlands_ZH-CN9174002963_UHD.jpg&rf=LaDigue_UHD.jpg`  

2：Bing 1920x1080 直链图片：'后面可拼上 '&rf=LaDigue_1920x1080.jpg',可与官网保持一致'  
https://cn.bing.com + bing壁纸官方 API2 中的接口响应中的 urlbase 的值中 + _1920x1080.jpg  
如：`https://cn.bing.com/th?id=OHR.UtahBadlands_ZH-CN9174002963_1920x1080.jpg`  
或者：`https://cn.bing.com/th?id=OHR.UtahBadlands_ZH-CN9174002963_1920x1080.jpg&rf=LaDigue_1920x1080.jpg`

3：Bing 首页分辨率1920*1200 直链图片：'后面可拼上 '&rf=LaDigue_1920x1200.jpg',可与官网保持一致'  
https://cn.bing.com + bing壁纸官方 API2 中的接口响应中的 urlbase 的值中 + _1920x1200.jpg  
如：`https://cn.bing.com/th?id=OHR.UtahBadlands_ZH-CN9174002963_1920x1200.jpg`  
或者：`https://cn.bing.com/th?id=OHR.UtahBadlands_ZH-CN9174002963_1920x1200.jpg&rf=LaDigue_1920x1200.jpg`
