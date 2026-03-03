# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScMeb(RPackage):
	"""Spatial Clustering with Hidden Markov Random Field using
Empirical Bayes

	Spatial clustering with hidden markov random field fitted via EM algorithm, details of which can be found in Yi Yang (2021) <doi:10.1101/2021.06.05.447181>. It is not only computationally efficient and scalable to the sample size increment, but also is capable of choosing the smoothness parameter and the number of clusters as well.
	"""
	
	cran = "SC.MEB" 

	version("1.1", md5="36bb62455b4e0a05f849c253921bab58")

	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
