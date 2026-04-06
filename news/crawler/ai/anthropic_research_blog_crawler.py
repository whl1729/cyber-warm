from typing import List

from bs4 import BeautifulSoup

from news.util import timelib
from news.util import web_crawler
from news.util.configer import config
from news.util.logger import logger
from news.util.web_parser import WebParser

ANTHROPIC_RESEARCH_BLOG_URL = "https://www.anthropic.com/research"
COLLECTION_NAME = "anthropic_research_blog"
BASE_URL = "https://www.anthropic.com"


class AnthropicResearchBlogParser(WebParser):
    def parse(self, resp_text: str) -> List[dict]:
        soup = BeautifulSoup(resp_text, "lxml")

        blog_list = []
        seen_urls = set()

        links = soup.find_all(
            "a",
            href=lambda x: x and "/research/" in x and "/team/" not in x,
        )
        for link in links:
            cls_str = " ".join(link.get("class", []))
            if "FeaturedGrid" in cls_str:
                post = self._parse_featured_item(link)
            elif "PublicationList" in cls_str:
                post = self._parse_publication_item(link)
            else:
                continue
            if post and post["url"] not in seen_urls:
                blog_list.append(post)
                seen_urls.add(post["url"])

        logger.info(f"{len(blog_list)} anthropic research blog posts parsed")
        return blog_list

    def _parse_featured_item(self, link) -> dict:
        try:
            title_elem = link.find(["h3", "h4"])
            if not title_elem:
                return None

            title = title_elem.get_text(strip=True)
            if not title:
                return None

            href = link.get("href", "")
            if not href:
                return None
            url = BASE_URL + href if href.startswith("/") else href

            time_elem = link.find("time")
            if time_elem:
                created_at = timelib.format_date_6(time_elem.get_text(strip=True))
            else:
                created_at = timelib.today()

            return {
                "id": title,
                "url": url,
                "created_at": created_at,
                "crawled_at": timelib.now2(),
            }
        except Exception as e:
            logger.warning(f"Failed to parse featured research item: {e}")
            return None

    def _parse_publication_item(self, link) -> dict:
        try:
            title = None
            for span in link.find_all("span"):
                span_cls = " ".join(span.get("class", []))
                if "title" in span_cls:
                    title = span.get_text(strip=True)
                    break

            if not title:
                return None

            href = link.get("href", "")
            if not href:
                return None
            url = BASE_URL + href if href.startswith("/") else href

            time_elem = link.find("time")
            if time_elem:
                created_at = timelib.format_date_6(time_elem.get_text(strip=True))
            else:
                created_at = timelib.today()

            return {
                "id": title,
                "url": url,
                "created_at": created_at,
                "crawled_at": timelib.now2(),
            }
        except Exception as e:
            logger.warning(f"Failed to parse publication research item: {e}")
            return None


def crawl():
    parser = AnthropicResearchBlogParser()
    web_crawler.crawl(
        parser,
        ANTHROPIC_RESEARCH_BLOG_URL,
        COLLECTION_NAME,
        proxies=config["proxies"],
    )


if __name__ == "__main__":
    crawl()
