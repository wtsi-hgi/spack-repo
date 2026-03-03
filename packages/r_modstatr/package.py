# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModstatr(RPackage):
	"""Statistical Modelling in Action with R

	Datasets and functions for the book "Modélisation statistique par la pratique avec R", F. Bertrand, E. Claeys and M. Maumy-Bertrand (2019, ISBN:9782100793525, Dunod, Paris). The first chapter of the book is dedicated to an introduction to the R statistical software. The second chapter deals with correlation analysis: Pearson, Spearman and Kendall simple, multiple and partial correlation coefficients. New wrapper functions for permutation tests or bootstrap of matrices of correlation are provided with the package. The third chapter is dedicated to data exploration with factorial analyses (PCA, CA, MCA, MDA) and clustering. The fourth chapter is dedicated to regression analysis: fitting and model diagnostics are detailed. The exercises focus on covariance analysis, logistic regression, Poisson regression, two-way analysis of variance for fixed or random factors. Various example datasets are shipped with the package: for instance on pokemon, world of warcraft, house tasks or food nutrition analyses.
	"""
	
	homepage = "https://fbertran.github.io/homepage/"
	cran = "ModStatR" 

	version("1.3.3", md5="af2ecdecfae5a382ae643e6102497f02")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-jmuoutlier", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
