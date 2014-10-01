#!/usr/bin/env python
# encoding: utf-8
"""
Copyright (c) 2014 TipTap. All rights reserved.

"""
import re
import logging


class HealthPingFilter(logging.Filter):
    """
    Filter out /health & /ping log messages
    """
    def __init__(self):
        self.prog = re.compile("200 GET /(ping|health)")

    def filter(self, record):
        if self.prog.search(record.getMessage()):
            return False

        return True
