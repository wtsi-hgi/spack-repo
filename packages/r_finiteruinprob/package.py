# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFiniteruinprob(RPackage):
	"""Computation of the Probability of Ruin Within a Finite Time
Horizon

	In the Cramér–Lundberg risk process perturbed by a Wiener
    process, this packages provides approximations to the probability of
    ruin within a finite time horizon.  Currently, there are three methods
    implemented: The first one uses saddlepoint approximation (two
    variants are provided), the second one uses importance sampling and
    the third one is based on the simulation of a dual process.  This last
    method is not very accurate and only given here for completeness.
	"""
	
	cran = "finiteruinprob" 

	version("0.6", md5="ce88c816dedf291e063cd0e449e35669")

	depends_on("r-sdprisk", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
