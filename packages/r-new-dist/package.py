# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewDist(RPackage):
	"""Alternative Continuous and Discrete Distributions

	The aim is to develop an R package, which is the 'new.dist'
    package, for the probability (density) function, the
    distribution function, the quantile function and the
    associated random number generation function for discrete and
    continuous distributions, which have recently been proposed
    in the literature. This package implements the following
    distributions: The Power Muth Distribution, a Bimodal Weibull
    Distribution, the Discrete Lindley Distribution, The
    Gamma-Lomax Distribution, Weighted Geometric Distribution, a
    Power Log-Dagum Distribution, Kumaraswamy Distribution,
    Lindley Distribution, the Unit-Inverse Gaussian Distribution,
    EP Distribution, Akash Distribution, Ishita Distribution,
    Maxwell Distribution, the Standard Omega Distribution,
    Slashed Generalized Rayleigh Distribution, Two-Parameter
    Rayleigh Distribution, Muth Distribution, Uniform-Geometric
    Distribution, Discrete Weibull Distribution.
	"""
	
	homepage = "https://github.com/akmn35/new.dist"
	cran = "new.dist" 

	version("0.1.1", md5="d4fb15b2074b2229c503f8bd885920ff")

	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
