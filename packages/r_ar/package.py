# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAr(RPackage):
	"""Another Look at the Acceptance-Rejection Method

	In mathematics, 'rejection sampling' is a basic technique used to generate observations from a distribution. It is also commonly called 'the Acceptance-Rejection method' or 'Accept-Reject algorithm' and is a type of Monte Carlo method. 'Acceptance-Rejection method' is based on the observation that to sample a random variable one can perform a uniformly random sampling of the 2D cartesian graph, and keep the samples in the region under the graph of its density function. Package 'AR' is able to generate/simulate random data from a probability density function by Acceptance-Rejection method. Moreover, this package is a useful teaching resource for graphical presentation of Acceptance-Rejection method. From the practical point of view, the user needs to calculate a constant in Acceptance-Rejection method, which package 'AR' is able to compute this constant by optimization tools. Several numerical examples are provided to illustrate the graphical presentation for the Acceptance-Rejection Method.
	"""
	
	cran = "AR" 

	version("1.1", md5="ca5f6e446ca88a587d5fde28d685ebc3")

	depends_on("r-distrib", type=("build", "run"))
