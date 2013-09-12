from ._hamt import (
    _absent,
    _not_found,
    EMPTY_BITMAP_INDEXED_NODE,
    )


# XXX: Add functions as supplements for methods?

class frozendict(object):

    # TODO: Docstring

    def __new__(cls, input=_absent):
        f = super(frozendict, cls).__new__(cls)
        f.root = None
        f.count = 0
        f._hash = None
        if input is _absent:
            return f
        else:
            return f.merge(input)


    def merge(self, pairs):
        """
        Return a new frozendict with the mappings in C{pairs}.

        If C{pairs} has a C{keys()} attribute, then adds C{(k, pairs[k])} for
        all C{k} in keys.  If not, then adds C{(k, v)} for all C{(k, v)} in
        pairs.
        """
        # XXX: Possible rename to with_pairs
        # XXX: Possible rename to mergeWith
        # XXX: It must be possible to rewrite this more efficiently, without
        # creating a new frozendict for each pair, perhaps by internally using
        # mutation.
        keys = getattr(pairs, 'keys', None)
        result = self
        if keys is not None:
            for k in pairs.keys():
                result = result.with_pair(k, pairs[k])
        else:
            for k, v in pairs:
                result = result.with_pair(k, v)
        return result


    def __len__(self):
        return self.count


    def __getitem__(self, key):
        val = self.get(key, _not_found)
        if val is _not_found:
            raise KeyError(key)
        else:
            return val


    def get(self, key, default=None):
        if self.root is None:
            return default
        val = self.root.find(0, hash(key), key)
        if val is _not_found:
            return default
        else:
            return val


    def __contains__(self, key):
        if self.root is None:
            return False
        else:
            return self.root.find(0, hash(key), key) is not _not_found


    def __hash__(self):
        if self._hash is not None:
            return self._hash
        # XXX: Why 0x3039?
        hashval = 0x3039
        for k, v in self.items():
            hashval += hash(k) ^ hash(v)
        self._hash = hashval
        return hashval


    def __eq__(self, other):
        if self is other:
            return True
        if not self.__class__ == other.__class__:
            return False
        if len(self) != len(other) or hash(self) != hash(other):
            return False
        for k, v in self.items():
            otherV = other.get(k, _not_found)
            if otherV is _not_found or v != otherV:
                return False
        return True


    def __ne__(self, other):
        # If you ever thought Python was good, this is where you can stop.
        return not self.__eq__(other)


    def keys(self):
        for (k, v) in self.items():
            yield k


    def values(self):
        for (k, v) in self.items():
            yield v


    def items(self):
        if self.root is None:
            return (x for x in ())
        else:
            return self.root.iteritems()


    def with_pair(self, k, v):
        """
        Return a new frozendict that maps 'k' to 'v'.
        """
        if self.root is None:
            newroot = EMPTY_BITMAP_INDEXED_NODE
        else:
            newroot = self.root

        newroot, addedLeaf = newroot.assoc(0, hash(k), k, v)

        if newroot is self.root:
            return self

        newf = frozendict()
        newf.count = self.count
        newf.root = newroot
        if addedLeaf:
            newf.count = self.count + 1
        return newf


    def without(self, k):
        """
        Return a new frozendict without key 'k'.
        """
        if self.root is None:
            return self
        newroot = self.root.without(0, hash(k), k)
        if newroot is _absent:
            return frozendict()
        if newroot is self.root:
            return self
        else:
            newf = frozendict()
            newf.count = self.count - 1
            newf.root = newroot
            return newf


    def __repr__(self):
        #for today, we're straight up cheatin'
        d = dict(self)
        return "frozendict(%r)" % (d,)
