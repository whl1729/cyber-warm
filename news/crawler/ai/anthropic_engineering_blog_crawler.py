from typing import List

from bs4 import BeautifulSoup

from news.util import timelib
from news.util import web_crawler
from news.util.configer import config
from news.util.logger import logger
from news.util.web_parser import WebParser

ANTHROPIC_ENGINEERING_BLOG_URL = "https://www.anthropic.com/engineering"
COLLECTION_NAME = "anthropic_engineering_blog"
BASE_URL = "https://www.anthropic.com"


class AnthropicEngineeringBlogParser(WebParser):
    def parse(self, resp_text: str) -> List[dict]:
        soup = BeautifulSoup(resp_text, "lxml")

        blog_list = []
        seen_urls = set()

        articles = soup.find_all("article")
        for article in articles:
            article_cls = " ".join(article.get("class", []))
            if "ArticleList" not in article_cls:
                continue

            link = article.find("a", href=lambda x: x and "/engineering/" in x)
            if not link:
                continue

            post = self._parse_item(article, link)
            if post and post["url"] not in seen_urls:
                blog_list.append(post)
                seen_urls.add(post["url"])

        logger.info(f"{len(blog_list)} anthropic engineering blog posts parsed")
        return blog_list

    def _parse_item(self, article, link) -> dict:
        try:
            title_elem = article.find(["h2", "h3", "h4"])
            if not title_elem:
                return None

            title = title_elem.get_text(strip=True)
            if not title or title == "Featured":
                return None

            href = link.get("href", "")
            if not href:
                return None
            url = BASE_URL + href if href.startswith("/") else href

            date_elem = None
            for div in article.find_all("div"):
                div_cls = " ".join(div.get("class", []))
                if "date" in div_cls:
                    date_elem = div
                    break
            if date_elem:
                created_at = timelib.format_date_6(date_elem.get_text(strip=True))
            else:
                created_at = timelib.today()

            return {
                "id": title,
                "url": url,
                "created_at": created_at,
                "crawled_at": timelib.now2(),
            }
        except Exception as e:
            logger.warning(f"Failed to parse engineering blog item: {e}")
            return None


def crawl():
    parser = AnthropicEngineeringBlogParser()
    web_crawler.crawl(
        parser,
        ANTHROPIC_ENGINEERING_BLOG_URL,
        COLLECTION_NAME,
        proxies=config["proxies"],
    )


if __name__ == "__main__":
    crawl()
