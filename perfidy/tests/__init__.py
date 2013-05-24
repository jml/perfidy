# Copyright (c) 2013 extras developers. See LICENSE for details.

"""Tests for perfidy."""

from unittest import TestSuite, TestLoader


def test_suite():
    from perfidy.tests import (
        test_extras,
        )
    modules = [
        test_extras,
        ]
    loader = TestLoader()
    suites = map(loader.loadTestsFromModule, modules)
    return TestSuite(suites)
