#!/usr/bin/env python3

import asyncio
import re
from urllib.parse import urlparse
from parsel import Selector
import httpx


async def main():

    async with httpx.AsyncClient() as client:
        for number in range(10):
            start_url = "link_page={number}"

            resp = await client.get(start_url)
            await get_links(resp)

async def get_links(resp):
    sel = Selector(resp.text)
    urls = sel.xpath('//a[contains(@href, "tag")]/@href').getall()
    print(urls)
asyncio.run(main())
