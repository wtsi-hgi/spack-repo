# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValse(RPackage):
	"""Variable Selection with Mixture of Models

	Two methods are implemented to cluster data with finite mixture
    regression models. Those procedures deal with high-dimensional covariates and
    responses through a variable selection procedure based on the Lasso estimator.
    A low-rank constraint could be added, computed for the Lasso-Rank procedure.
    A collection of models is constructed, varying the level of sparsity and the
    number of clusters, and a model is selected using a model selection criterion
    (slope heuristic, BIC or AIC). Details of the procedure are provided in
    "Model-based clustering for high-dimensional data. Application to functional data"
    by Emilie Devijver (2016) <arXiv:1409.1333v2>,
    published in Advances in Data Analysis and Clustering.
	"""
	
	homepage = "https://git.auder.net/?p=valse.git"
	cran = "valse" 

	version("0.1-0", md5="8ed15c96be34fde0ea3f5b6d3c03745a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
