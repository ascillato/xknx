"""Unit test for KNX/IP base class."""
import asyncio
import unittest

from xknx import XKNX
from xknx.knxip import KNXIPFrame
from xknx.exceptions import CouldNotParseKNXIP


class Test_KNXIP(unittest.TestCase):
    """Test class for KNX/IP base class."""

    # pylint: disable=too-many-public-methods,invalid-name

    def setUp(self):
        """Set up test class."""
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        """Tear down test class."""
        self.loop.close()

    def test_wrong_init(self):
        """Testing init method with wrong service_type_ident."""
        xknx = XKNX(loop=self.loop)
        knxipframe = KNXIPFrame(xknx)
        with self.assertRaises(TypeError):
            knxipframe.init(23)

    def test_parsing_too_long_knxip(self):
        """Test parsing and streaming connection state request KNX/IP packet."""
        raw = ((0x06, 0x10, 0x02, 0x07, 0x00, 0x10, 0x15, 0x00,
                0x08, 0x01, 0xC0, 0xA8, 0xC8, 0x0C, 0xC3, 0xB4, 0x00))
        xknx = XKNX(loop=self.loop)
        knxipframe = KNXIPFrame(xknx)
        with self.assertRaises(CouldNotParseKNXIP):
            knxipframe.from_knx(raw)
