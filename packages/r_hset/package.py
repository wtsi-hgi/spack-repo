# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHset(RPackage):
	"""Sets of Numbers Implemented with Hash Tables

	Implementation of S4 class of sets and multisets of numbers.
    The implementation is based on the hash table from the package 'hash'.
    Quick operations are allowed when the set is a dynamic object.
    The implementation is discussed in detail in Ceoldo and Wit (2023) <arXiv:2304.09809>.
	"""
	
	cran = "hset" 

	version("0.1.1", md5="651b3c3605650a19fccbd19bf4c65772")

	depends_on("r-hash", type=("build", "run"))
