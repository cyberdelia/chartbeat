# Chartbeat

A charbeat/newsbeat API wrapper.

    >>> from chartbeat import Chartbeat
    >>> beat = Chartbeat("<your chartbeat api key>", "<your host>")
    >>> beat.quickstats()
    {u'crowd': 0,
    u'direct': 24,
    u'domload': 5000.0,
    u'engaged_time': 86.066,
    u'idle': 52,
    u'internal': 4,
    u'links': 13,
    u'new': 29,
    u'pages': 29,
    u'people': 61,
    u'platform': {u'd': 59, u'm': 1},
    u'read': 9,
    u'search': 7,
    u'social': 13,
    u'subscr': 0,
    u'toppages': [{u'path': u'/a_vc/2012/03/the-startup-curve.html',
                   u'visitors': 10},
                  {u'path': u'/', u'visitors': 9},
                  {u'path': u'/a_vc/2012/02/the-management-team-guest-post-from-joel-spolsky.html',
                   u'visitors': 7},
                  {u'path': u'/a_vc/2012/03/can-you-build-a-network-on-top-of-another-network.html',
                   u'visitors': 5},
                  {u'path': u'/a_vc/2011/09/minimum-viable-personality.html',
                   u'visitors': 3}],
    u'visit': 60.0,
    u'visits': 61,
    u'write': 0}

## Installation

To install charbeat, use pip :

    $ pip install chartbeat
