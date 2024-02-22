# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMipfp(RPackage):
	"""Multidimensional Iterative Proportional Fitting and Alternative
Models

	An implementation of the iterative proportional fitting (IPFP), 
    maximum likelihood, minimum chi-square and weighted least squares procedures
    for updating a N-dimensional array with respect to given target marginal 
    distributions (which, in turn can be multidimensional). The package also
    provides an application of the IPFP to simulate multivariate Bernoulli
    distributions.
	"""
	
	homepage = "https://github.com/jojo-/mipfp"
	cran = "mipfp" 

	version("3.2.1", md5="b24019b0ac96bc4d0894eff479134dc0")

	depends_on("r-cmm", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
