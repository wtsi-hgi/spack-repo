# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrishdirectorates(RPackage):
	"""A Dynamic Bipartite Latent Space Model to Analyse Irish
Companies' Boards from 2003 to 2013

	Provides the dataset and an implementation of the method illustrated in Friel, N., Rastelli, R., Wyse, J. and Raftery, A.E. (2016) <DOI:10.1073/pnas.1606295113>.
	"""
	
	cran = "IrishDirectorates" 

	version("1.4", md5="4ed5926c738650f31b9d37f8f9d4ae9b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
