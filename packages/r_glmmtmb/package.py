# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmtmb(RPackage):
	"""Generalized Linear Mixed Models using Template Model Builder

	Fit linear and generalized linear mixed models with various
    extensions, including zero-inflation. The models are fitted using maximum
    likelihood estimation via 'TMB' (Template Model Builder). Random effects are
    assumed to be Gaussian on the scale of the linear predictor and are integrated
    out using the Laplace approximation. Gradients are calculated using automatic
    differentiation.
	"""
	
	homepage = "https://github.com/glmmTMB/glmmTMB"
	cran = "glmmTMB" 

	version("1.1.9", md5="a2d376ca8ae9bb5c5cacda1e557afb54")
	version("1.1.8", md5="b38f12164a971f380576ad2743f3ef12")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-lme4@1.1.18.9000:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
