import pytest
from unittest.mock import MagicMock, patch

def test_client_initialization():
    from butler.client import client
    assert client is not None
