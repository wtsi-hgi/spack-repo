# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtm(RPackage):
	"""Latent Trait Models under IRT

	Analysis of multivariate dichotomous and polytomous data using latent trait models under the Item Response Theory approach. It includes the Rasch, the Two-Parameter Logistic, the Birnbaum's Three-Parameter, the Graded Response, and the Generalized Partial Credit Models.
	"""
	
	homepage = "https://github.com/drizopoulos/ltm"
	cran = "ltm" 

	version("1.2-0", md5="619669b10a42ffce353664582b0adf3d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
