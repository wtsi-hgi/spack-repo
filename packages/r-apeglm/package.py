# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApeglm(RPackage):
	"""Approximate posterior estimation for GLM coefficients

	apeglm provides Bayesian shrinkage estimators for effect sizes for a variety of GLM models, using approximation of the posterior for individual coefficients.
	"""
	
	bioc = "apeglm"

	version("1.30.0", commit="0062b09ff3a9946b919b7935869b161308fb701b")
	version("1.24.0", commit="b6b76e653ae59a54c59f328ee25709286cb83ab5")

	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
