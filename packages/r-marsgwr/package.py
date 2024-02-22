# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarsgwr(RPackage):
	"""A Hybrid Spatial Model for Capturing Spatially Varying
Relationships Between Variables in the Data

	It is a hybrid spatial model that combines the strength of two widely used regression models, MARS (Multivariate Adaptive Regression Splines) and
             GWR (Geographically Weighted Regression) to provide an effective approach for predicting a response variable at unknown locations. The MARS model
             is used in the first step of the development of a hybrid model to identify the most important predictor variables that assist in predicting the response
             variable. For method details see, Friedman, J.H. (1991). <DOI:10.1214/aos/1176347963>.The GWR model is then used to predict the response variable at 
             testing locations based on these selected variables that account for spatial variations in the relationships between the variables. This hybrid model 
             can improve the accuracy of the predictions compared to using an individual model alone.This developed hybrid spatial model can be useful particularly in 
             cases where the relationship between the response variable and predictor variables is complex and non-linear, and varies across locations.
	"""
	
	cran = "MARSGWR" 

	version("0.1.0", md5="aa1bd88ecb124da1629a5c73d45a9a8b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
