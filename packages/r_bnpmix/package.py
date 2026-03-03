# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnpmix(RPackage):
	"""Bayesian Nonparametric Mixture Models

	Functions to perform Bayesian nonparametric univariate and multivariate density estimation and clustering, by means of Pitman-Yor mixtures, and dependent Dirichlet process mixtures for partially exchangeable data. See Corradin et al. (2021) <doi:10.18637/jss.v100.i15> for more details.  
	"""
	
	cran = "BNPmix" 

	version("1.0.2", md5="6c5b79624b2889b6902dd0884b85fd51")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpp@0.12.13:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
