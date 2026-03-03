# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvctm(RPackage):
	"""Multivariate Variance Components Tests for Multilevel Data

	Permutation tests for variance components for 2-level, 3-level and 4-level data with univariate or multivariate responses.
	"""
	
	cran = "mvctm" 

	version("1.2", md5="3c2cb240d21f8c533e958430b1f2a8be")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mnm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rfit", type=("build", "run"))
	depends_on("r-spatialnp", type=("build", "run"))
