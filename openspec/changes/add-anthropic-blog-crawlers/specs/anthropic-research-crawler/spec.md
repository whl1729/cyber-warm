## ADDED Requirements

### Requirement: Crawl Anthropic Research blog posts
The system SHALL crawl https://www.anthropic.com/research and extract blog post metadata including title, URL, and publication date.

#### Scenario: Successful crawl of research blog
- **WHEN** the crawler runs against https://www.anthropic.com/research
- **THEN** system extracts all visible blog posts with title, URL, and created_at date

#### Scenario: Parse blog post item
- **WHEN** HTML contains a blog post element
- **THEN** system extracts title as string, URL as absolute path, and created_at in YYYY-MM-DD format

#### Scenario: Handle missing date
- **WHEN** blog post element has no date information
- **THEN** system uses current date as fallback

### Requirement: Store research blog data
The system SHALL store crawled research blog posts in MongoDB collection `anthropic_research_blog` with deduplication by title.

#### Scenario: Insert new blog posts
- **WHEN** crawler finds new blog posts not in database
- **THEN** system inserts them into `anthropic_research_blog` collection

#### Scenario: Skip duplicate posts
- **WHEN** crawler finds blog posts already in database (matching by `id` field which contains title)
- **THEN** system skips insertion and logs count of duplicates

### Requirement: Log crawl results
The system SHALL log the number of blog posts parsed and inserted.

#### Scenario: Log parsing count
- **WHEN** crawler completes parsing
- **THEN** system logs "N anthropic research blog posts parsed"

#### Scenario: Log insertion count
- **WHEN** crawler completes database insertion
- **THEN** system logs "N anthropic research blog inserted"

### Requirement: Support configuration control
The system SHALL respect the `enabled_topics` configuration to enable/disable the crawler.

#### Scenario: Crawler enabled in config
- **WHEN** `anthropic_research_blog` is in `enabled_topics` list or `enabled_topics` is None
- **THEN** system runs the crawler

#### Scenario: Crawler disabled in config
- **WHEN** `anthropic_research_blog` is NOT in `enabled_topics` list
- **THEN** system skips the crawler and logs skip message
