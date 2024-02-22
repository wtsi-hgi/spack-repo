# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegtools(RPackage):
	"""Regression and Classification Tools

	Tools for linear, nonlinear and nonparametric regression
             and classification.  Novel graphical methods for assessment 
             of parametric models using nonparametric methods. One 
             vs. All and All vs. All multiclass classification, optional
             class probabilities adjustment.  Nonparametric regression 
             (k-NN) for general dimension, local-linear option.  Nonlinear 
             regression with Eickert-White method for dealing with 
             heteroscedasticity.  Utilities for converting time series
             to rectangular form.  Utilities for conversion between
             factors and indicator variables.  Some code related to
             "Statistical Regression and Classification: from Linear
             Models to Machine Learning", N. Matloff, 2017, CRC,
             ISBN 9781498710916.
	"""
	
	homepage = "https://github.com/matloff/regtools"
	cran = "regtools" 

	version("1.7.0", md5="6cbf6a5af60112074e2ea57d082e74bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rje", type=("build", "run"))
	depends_on("r-text2vec", type=("build", "run"))
	depends_on("r-polyreg", type=("build", "run"))
