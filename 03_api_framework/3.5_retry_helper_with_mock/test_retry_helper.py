"""Твои тесты. См. TASK.md. retry_helper.py готов — твоя работа — тесты,
которые проверяют retry_call через мок, без реального time.sleep."""

from unittest.mock import Mock, patch

from retry_helper import RetryError, retry_call
