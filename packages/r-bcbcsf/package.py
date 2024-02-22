# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcbcsf(RPackage):
	"""Bias-Corrected Bayesian Classification with Selected Features

	Fully Bayesian Classification with a subset of high-dimensional features, such as expression levels of genes. The data are modeled with a hierarchical Bayesian models using heavy-tailed t distributions as priors. When a large number of features are available, one may like to select only a subset of features to use, typically those features strongly correlated with the response in training cases. Such a feature selection procedure is however invalid since the relationship between the response and the features has be exaggerated by feature selection. This package provides a way to avoid this bias and yield better-calibrated predictions for future cases when one uses F-statistic to select features. 
	"""
	
	homepage = "http://www.r-project.org"
	cran = "BCBCSF" 

	version("1.0-1", md5="db48e4433214b8cfa6fcbb85f7fee421")

	depends_on("r@2.13.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
