# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWarpmix(RPackage):
	"""Mixed Effects Modeling with Warping for Functional Data Using
B-Spline

	Mixed effects modeling with warping for functional data using B-
    spline. Warping coefficients are considered as random effects, and warping
    functions are general functions, parameters representing the projection onto B-
    spline basis of a part of the warping functions. Warped data are modelled by a
    linear mixed effect functional model, the noise is Gaussian and independent from
    the warping functions.
	"""
	
	cran = "warpMix" 

	version("0.1.0", md5="46235a350333d9da6bd768ff548bf4fd")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-fda@2.4.4:", type=("build", "run"))
	depends_on("r-fields@8.4.1:", type=("build", "run"))
	depends_on("r-mass@7.3.44:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-nlme@3.1.128:", type=("build", "run"))
	depends_on("r-lme4@1.1.12:", type=("build", "run"))
