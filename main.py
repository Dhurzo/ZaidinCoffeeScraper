import asyncio

from src.application.use_cases.coffee_scraper_app import CoffeeScraperApp
from src.di.diContainer import Container
from src.infrastructure.logging.config import configure_logging


async def run_app() -> int:
    configure_logging()

    container = Container()

    app = CoffeeScraperApp(
        coffee_repository=container.coffee_repository(),
        category_repository=container.category_repository(),
        presenter=container.presenter(),
    )

    logger = container.logger()
    try:
        logger.info("Starting scraper...")
        result = await app.run()
        logger.info(f"\n{result}")
    except Exception as e:
        logger.error(f"Error running application: {str(e)}")
        return 1
    return 0


def main() -> int:
    return asyncio.run(run_app())


if __name__ == "__main__":
    exit(main())
