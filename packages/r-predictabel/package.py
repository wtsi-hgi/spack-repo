# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictabel(RPackage):
	"""Assessment of Risk Prediction Models

	We included functions to assess the performance of
 risk models. The package contains functions for the various measures that are
 used in empirical studies, including univariate and multivariate odds ratios
 (OR) of the predictors, the c-statistic (or area under the receiver operating
 characteristic (ROC) curve (AUC)), Hosmer-Lemeshow goodness of fit test,
 reclassification table, net reclassification improvement (NRI) and
 integrated discrimination improvement (IDI). Also included are functions
 to create plots, such as risk distributions, ROC curves, calibration plot,
 discrimination box plot and predictiveness curves. In addition to functions
 to assess the performance of risk models, the package includes functions to
 obtain weighted and unweighted risk scores as well as predicted risks using
 logistic regression analysis. These logistic regression functions are
 specifically written for models that include genetic variables, but they
 can also be applied to models that are based on non-genetic risk factors only.
 Finally, the package includes function to construct a simulated dataset with 
 genotypes, genetic risks, and disease status for a hypothetical population, which 
 is used for the evaluation of genetic risk models.
	"""
	
	cran = "PredictABEL" 

	version("1.2-4", md5="c404e14d5bcfe9a61d8657d21f3352e5")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-pbsmodelling", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
