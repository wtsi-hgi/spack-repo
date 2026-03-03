# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJoinet(RPackage):
	"""Multivariate Elastic Net Regression

	Implements high-dimensional multivariate regression by stacked generalisation (Rauschenberger 2021 <doi:10.1093/bioinformatics/btab576>). For positively correlated outcomes, a single multivariate regression is typically more predictive than multiple univariate regressions. Includes functions for model fitting, extracting coefficients, outcome prediction, and performance measurement. If required, install MRCE or remMap from GitHub (<https://github.com/cran/MRCE>, <https://github.com/cran/remMap>).
	"""
	
	homepage = "https://github.com/rauschenberger/joinet"
	cran = "joinet" 

	version("0.0.10", md5="f6bb5bb2602ad49bf99ce3d6f9e09ffb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-palasso", type=("build", "run"))
	depends_on("r-cornet", type=("build", "run"))
