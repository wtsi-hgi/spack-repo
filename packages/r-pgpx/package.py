# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgpx(RPackage):
	"""Pseudo-Realizations for Gaussian Process Excursions

	Computes pseudo-realizations from the posterior distribution of a Gaussian Process (GP) with the method described in Azzimonti et al. (2016) <doi:10.1137/141000749>. The realizations are obtained from simulations of the field at few well chosen points that minimize the expected distance in measure between the true excursion set of the field and the approximate one. Also implements a R interface for (the main function of) Distance Transform of sampled Functions (<https://cs.brown.edu/people/pfelzens/dt/index.html>).
	"""
	
	homepage = "https://doi.org/10.1137/141000749"
	cran = "pGPx" 

	version("0.1.4", md5="630e90e10812c3d503cda609d045bde4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-kriginv", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
