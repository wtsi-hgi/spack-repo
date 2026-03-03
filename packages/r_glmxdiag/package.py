# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmxdiag(RPackage):
	"""A Collection of Graphic Tools for GLM Diagnostics and some
Extensions

	Provides diagnostic graphic tools for GLMs, beta-binomial regression model (estimated by 'VGAM' package), beta regression model (estimated by 'betareg' package) and negative binomial regression model (estimated by 'MASS' package). Since most of functions implemented in 'glmxdiag' already exist in other packages, the aim is to provide the user unique functions that work on almost all regression models previously specified. Details about some of the implemented functions can be found in Brown (1992) <doi:10.2307/2347617>, Dunn and Smyth (1996) <doi:10.2307/1390802>, O'Hara Hines and Carter (1993) <doi:10.2307/2347405>, Wang (1985) <doi:10.2307/1269708>.
	"""
	
	cran = "glmxdiag" 

	version("1.0.0", md5="a89409c8d9388843d4aed7ef7a271bfa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
