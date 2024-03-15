# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpvecchia(RPackage):
	"""Scalable Gaussian-Process Approximations

	Fast scalable Gaussian process approximations, particularly well suited to spatial (aerial, remote-sensed) and environmental data, described in more detail in Katzfuss and Guinness (2017) <arXiv:1708.06302>. Package also contains a fast implementation of the incomplete Cholesky decomposition (IC0), based on Schaefer et al. (2019) <arXiv:1706.02205> and MaxMin ordering proposed in Guinness (2018) <arXiv:1609.05372>.
	"""
	
	cran = "GPvecchia" 

	version("0.1.7", md5="aa543f82b8ab28f85b987a31ebe8814f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sparseinv", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-matrix@1.5.1:", type=("build", "run"))
	depends_on("r-gpgp", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
