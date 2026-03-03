# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntegratedmrf(RPackage):
	"""Integrated Prediction using Uni-Variate and Multivariate Random
Forests

	An implementation of a framework for drug sensitivity prediction from various genetic characterizations using ensemble approaches. Random Forests or Multivariate Random Forest predictive models can be generated from each genetic characterization that are then combined using a Least Square Regression approach. It also provides options for the use of different error estimation approaches of Leave-one-out, Bootstrap, N-fold cross validation and 0.632+Bootstrap along with generation of prediction confidence interval using Jackknife-after-Bootstrap approach. 
	"""
	
	cran = "IntegratedMRF" 

	version("1.1.9", md5="c27d43d1eef69104bc9d30107e04bfba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-multivariaterandomforest", type=("build", "run"))
