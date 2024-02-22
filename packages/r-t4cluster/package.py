# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RT4cluster(RPackage):
	"""Tools for Cluster Analysis

	Cluster analysis is one of the most fundamental problems in data science. We provide a variety of algorithms from clustering to the learning on the space of partitions. See Hennig, Meila, and Rocci (2016, ISBN:9781466551886) for general exposition to cluster analysis.
	"""
	
	homepage = "https://kisungyou.com/T4cluster/"
	cran = "T4cluster" 

	version("0.1.2", md5="0d412ebcb385660c0ff050615e56309d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rdimtools", type=("build", "run"))
	depends_on("r-admm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-maotai", type=("build", "run"))
	depends_on("r-mclustcomp", type=("build", "run"))
	depends_on("r-rstiefel", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
