## ADDED Requirements

### Requirement: Generate Anthropic Engineering blog report
The system SHALL generate a daily news report section for Anthropic Engineering blog posts ordered by publication date (newest first).

#### Scenario: Generate report with posts
- **WHEN** reporter runs and database contains Anthropic Engineering blog posts
- **THEN** system generates markdown section with title "## Anthropic Engineering Blog" and list of posts

#### Scenario: Order posts by created_at
- **WHEN** reporter queries database
- **THEN** system orders results by `created_at` field in descending order (newest first)

#### Scenario: Format post entry
- **WHEN** reporter formats a blog post
- **THEN** system outputs markdown link format: "- [title](url) (YYYY-MM-DD)"

#### Scenario: Empty report
- **WHEN** reporter runs and database has no posts
- **THEN** system returns empty string (no section generated)

### Requirement: Generate Anthropic Research blog report
The system SHALL generate a daily news report section for Anthropic Research blog posts ordered by publication date (newest first).

#### Scenario: Generate report with posts
- **WHEN** reporter runs and database contains Anthropic Research blog posts
- **THEN** system generates markdown section with title "## Anthropic Research Blog" and list of posts

#### Scenario: Order posts by created_at
- **WHEN** reporter queries database
- **THEN** system orders results by `created_at` field in descending order (newest first)

#### Scenario: Format post entry
- **WHEN** reporter formats a blog post
- **THEN** system outputs markdown link format: "- [title](url) (YYYY-MM-DD)"

#### Scenario: Empty report
- **WHEN** reporter runs and database has no posts
- **THEN** system returns empty string (no section generated)

### Requirement: Integrate with main news reporter
The system SHALL register both Anthropic reporters in the main news reporter to include them in daily news generation.

#### Scenario: Include in daily news
- **WHEN** main news reporter runs
- **THEN** system includes both Anthropic Engineering and Research sections in the output

#### Scenario: Reporter ordering
- **WHEN** main news reporter generates content
- **THEN** system places Anthropic reporters near other AI blog sources (after Claude Code Blog, before or after other AI blogs)
