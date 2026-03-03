# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmixture(RPackage):
	"""Bayesian Estimation for Finite Mixture of Distributions

	Provides statistical tools for Bayesian estimation of mixture distributions, mainly a mixture of Gamma, Normal, and t-distributions. The package is implemented based on the Bayesian literature for the finite mixture of distributions, including Mohammadi and et al. (2013) <doi:10.1007/s00180-012-0323-3> and Mohammadi and Salehi-Rad (2012) <doi:10.1080/03610918.2011.588358>.
	"""
	
	homepage = "https://www.uva.nl/profile/a.mohammadi"
	cran = "bmixture" 

	version("1.7", md5="31322aef8c62f86e3f88584d89f6b8b1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bdgraph", type=("build", "run"))
