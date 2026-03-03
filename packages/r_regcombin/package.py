# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegcombin(RPackage):
	"""Partially Linear Regression under Data Combination

	We implement linear regression when the outcome of interest and some of the covariates are observed in two different datasets that cannot be linked, based on D'Haultfoeuille, Gaillac, Maurel (2022) <doi:10.3386/w29953>. The package allows for common regressors observed in both datasets, and for various shape constraints on the effect of covariates on the outcome of interest. It also provides the tools to perform a test of point identification. See the associated vignette <https://github.com/cgaillac/RegCombin/blob/master/RegCombin_vignette.pdf> for theory and code examples.
	"""
	
	cran = "RegCombin" 

	version("0.4.1", md5="dce37e0f5fae23c218f0cb22a9ae28ca")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-rationalexp", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
