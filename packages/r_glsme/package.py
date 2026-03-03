# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlsme(RPackage):
	"""Generalized Least Squares with Measurement Error

	Performs linear regression with correlated predictors, responses and correlated measurement errors in predictors and responses, correcting for biased caused by these.
	"""
	
	cran = "GLSME" 

	version("1.0.5", md5="00d9953f689c5749cb32226a33669043")

	depends_on("r@2.9.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
