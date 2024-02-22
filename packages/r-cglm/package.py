# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCglm(RPackage):
	"""Fits Conditional Generalized Linear Models

	Estimates the ratio of the regression coefficients and the dispersion parameter in conditional generalized linear models for clustered data.
	"""
	
	cran = "cglm" 

	version("1.1", md5="0a661d8bcbdcadd289a34875c29d9bf9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
