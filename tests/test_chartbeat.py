from unittest import TestCase

from chartbeat import Chartbeat


class ChartbeatTest(TestCase):
    def setUp(self):
        self.beat = Chartbeat("317a25eccba186e0f6b558f45214c0e7", "avc.com")
        self.keys = [
            Chartbeat.READ, Chartbeat.WRITE, Chartbeat.IDLE
        ]

    def test_histogram(self):
        data = self.beat.histogram(keys=self.keys, breaks=[1, 5, 10])
        for key in self.keys:
            self.assertTrue(key in data)

    def test_path_summary(self):
        data = self.beat.path_summary(keys=self.keys, types=["n", "n", "s"])
        for path in data:
            for key in self.keys:
                self.assertTrue(key in data[path])

    def test_quickstats(self):
        data = self.beat.quickstats(path="/")
        self.assertTrue("toprefs" in data)
        self.assertTrue("visit" in data)

    def test_api_version(self):
        self.beat = Chartbeat("317a25eccba186e0f6b558f45214c0e7", "avc.com", api_version='3')
        data = self.beat.quickstats(path="/")
        self.assertTrue("toprefs" in data)
        self.assertTrue("visit" in data)
