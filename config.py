# -*- coding: utf-8 -*-
"""config

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iVCn73A-4_1-tQAHcl4QtSFN-lBwc53B
"""

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
UPDATE_INTERVAL = 3600