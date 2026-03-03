# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreed(RPackage):
	"""Clustering and Model Selection with the Integrated
Classification Likelihood

	An ensemble of algorithms that enable the clustering of networks and data matrices (such as counts, categorical or continuous) with different type of generative models. Model selection and clustering is performed in combination by optimizing the Integrated Classification Likelihood (which is equivalent to minimizing the description length). Several models are available such as: Stochastic Block Model, degree corrected Stochastic Block Model, Mixtures of Multinomial, Latent Block Model. The optimization is performed thanks to a combination of greedy local search and a genetic algorithm (see <arXiv:2002:11577> for more details).
	"""
	
	homepage = "https://comeetie.github.io/greed/"
	cran = "greed" 

	version("0.6.1", md5="a378f3176168521d9772d3674ccccf7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-listenv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cba", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
