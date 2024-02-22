# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGood(RPackage):
	"""Good Regression

	Fit Good regression models to count data (Tur et al., 2021) <arXiv:2105.01557>. The package provides functions for model estimation and model prediction. Density, distribution function, quantile function and random generation for the Good distribution are also provided.
	"""
	
	cran = "good" 

	version("1.0.1", md5="a7db2f2c79ba0f59d26645c5c7a5c760")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
