# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepgwr(RPackage):
	"""A Hybrid Spatial Model for Prediction and Capturing Spatial
Variation in the Data

	It is a hybrid spatial model that combines the variable selection capabilities of stepwise regression methods with the predictive power of the Geographically 
             Weighted Regression(GWR) model.The developed hybrid model follows a two-step approach where the stepwise variable selection method is applied first to identify 
             the subset of predictors that have the most significant impact on the response variable, and then a GWR model is fitted using those selected variables for spatial 
             prediction at test or unknown locations. For method details,see Leung, Y., Mei, C. L. and Zhang, W. X. (2000).<DOI:10.1068/a3162>.This hybrid spatial model aims to 
             improve the accuracy and interpretability of GWR predictions by selecting a subset of relevant variables through a stepwise selection process.This approach is particularly 
             useful for modeling spatially varying relationships and improving the accuracy of spatial predictions.
	"""
	
	cran = "StepGWR" 

	version("0.1.0", md5="7b695b56f34f63c4dca0a03433840ec5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
