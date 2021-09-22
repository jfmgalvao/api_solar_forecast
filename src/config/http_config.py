import asyncio
import sys


def http_config():
    # Workaround to suppress EventLoop bug on windows machines
    if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())