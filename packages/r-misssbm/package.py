# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisssbm(RPackage):
	"""Handling Missing Data in Stochastic Block Models

	When a network is partially observed (here, NAs in the adjacency matrix rather than 1 or 0 
  due to missing information between node pairs), it is possible to account for the underlying process
  that generates those NAs. 'missSBM', presented in 'Barbillon, Chiquet and Tabouy' (2022) <doi:10.18637/jss.v101.i12>,
  adjusts the popular stochastic block model from network data sampled under various missing data conditions, 
  as described in 'Tabouy, Barbillon and Chiquet' (2019) <doi:10.1080/01621459.2018.1562934>.
	"""
	
	homepage = "https://grosssbm.github.io/missSBM/"
	cran = "missSBM" 

	version("1.0.4", md5="b3f55201d8ebebd6ba542a0d2d7c22db")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sbm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
