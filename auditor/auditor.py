#!/usr/bin/env python

from merkle import *

import hashlib

class Auditor:
	def __init__(self):
		pass

	def audit(self, entry, hashes):
		components = entry.split(".")
		expected_merkle_root = components[0] + components[1]
		version = components[2].replace("-", ".")
		tag = components[3]

		print "Auditing", tag, version, "with expected merkle root", expected_merkle_root
		
		tree = MerkleTree(hashlib.sha256, hashes)
		got_merkle_root = tree.head().encode("hex")
		print "  Got tree head", got_merkle_root
		print "  Expected tree head", expected_merkle_root
		print "  Match:", expected_merkle_root == got_merkle_root

		return expected_merkle_root == got_merkle_root
		