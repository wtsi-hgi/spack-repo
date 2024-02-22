# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBurstmisc(RPackage):
	"""Burns Statistics Miscellaneous

	Script search, corner, genetic optimization, permutation tests, write expect test.
	"""
	
	cran = "BurStMisc" 

	version("1.1", md5="98509d7b9735a41becf6346742ac8b99")

