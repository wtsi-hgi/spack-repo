# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsfmi(RPackage):
	"""Prediction Model Pooling, Selection and Performance Evaluation
Across Multiply Imputed Datasets

	
	Pooling, backward and forward selection of linear, logistic and Cox regression models in 
	multiply imputed datasets. Backward and forward selection can be done 
	from the pooled model using Rubin's Rules (RR), the D1, D2, D3, D4 and 
	the median p-values method. This is also possible for Mixed models. 
	The models can contain continuous, dichotomous, categorical and restricted 
	cubic spline predictors and interaction terms between	all these type of predictors. 
	The stability of the models	can be evaluated using (cluster) bootstrapping. The package 
	further contains functions to pool model performance measures as ROC/AUC, Reclassification, 
	R-squared, scaled Brier score, H&L test and calibration	plots for logistic regression models. 
	Internal validation can be done across multiply imputed datasets with cross-validation or 
	bootstrapping. The adjusted intercept after shrinkage of pooled regression coefficients 
	can be obtained. Backward and forward selection as part of internal validation is possible. 
	A function to externally validate logistic prediction models in multiple imputed 
	datasets is available and a function to compare models. For Cox models a strata variable
	can be included.
	Eekhout (2017) <doi:10.1186/s12874-017-0404-7>.
	Wiel (2009) <doi:10.1093/biostatistics/kxp011>.
	Marshall (2009) <doi:10.1186/1471-2288-9-57>.
	"""
	
	homepage = "https://mwheymans.github.io/psfmi/"
	cran = "psfmi" 

	version("1.4.0", md5="446279993c1480cd1bee281ba268d9c4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mitools", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-mitml", type=("build", "run"))
	depends_on("r-cvauc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
