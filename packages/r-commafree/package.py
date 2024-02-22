# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommafree(RPackage):
	"""Call Functions Without Commas Between Arguments

	Provides the "comma-free call" operator: '%(%'. Use it to call a
    function without commas between the arguments. Just replace the '('
    with '%(%' in a function call, supply your arguments as standard R
    expressions enclosed by '{ }', and be free of commas (for that call).
	"""
	
	homepage = "https://github.com/t-kalinowski/commafree"
	cran = "commafree" 

	version("0.1.0", md5="0afb58c8f2448e6823eefd84af873816")

