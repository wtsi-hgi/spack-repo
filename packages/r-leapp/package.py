# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeapp(RPackage):
	"""Latent Effect Adjustment After Primary Projection

	These functions take a gene expression value matrix, a
        primary covariate vector, an additional known covariates
        matrix.  A two stage analysis is applied to counter the effects
        of latent variables on the rankings of hypotheses.  The
        estimation and adjustment of latent effects are proposed by
        Sun, Zhang and Owen (2011).  "leapp" is developed in the
        context of microarray experiments, but may be used as a general
        tool for high throughput data sets where dependence may be
        involved.
	"""
	
	cran = "leapp" 

	version("1.3", md5="f29d040935908acb7adb69bd9530328e")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
