# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdmtmb(RPackage):
	"""Spatial and Spatiotemporal SPDE-Based GLMMs with 'TMB'

	Implements spatial and spatiotemporal GLMMs (Generalized Linear
    Mixed Effect Models) using 'TMB', 'fmesher', and the SPDE (Stochastic Partial
    Differential Equation) Gaussian Markov random field approximation to
    Gaussian random fields. One common application is for spatially explicit
    species distribution models (SDMs).
    See Anderson et al. (2022) <doi:10.1101/2022.03.24.485545>.
	"""
	
	homepage = "https://pbs-assess.github.io/sdmTMB/"
	cran = "sdmTMB" 

	version("0.4.2", md5="8a6e96a565e3d1ed286756500e9e91b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fmesher", type=("build", "run"))
	depends_on("r-fishmod", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
