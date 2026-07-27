"""
title: Weather Module
author: Y K
version: 0.0.1
requirements: aiohttp[speedups]
"""

import os

import aiohttp


class Tools:
    def __init__(self) -> None:
        """Customize Constructor"""

    async def get_current_weather(
        self,
        location: str,
    ) -> str:
        """Get Current Weather

        Get the current weather for a given location.

        Args:
            location: The location for which to retrieve the weather.

        Returns:
            The current weather as a string.
        """

        api_key = os.environ.get("OPENWEATHER_API_KEY")
        if not api_key:
            return (
                "API key is not set in the environment variable 'OPENWEATHER_API_KEY'."
            )

        base_url = "https://api.openweathermap.org/data/2.5/weather"
        query = {
            "q": location,
            "appid": api_key,
            "units": "metric",  # Optional: Use 'imperial' for Fahrenheit
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    url=base_url,
                    params=query,
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=False,
                ) as response:
                    if response.status == 200:
                        data = await response.json()

                        weather_description = data["weather"][0]["description"]
                        temperature = data["main"]["temp"]
                        humidity = data["main"]["humidity"]
                        wind_speed = data["wind"]["speed"]

                        return f"Weather in {location}: {temperature}°C"

                    return (
                        f"Error fetching weather data. Status Code: {response.status}"
                    )
            except Exception as error:
                return f"Error fetching weather data: {error!s}"
