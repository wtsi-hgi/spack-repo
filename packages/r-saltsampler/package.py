# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaltsampler(RPackage):
	"""Efficient Sampling on the Simplex

	The SALTSampler package facilitates Monte Carlo Markov Chain (MCMC)
    sampling of random variables on a simplex. A Self-Adjusting Logit Transform
    (SALT) proposal is used so that sampling is still efficient even in difficult
    cases, such as those in high dimensions or with parameters that differ by orders
    of magnitude. Special care is also taken to maintain accuracy even when some
    coordinates approach 0 or 1 numerically. Diagnostic and graphic functions are
    included in the package, enabling easy assessment of the convergence and mixing
    of the chain within the constrained space.
	"""
	
	cran = "SALTSampler" 

	version("1.1.0", md5="6b05cab4ee2719a771e47c135a897091")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
