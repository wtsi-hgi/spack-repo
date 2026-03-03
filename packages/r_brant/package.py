# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrant(RPackage):
	"""Test for Parallel Regression Assumption

	Tests the parallel regression assumption wit the brant test by Brant (1990) <doi: 10.2307/2532457> for ordinal logit models generated with the function polr() from the package 'MASS'.
	"""
	
	homepage = "https://benjaminschlegel.ch/r/brant/"
	cran = "brant" 

	version("0.3-0", md5="116f59e197045369878f99c7785afbab")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
