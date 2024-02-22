# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvgeom(RPackage):
	"""The Time-Varying (Right-Truncated) Geometric Distribution

	Probability mass (d), distribution (p), quantile (q), and random 
    number generating (r and rt) functions for the time-varying right-truncated 
    geometric (tvgeom) distribution. Also provided are functions to calculate the first 
    and second central moments of the distribution. The tvgeom distribution
    is similar to the geometric distribution, but the probability 
    of success is allowed to vary at each time step, and there are a limited 
    number of trials. This distribution is essentially a Markov chain, and it
    is useful for modeling Markov chain systems with a set 
    number of time steps.
	"""
	
	cran = "tvgeom" 

	version("1.0.1", md5="e659d7ce16a9c56cded8329f9594d486")

	depends_on("r@3.5:", type=("build", "run"))
