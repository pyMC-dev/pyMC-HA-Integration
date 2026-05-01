"""Data coordinator for pyMC Repeater."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import (
    PyMCRepeaterApiClient,
    PyMCRepeaterAuthenticationError,
    PyMCRepeaterCannotConnect,
)
from .const import DEFAULT_SCAN_INTERVAL, DOMAIN

_LOGGER = logging.getLogger(__name__)


class PyMCRepeaterDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    """Coordinate pyMC Repeater polling."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        api: PyMCRepeaterApiClient,
    ) -> None:
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=DEFAULT_SCAN_INTERVAL,
        )
        self.config_entry = entry
        self.api = api

    async def _async_update_data(self) -> dict:
        try:
            return await self.api.async_fetch_all()
        except PyMCRepeaterAuthenticationError as err:
            raise ConfigEntryAuthFailed(str(err)) from err
        except PyMCRepeaterCannotConnect as err:
            raise UpdateFailed(str(err)) from err
