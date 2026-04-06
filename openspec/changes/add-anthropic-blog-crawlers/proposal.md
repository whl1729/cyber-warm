## Why

The project currently lacks crawlers for Anthropic's official blog content (Engineering and Research sections). Adding these crawlers will provide comprehensive coverage of AI research and engineering insights from one of the leading AI companies.

## What Changes

- Add `anthropic_engineering_blog_crawler.py` to crawl https://www.anthropic.com/engineering
- Add `anthropic_research_blog_crawler.py` to crawl https://www.anthropic.com/research
- Add corresponding reporters for both blog sources
- Register new crawlers in `ai_crawler.py`
- Register new reporters in `news_reporter.py`
- Add new topics to `config/cyber_news_config.yaml`

## Capabilities

### New Capabilities
- `anthropic-engineering-crawler`: Crawls Anthropic Engineering blog posts with title, URL, and publication date
- `anthropic-research-crawler`: Crawls Anthropic Research blog posts with title, URL, and publication date
- `anthropic-blog-reporters`: Generates daily news reports for both Anthropic blog sources

### Modified Capabilities
<!-- No existing capabilities are being modified -->

## Impact

- New files: `news/crawler/ai/anthropic_engineering_blog_crawler.py`, `news/crawler/ai/anthropic_research_blog_crawler.py`
- New files: `news/reporter/anthropic_engineering_blog_reporter.py`, `news/reporter/anthropic_research_blog_reporter.py`
- Modified: `news/crawler/ai/ai_crawler.py` (register new crawlers)
- Modified: `news/reporter/news_reporter.py` (register new reporters)
- Modified: `config/cyber_news_config.yaml` (add new topics)
- New MongoDB collections: `anthropic_engineering_blog`, `anthropic_research_blog`
