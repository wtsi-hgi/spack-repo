# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBalancedsampling(RPackage):
	"""Balanced and Spatially Balanced Sampling

	Select balanced and spatially balanced probability samples in multi-dimensional spaces
    with any prescribed inclusion probabilities. It contains fast (C++ via Rcpp) implementations of
    the included sampling methods. The local pivotal method by Grafström, Lundström and Schelin (2012)
    <doi:10.1111/j.1541-0420.2011.01699.x> and spatially correlated Poisson sampling by Grafström (2012)
    <doi:10.1016/j.jspi.2011.07.003> are included. Also the cube method (for balanced sampling) and
    the local cube method (for doubly balanced sampling) are included, see Grafström and Tillé (2013)
    <doi:10.1002/env.2194>.
	"""
	
	homepage = "https://www.envisim.se/"
	cran = "BalancedSampling" 

	version("2.0.6", md5="25891bbf878347c467d244af2695a15b")
	version("1.6.3", md5="66aa7fdb71bb8f3432c6e26f2bd44ba8")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
