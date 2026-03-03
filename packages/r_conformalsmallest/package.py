# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConformalsmallest(RPackage):
	"""Efficient Tuning-Free Conformal Prediction

	An implementation of efficiency first conformal prediction (EFCP) and validity first conformal prediction (VFCP) that demonstrates both validity (coverage guarantee) and efficiency (width guarantee). To learn how to use it, check the vignettes for a quick tutorial. The package is based on the work by Yang Y., Kuchibhotla A.,(2021) <arxiv:2104.13871>.
	"""
	
	homepage = "https://github.com/Elsa-Yang98/ConformalSmallest"
	cran = "ConformalSmallest" 

	version("1.0", md5="6aafb768e2d4ab968d1a5c8de9340886")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quantregforest", type=("build", "run"))
