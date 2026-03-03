# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWqs(RPackage):
	"""Weighted Quantile Sum Regression

	Fits weighted quantile sum regression models, calculates weighted quantile sum index and estimated component weights.
	"""
	
	cran = "wqs" 

	version("0.0.1", md5="d39edcdf1e99c05596e8bbbc82d8c6a3")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
