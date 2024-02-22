# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdivar(RPackage):
	"""Statistical Inference for Noisy Vector Autoregression

	The model is high-dimensional vector autoregression with measurement error, also known as linear gaussian state-space model. Provable sparse expectation-maximization algorithm is provided for the estimation of transition matrix and noise variances. Global and simultaneous testings are implemented for transition matrix with false discovery rate control. For more information, see the accompanying paper: Lyu, X., Kang, J., & Li, L. (2023). "Statistical inference for high-dimensional vector autoregression with measurement error", Statistica Sinica.
	"""
	
	cran = "hdiVAR" 

	version("1.0.2", md5="83ee6612bb1226ad8f9ddd0c252fe8e0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
