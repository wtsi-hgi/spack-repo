# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpm2(RPackage):
	"""Spatial Predictive Modeling

	An updated and extended version of 'spm' package, by introducing some further novel functions for modern statistical methods (i.e., generalised linear models, glmnet, generalised least squares), thin plate splines, support vector machine, kriging methods (i.e., simple kriging, universal kriging, block kriging, kriging with an external drift), and novel hybrid methods (228 hybrids plus numerous variants) of modern statistical methods or machine learning methods with mathematical and/or univariate geostatistical methods for spatial predictive modelling. For each method, two functions are provided, with one function for assessing the predictive errors and accuracy of the method based on cross-validation, and the other for generating spatial predictions. It also contains a couple of functions for data preparation and predictive accuracy assessment. 
	"""
	
	cran = "spm2" 

	version("1.1.3", md5="1551105b49b5b8803d9945477943ddc8", url="https://cran.r-project.org/src/contrib/spm2_1.1.3.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-spm", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
