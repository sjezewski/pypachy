#!/usr/bin/env python

"""Tests debug-related functionality"""

import pytest
import random
import string
import threading
from io import BytesIO
from collections import namedtuple

import python_pachyderm
from tests import util


def test_dump():
    client = python_pachyderm.Client()
    for b in client.dump():
        assert isinstance(b, bytes)
        assert len(b) > 0


def test_profile_cpu():
    client = python_pachyderm.Client()
    for b in client.profile_cpu(python_pachyderm.Duration(seconds=1)):
        assert isinstance(b, bytes)
        assert len(b) > 0


def test_binary():
    client = python_pachyderm.Client()
    for b in client.binary():
        assert isinstance(b, bytes)
        assert len(b) > 0
