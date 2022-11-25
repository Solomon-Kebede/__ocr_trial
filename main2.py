import json
import requests
import base64
import random
import logging
import pprint

from engine.google import headers as header
from engine.google import uuid4like
from engine.randomizer import Randomizer
from engine.google import data4batchexecute
from engine.google import url4batchexecute

import asyncio
import aiohttp

logging.basicConfig(
	level=logging.ERROR,
	format=' %(asctime)s -%(levelname)s - %(message)s'
	)

image_paths = [
"./test_images/everything-has-beauty-confucius-quote.jpg",
"./test_images/maya-angelou-famous-quote.webp",
"./test_images/download2.jpg",
"./test_images/download.jpg",
"./test_images/d760e79a7997acefb79c917b7771d75f.jpg",
"./test_images/03ab9fbff391a8a3de0569050745a555.jpg",
"./test_images/download.png",
"./test_images/2101793258-amharic-poem.jpg"
]

base_url = "https://lens.google.com"
endpoint_1 = f"{base_url}/_/upload/"

def read_image(file_path):
	with open(file_path, 'rb') as f:
		return f.read()

