"""
Test Weather
~~~~~~~~~~~~

This module test functionality for the Weather Module.
"""

from pathlib import Path

import pytest
import tealogger

import weather

CURRENT_MODULE_PATH = Path(__file__).parent.expanduser().resolve()

# Configure test_logger
tealogger.configure(configuration=CURRENT_MODULE_PATH / "tealogger.json")
logger = tealogger.get_logger("test.weather")


class TestWeather:
    @pytest.mark.asyncio
    async def test_get_current_weather(self):
        """Test Get Current Weather"""

        tools = weather.Tools()
        location = "Carmel, Indiana"

        result = await tools.get_current_weather(location)
        logger.debug(f"Weather Result: {result}")

        assert isinstance(result, str)
