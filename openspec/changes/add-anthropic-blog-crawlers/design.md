## Context

The cyber-news project follows a consistent pattern for blog crawlers:
- Each blog source has a dedicated crawler file in `news/crawler/ai/`
- Crawlers inherit from `WebParser` and implement the `parse()` method
- Crawlers use BeautifulSoup to parse HTML and extract title, URL, and date
- Each crawler is registered in `ai_crawler.py` with a topic key
- Reporters extend `DailyNewsReporter` with `order_by="created_at"` for blog sources
- Configuration uses `enabled_topics` to control which crawlers run

Existing similar implementations: `claude_code_blog_crawler.py`, `deepmind_blog_crawler.py`, `openai_news_crawler.py`

## Goals / Non-Goals

**Goals:**
- Add crawlers for Anthropic Engineering and Research blogs following existing patterns
- Extract title, URL, and publication date from each blog post
- Store data in MongoDB collections: `anthropic_engineering_blog`, `anthropic_research_blog`
- Generate daily reports ordered by `created_at` (newest first)
- Enable/disable via config file

**Non-Goals:**
- Crawling blog post content (only metadata)
- Handling pagination (first page only, consistent with other crawlers)
- Real-time updates (runs on schedule like other crawlers)

## Decisions

### 1. Two Separate Crawlers vs. One Unified Crawler
**Decision**: Create two separate crawler files (`anthropic_engineering_blog_crawler.py` and `anthropic_research_blog_crawler.py`)

**Rationale**:
- Engineering and Research are distinct content categories with potentially different HTML structures
- Separate crawlers allow independent configuration and troubleshooting
- Consistent with existing pattern (e.g., separate crawlers for different OpenAI sections)
- Each can be enabled/disabled independently via config

**Alternative Considered**: Single crawler with URL parameter - rejected because it reduces flexibility and doesn't match project conventions

### 2. HTML Parsing Strategy
**Decision**: Use BeautifulSoup with CSS class selectors, implement after initial testing

**Rationale**:
- Anthropic pages may use JavaScript rendering, but will attempt static parsing first
- If static parsing fails, add `use_selenium=True` parameter (like some existing crawlers)
- HTML structure needs to be discovered through testing

**Alternative Considered**: Selenium by default - rejected because it's slower and most sites work with static parsing

### 3. Date Format Handling
**Decision**: Use existing `timelib` date parsing functions, add new format if needed

**Rationale**:
- Project has extensive date parsing utilities (`format_date`, `format_date_2`, etc.)
- Anthropic likely uses standard formats (e.g., "March 12, 2026" or "2026-03-12")
- Fallback to `timelib.today()` if parsing fails (consistent with other crawlers)

### 4. Reporter Configuration
**Decision**: Use `order_by="created_at"` for both reporters

**Rationale**:
- Blog posts have explicit publication dates (not just crawl time)
- CLAUDE.md explicitly requires `order_by="created_at"` for blog sources
- Ensures reports show newest content first

## Risks / Trade-offs

**Risk**: Anthropic pages may require JavaScript rendering
→ **Mitigation**: Test with static parsing first, add `use_selenium=True` if needed

**Risk**: HTML structure may change frequently
→ **Mitigation**: Follow existing error handling patterns, log parsing failures, use multiple selector strategies

**Risk**: Date format may be non-standard or missing
→ **Mitigation**: Implement robust date parsing with fallback to current date

**Risk**: Pages may be behind authentication or rate limiting
→ **Mitigation**: Use proxy configuration if needed (already supported), add appropriate delays

**Trade-off**: Two crawlers means more code duplication
→ **Accepted**: Consistency with project patterns outweighs DRY principle here
