# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniqtag(RPackage):
	"""Abbreviate Strings to Short, Unique Identifiers

	For each string in a set of strings, determine a unique tag that is a substring of fixed size k unique to that string, if it has one. If no such unique substring exists, the least frequent substring is used. If multiple unique substrings exist, the lexicographically smallest substring is used. This lexicographically smallest substring of size k is called the "UniqTag" of that string.
	"""
	
	homepage = "https://github.com/sjackman/uniqtag"
	cran = "uniqtag" 

	version("1.0.1", md5="faea87762dd805d7aef056fdb84eaa24")

