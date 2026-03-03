# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdprisk(RPackage):
	"""Measures of Risk for the Compound Poisson Risk Process with
Diffusion

	Based on the compound Poisson risk process that is perturbed by
    a Brownian motion, saddlepoint approximations to some measures of risk are
    provided. Various approximation methods for the probability of ruin are
    also included. Furthermore, exact values of both the risk measures as well
    as the probability of ruin are available if the individual claims follow
    a hypo-exponential distribution (i. e., if it can be represented as a sum
    of independent exponentially distributed random variables with different
    rate parameters). For more details see Gatto and Baumgartner (2014)
    <doi:10.1007/s11009-012-9316-5>.
	"""
	
	cran = "sdprisk" 

	version("1.1-6", md5="e4b657ae1c2127f77474b680101f5fcb")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-polynomf@2.0.0:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
