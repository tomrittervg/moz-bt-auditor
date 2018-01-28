#!/usr/bin/env python

from requestsdownloader import RequestsDownloader
from mockdownloader import MockDownloader

def get_downloader():
	#return RequestsDownloader()
	return MockDownloader()