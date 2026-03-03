# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcdglm(RPackage):
	"""EM by the Method of Weights for Incomplete Categorical Data in
Generlized Linear Models

	Provides an estimator for generalized linear models with incomplete
    data for discrete covariates. The estimation is based on the EM algorithm by the
    method of weights by Ibrahim (1990) <DOI:10.2307/2290013>.
	"""
	
	cran = "icdGLM" 

	version("1.0.0", md5="97b391271516f648313d5762eca77623")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
