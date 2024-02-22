# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnarclust(RPackage):
	"""Clustering Data with Non-Ignorable Missingness using
Semi-Parametric Mixture Models

	Clustering of data under a non-ignorable missingness mechanism. Clustering is achieved by a semi-parametric mixture model and missingness is managed by using the pattern-mixture approach. More details of the approach are available in Du Roy de Chaumaray et al. (2020) <arXiv:2009.07662>. 
	"""
	
	homepage = "https://arxiv.org/abs/2009.07662"
	cran = "MNARclust" 

	version("1.1.0", md5="25374d49e8db60d5a815ea057246a25b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
