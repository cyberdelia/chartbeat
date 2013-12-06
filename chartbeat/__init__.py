import requests
import time

try:
    import json
except ImportError:
    import simplejson as json  # noqa

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin  # noqa

from datetime import datetime


class ChartbeatException(Exception):
    response = None


class Chartbeat(object):
    PAGETIMER = 'b'  # Time to finish loading the dom.
    TIME_SPENT = 'c'  # Number of seconds on page.
    DOMAIN = 'd'  # The domain name of the document (what's in the browser bar).
    UID = 'g'  # The chartbeat account.
    HOST = 'h'  # The reported domain (the dashboard the data goes to).
    TITLE = 'i'  # Page title.
    NEW = 'n'  # First time visitor for the site in last 30 days.
    PATH = 'p'  # Path of page from location.pathname.
    REFERRER = 'r'  # Referrer from document.referrer.
    TOKEN = 't'  # Temporary uuid event's page session (regenerated when moving to another page).
    USER = 'u'  # User token.
    WINDOW_HEIGHT = 'w'  # window.innerHeight || document.body.offsetHeight.
    SCROLL_TOP = 'x'  # window.pageYOffset || document.body.scrollTop || document.documentElement.scrollTop.
    PAGE_HEIGHT = 'y'  # document.body.scrollHeight.
    READ = 'R'  # Number of people reading.
    WRITE = 'W'  # Number of people writing.
    IDLE = 'I'  # Number of people idle.

    def __init__(self, apikey, host, api_version=None):
        self.apikey = apikey
        self.host = host
        self.api_version = api_version

        if self.api_version is not None and self.api_version.isdigit():
            self.api_version = 'v%s' % (self.api_version)

    def _request(self, endpoint, **params):
        params.update({
            'apikey': self.apikey,
            'host': self.host
        })
        for key, value in list(params.items()):
            if isinstance(value, datetime):
                params[key] = int(time.mktime(value.timetuple()))
            if isinstance(value, list):
                params[key] = ",".join([str(v) for v in value])

        if 'live' in endpoint and self.api_version is not None:
            endpoint = '%s/%s/' % (endpoint, self.api_version)

        endpoint = urljoin("http://api.chartbeat.com", endpoint)

        response = requests.get(endpoint, params=params)

        try:
            response.raise_for_status()
        except requests.RequestException as e:
            exception = ChartbeatException(e)
            if hasattr(e, 'response'):
                exception.response = e.response
            raise exception

        if hasattr(response, 'json'):
            if callable(response.json):
                return response.json()
            else:
                return response.json
        else:
            if response.content and "application/json" in response.headers['Content-Type']:
                return json.loads(response.content.decode('utf-8'))
        return response.content

    def histogram(self, keys, breaks, path=None):
        return self._request("/live/histogram/", keys=keys, breaks=breaks, path=path)

    def path_summary(self, keys, types):
        return self._request("/live/pathsummary/", keys=keys, types=types)

    def quickstats(self, path=None):
        return self._request("/live/quickstats/", path=path)

    def recent(self, path=None, limit=50):
        return self._request("/live/recent/", path=path, limit=limit)

    def referrers(self, limit=10):
        return self._request("/live/referrers/", limit=limit)

    def summary(self, keys, path=None):
        return self._request("/live/summary/", keys=keys, path=path)

    def top_pages(self, limit=10):
        return self._request("/live/toppages/", limit=limit)

    def geo(self, section=None, author=None, path=None, limit=100):
        return self._request("/live/geo/", section=section, author=author, path=path, limit=limit)

    def alerts(self, since):
        return self._request("/historical/dashapi/alerts/", since=since)

    def snapshots(self, timestamp):
        return self._request("/historical/dashapi/snapshots/", timestamp=timestamp)

    def stats(self):
        return self._request("/historical/dashapi/stats/")

    def data_series(self, days, minutes, type, val=None, timestamp=None):
        return self._request("/historical/dashapi/data_series/", days=days,
            minutes=minutes, type=type, val=val, timestamp=timestamp)

    def day_data_series(self, type, timestamp=None):
        return self._request("/historical/dashapi/day_data_series/", type=type, timestamp=timestamp)
