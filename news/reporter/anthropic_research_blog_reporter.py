from news.reporter.daily_news_reporter import DailyNewsReporter


class AnthropicResearchBlogReporter(DailyNewsReporter):
    def __init__(self):
        super().__init__(
            title="Anthropic Research Blog",
            table_name="anthropic_research_blog",
            order_by="created_at",
        )


def report() -> str:
    reporter = AnthropicResearchBlogReporter()
    return reporter.report()


if __name__ == "__main__":
    print(report())
