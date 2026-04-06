from news.reporter.daily_news_reporter import DailyNewsReporter


class AnthropicEngineeringBlogReporter(DailyNewsReporter):
    def __init__(self):
        super().__init__(
            title="Anthropic Engineering Blog",
            table_name="anthropic_engineering_blog",
            order_by="created_at",
        )


def report() -> str:
    reporter = AnthropicEngineeringBlogReporter()
    return reporter.report()


if __name__ == "__main__":
    print(report())
