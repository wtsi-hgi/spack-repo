# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeogam(RPackage):
	"""Select Sparse Geoadditive Models for Spatial Prediction

	A model building procedure to build parsimonious geoadditive model from a large number of covariates. Continuous, binary and ordered categorical responses are supported. The model building is based on component wise gradient boosting with linear effects, smoothing splines and a smooth spatial surface to model spatial autocorrelation. The resulting covariate set after gradient boosting is further reduced through backward elimination and aggregation of factor levels. The package provides a model based bootstrap method to simulate prediction intervals for point predictions. A test data set of a soil mapping case study in Berne (Switzerland) is provided. Nussbaum, M., Walthert, L., Fraefel, M., Greiner, L., and Papritz, A. (2017) <doi:10.5194/soil-3-191-2017>. 
	"""
	
	cran = "geoGAM" 

	version("0.1-3", md5="d856f858254f0c34ff12f1dff453c247")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
