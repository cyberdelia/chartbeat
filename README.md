# Chartbeat

A charbeat/newsbeat API wrapper.

    >>> from atomic import Atomic
    >>> atomic = Atomic(0)
    >>> atomic.value = 40
    >>> atomic.value
    40
    >>> with atomic:
        atomic.value += 1
    >>> atomic.value
    41

## Installation

To install charbeat, use pip :

    $ pip install chartbeat
