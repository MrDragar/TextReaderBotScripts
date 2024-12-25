import requests
import json


def handle(data):
	data = json.loads(data)
	BOT_TOKEN = data["BOT_TOKEN"]

	file_id = data["file_id"]
	proxy = {
		"https": data["HTTPS_PROXY"]
	}

	get_file_url = f'https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={file_id}'
	response = requests.get(get_file_url, proxies=proxy).json()

	if response['ok']:
		file_path = response['result']['file_path']

		download_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}'
		return download_url
	return 
