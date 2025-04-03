import requests
import json
import os


def get_bing_wallpaper():
	url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1614319565639&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"

	headers = {
		'Cookie': 'MUID=3215B205599A658F1EB3A7C4584364E7; SRCHD=AF=NOFORM; SRCHHPGUSR=SRCHLANG=zh-Hans; SRCHUID=V=2&GUID=33C388394D304D3B8041F82DFA28E53D&dmnchg=1; SRCHUSR=DOB=20250401&DS=1; _EDGE_S=SID=37B6604DF2A26FD82814758FF38C6EE5&mkt=zh-CN; _EDGE_V=1; _SS=SID=37B6604DF2A26FD82814758FF38C6EE5; MUIDB=3215B205599A658F1EB3A7C4584364E7'
	}

	try:
		# 发送 HTTP 请求
		response = requests.get(url, headers=headers)
		response.raise_for_status()  # 检查 HTTP 状态码（4XX/5XX 会抛出异常）

		# 解析 JSON 数据
		data = json.loads(response.text)

		# 壁纸url
		image_url_base = data["images"][0]["urlbase"]
		image_url = f"https://cn.bing.com{image_url_base}_UHD.jpg"  # 使用 UHD 分辨率（3840x2160）

		# 壁纸alt
		alt = data["images"][0]["urlbase"] + '.jpg'

		# 壁纸title(拼接了时间+地址)
		title_time = data["images"][0]["title"] + '_' + data["images"][0]["enddate"] + '_' + data["images"][0][
			"copyright"]

		print("成功获取 4K Bing 壁纸 URL:", image_url)
		return {
			"url": image_url,
			"alt": alt,
			"title": title_time
		}

	except requests.exceptions.RequestException as e:
		print("请求失败:", e)
	except json.JSONDecodeError as e:
		print("JSON 解析失败:", e)
	except KeyError as e:
		print("JSON 数据格式异常:", e)
	except Exception as e:
		print("未知错误:", e)

	return None  # 获取失败返回 None


def save_to_json(new_data):
	json_file = 'Bing-Wallpaper_info.json'

	# 如果文件不存在，创建初始结构
	if not os.path.exists(json_file):
		with open(json_file, 'w', encoding='utf-8') as f:
			json.dump([], f, ensure_ascii=False, indent=4)

	# 读取现有数据
	try:
		with open(json_file, 'r', encoding='utf-8') as f:
			existing_data = json.load(f)
	except (json.JSONDecodeError, FileNotFoundError):
		existing_data = []

	# 追加新数据--添加到最后面
	# existing_data.append(new_data)

	# 添加新数据到开头（而不是追加到结尾）
	existing_data.insert(0, new_data)  # 用insert方法插入到首位
	# """ 或者也可以用：
	# existing_data = [new_data] + existing_data  # 拼接方式
	# """

	# 写回文件
	with open(json_file, 'w', encoding='utf-8') as f:
		json.dump(existing_data, f, ensure_ascii=False, indent=4)
	print(f"数据已添加 {json_file}")


if __name__ == "__main__":
	wallpaper_data = get_bing_wallpaper()
	if wallpaper_data:
		save_to_json(wallpaper_data)
		print("最新壁纸数据已更新:", wallpaper_data)
	else:
		print("获取壁纸失败")
