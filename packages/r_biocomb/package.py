# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocomb(RPackage):
	"""Feature Selection and Classification with the Embedded
Validation Procedures for Biomedical Data Analysis

	Contains functions for the data analysis with the emphasis on biological data, including several algorithms for feature ranking, feature selection, classification
 algorithms with the embedded validation procedures.
 The functions can deal with numerical as well as with nominal features. Includes also the functions for calculation
 of feature AUC (Area Under the ROC Curve) and HUM (hypervolume under manifold) values and construction 2D- and 3D- ROC curves.
 Provides the calculation of Area Above the RCC (AAC) values and construction of Relative Cost Curves
 (RCC) to estimate the classifier performance under unequal misclassification costs problem.
 There exists the special function to deal with missing values, including different imputing schemes.
	"""
	
	cran = "Biocomb" 

	version("0.4", md5="5218452583b52ad6060af90ce406c56e")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-fselector", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
