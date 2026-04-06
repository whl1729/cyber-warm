## 1. Create Anthropic Engineering Blog Crawler

- [x] 1.1 Create `news/crawler/ai/anthropic_engineering_blog_crawler.py` with WebParser implementation
- [x] 1.2 Implement `parse()` method to extract blog posts from HTML
- [x] 1.3 Implement `_parse_item()` helper to extract title, URL, and date from each post element
- [x] 1.4 Add date parsing logic with fallback to current date
- [x] 1.5 Add `crawl()` function that calls `web_crawler.crawl()` with collection name `anthropic_engineering_blog`

## 2. Create Anthropic Research Blog Crawler

- [x] 2.1 Create `news/crawler/ai/anthropic_research_blog_crawler.py` with WebParser implementation
- [x] 2.2 Implement `parse()` method to extract blog posts from HTML
- [x] 2.3 Implement `_parse_item()` helper to extract title, URL, and date from each post element
- [x] 2.4 Add date parsing logic with fallback to current date
- [x] 2.5 Add `crawl()` function that calls `web_crawler.crawl()` with collection name `anthropic_research_blog`

## 3. Register Crawlers in AI Crawler

- [x] 3.1 Add import for `anthropic_engineering_blog_crawler` in `news/crawler/ai/ai_crawler.py`
- [x] 3.2 Add import for `anthropic_research_blog_crawler` in `news/crawler/ai/ai_crawler.py`
- [x] 3.3 Add `"anthropic_engineering_blog": anthropic_engineering_blog_crawler` to crawlers dict
- [x] 3.4 Add `"anthropic_research_blog": anthropic_research_blog_crawler` to crawlers dict

## 4. Create Anthropic Engineering Blog Reporter

- [x] 4.1 Create `news/reporter/anthropic_engineering_blog_reporter.py` extending DailyNewsReporter
- [x] 4.2 Set title to "Anthropic Engineering Blog", table_name to "anthropic_engineering_blog", order_by to "created_at"
- [x] 4.3 Add `report()` function and `__main__` block

## 5. Create Anthropic Research Blog Reporter

- [x] 5.1 Create `news/reporter/anthropic_research_blog_reporter.py` extending DailyNewsReporter
- [x] 5.2 Set title to "Anthropic Research Blog", table_name to "anthropic_research_blog", order_by to "created_at"
- [x] 5.3 Add `report()` function and `__main__` block

## 6. Register Reporters in News Reporter

- [x] 6.1 Add DailyNewsReporter entry for Anthropic Engineering Blog in `news/reporter/news_reporter.py`
- [x] 6.2 Add DailyNewsReporter entry for Anthropic Research Blog in `news/reporter/news_reporter.py`
- [x] 6.3 Position reporters after Claude Code Blog in the daily_reporters list

## 7. Update Configuration

- [x] 7.1 Add `anthropic_engineering_blog` to `enabled_topics` list in `config/cyber_news_config.yaml`
- [x] 7.2 Add `anthropic_research_blog` to `enabled_topics` list in `config/cyber_news_config.yaml`

## 8. Verification

- [x] 8.1 Run engineering blog crawler and verify posts are inserted into MongoDB
- [x] 8.2 Run research blog crawler and verify posts are inserted into MongoDB
- [x] 8.3 Run news reporter and verify both Anthropic sections appear in output with correct ordering
- [x] 8.4 Run pre-commit checks to ensure code passes formatting and linting
