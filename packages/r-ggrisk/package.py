# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrisk(RPackage):
	"""Risk Score Plot for Cox Regression

	The risk plot may be one of the most commonly used figures in 
    tumor genetic data analysis. We can conclude the following two points: 
    Comparing the prediction results of the model with the real survival situation 
    to see whether the survival rate of the high-risk group is lower than that of the 
    low-level group, and whether the survival time of the high-risk group is 
    shorter than that of the low-risk group. The other is to compare the heat 
    map and scatter plot to see the correlation between the predictors and the 
    outcome.
	"""
	
	homepage = "https://github.com/yikeshu0611/ggrisk"
	cran = "ggrisk" 

	version("1.3", md5="ea6fce4d90768de096e57d1b809d15f5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-do", type=("build", "run"))
	depends_on("r-set", type=("build", "run"))
	depends_on("r-cutoff", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-nomogramformula", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
