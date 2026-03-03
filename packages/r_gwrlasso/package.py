# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwrlasso(RPackage):
	"""A Hybrid Model for Spatial Prediction Through Local Regression

	It implements a hybrid spatial model for improved spatial prediction by combining the variable selection capability of
             LASSO (Least Absolute Shrinkage and Selection Operator) with the Geographically Weighted Regression (GWR) model that 
             captures the spatially varying relationship efficiently. For method details see, Wheeler, D.C.(2009).<DOI:10.1068/a40256>.
             The developed hybrid model efficiently selects the relevant variables by using LASSO as the first step; these selected variables
             are then incorporated into the GWR framework, allowing the estimation of spatially varying regression coefficients at unknown locations
             and finally predicting the values of the response variable at unknown test locations while taking into account the spatial heterogeneity of the data. 
             Integrating the LASSO and GWR models enhances prediction accuracy by considering spatial heterogeneity and capturing the local relationships between 
             the predictors and the response variable. The developed hybrid spatial model can be useful for spatial modeling, especially in scenarios involving complex 
             spatial patterns and large datasets with multiple predictor variables.
	"""
	
	cran = "GWRLASSO" 

	version("0.1.0", md5="f9f88eeaad39bc44ef6af073867244b3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
