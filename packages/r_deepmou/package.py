# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepmou(RPackage):
	"""Clustering of Short Texts by Mixture of Unigrams and Its Deep
Extensions

	Functions providing an easy and intuitive way for fitting and clusters data using the Mixture of Unigrams models by means the Expectation-Maximization algorithm (Nigam, K. et al. (2000). <doi:10.1023/A:1007692713085>), Mixture of Dirichlet-Multinomials estimated by Gradient Descent (Anderlucci, Viroli (2020) <doi:10.1007/s11634-020-00399-3>) and Deep Mixture of Multinomials whose estimates are obtained with Gibbs sampling scheme (Viroli, Anderlucci (2020) <doi:10.1007/s11222-020-09989-9>). There are also functions for graphical representation of clusters obtained.
	"""
	
	cran = "deepMOU" 

	version("0.1.1", md5="c37e8dd0be1d72ded063470ded765078")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-skmeans", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
