# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScalreg(RPackage):
	"""Scaled Sparse Linear Regression

	Algorithms for fitting scaled sparse linear regression and estimating precision matrices.
	"""
	
	cran = "scalreg" 

	version("1.0.1", md5="9391cc48dee24a00b6827192fb95cf42")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
