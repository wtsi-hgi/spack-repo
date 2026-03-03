# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegexpipes(RPackage):
	"""Wrappers Around 'base::grep()' for Use with Pipes

	Provides wrappers around base::grep() where the first argument
    is standardized to take the data object. This makes it less of a pain to use
    regular expressions with 'magrittr' or other pipe operators.
	"""
	
	cran = "regexPipes" 

	version("0.0.1", md5="db46955fcf0789aa369df6d5a6f4feb8")

