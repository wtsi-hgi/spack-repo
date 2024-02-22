# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneralizedhyperbolic(RPackage):
	"""The Generalized Hyperbolic Distribution

	Functions for the hyperbolic and related distributions.
  Density, distribution and quantile functions and random number generation
  are provided for the hyperbolic distribution, the generalized hyperbolic
        distribution, the generalized inverse Gaussian distribution and
        the skew-Laplace distribution. Additional functionality is
        provided for the hyperbolic distribution, normal inverse
	Gaussian distribution and generalized inverse Gaussian distribution,
	including fitting of these distributions to data. Linear models with
        hyperbolic errors may be fitted using hyperblmFit.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rmetrics/"
	cran = "GeneralizedHyperbolic" 

	version("0.8-6", md5="428dde928d2b3cbdb5b0504aef9c177d")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-distributionutils", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
