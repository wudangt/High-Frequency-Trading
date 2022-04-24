import asyncio
import errno
import socket
from typing import Coroutine, List


async def main():
  print('Hi!')

if __name__ == "__main__":
  ev_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
  ev_loop.run_until_complete(main())
