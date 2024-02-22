# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcrocsurface(RPackage):
	"""Bias-Corrected Methods for Estimating the ROC Surface of
Continuous Diagnostic Tests

	The bias-corrected estimation methods for the receiver operating characteristics
  ROC surface and the volume under ROC surfaces (VUS) under missing at random (MAR)
  assumption.
	"""
	
	homepage = "https://github.com/toduckhanh/bcROCsurface"
	cran = "bcROCsurface" 

	version("1.0-6", md5="4266e43eafce33dff8425abe7618fb30")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
