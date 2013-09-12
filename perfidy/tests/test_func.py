from testtools import TestCase


from .._func import (
    identity,
)


class TestIdentity(TestCase):

    def test_identity(self):
        x = object()
        self.assertIs(x, identity(x))
