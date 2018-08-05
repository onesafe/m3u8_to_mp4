# -*- coding:utf-8 -*-
import sys
import os
import sh
import requests


cwd = os.getcwd()


def download_ts(path, url_list):
	ts_files = []
	for url in url_list:
		ts_name = url.split("/")[-1:]
		ts_file = os.path.join(path, ts_name[0])
		if os.path.exists(ts_file):
			ts_files.append(ts_file)
			continue
		with open(ts_file, 'w') as f:
			data = requests.get(url, stream=True)
			for chunk in data.iter_content(chunk_size=512):
				if chunk:
					f.write(chunk)
		ts_files.append(ts_file)
	return ts_files



if __name__=='__main__':
	argv_len = len(sys.argv)

	ts_list = []
	mp4_file = None

	if argv_len == 3:
		m3u8_file, mp4_file = sys.argv[1:]
		print m3u8_file, mp4_file
		with open(m3u8_file) as m3u8_f:
			content = m3u8_f.readlines()
			for line in content:
				if line.endswith(".ts\n"):
					ts_list.append(line.replace("\n", ""))

	ts_path = os.path.join(cwd, "ts_files")
	sh.mkdir("-p", ts_path)

	ts_file_list = download_ts(ts_path, ts_list)


	print ts_file_list

	mp4_path = os.path.join(cwd, mp4_file)
	with open(mp4_path, 'wa+') as f:
		for ts_file in ts_file_list:
			with open(ts_file) as ts:
				f.write(ts.read())
				
	sh.rmdir("-rf", ts_path)
