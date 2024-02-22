# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterlap(RPackage):
	"""Approximate Probability Densities by Iterated Laplace
Approximations

	The iterLap (iterated Laplace approximation) algorithm approximates a
             general (possibly non-normalized) probability density on R^p, by repeated
             Laplace approximations to the difference between current approximation 
             and true density (on log scale). The final approximation is a mixture of
             multivariate normal distributions and might be used for example as a
             proposal distribution for importance sampling (eg in Bayesian applications). 
             The algorithm can be seen as a computational generalization of the Laplace 
             approximation suitable for skew or multimodal densities.
	"""
	
	cran = "iterLap" 

	version("1.1-4", md5="59fbd01a4051a2c8cff61c7f62aab52c")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))
