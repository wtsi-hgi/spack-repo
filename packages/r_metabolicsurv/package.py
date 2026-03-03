# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabolicsurv(RPackage):
	"""A Biomarker Validation Approach for Classification and
Predicting Survival Using Metabolomics Signature

	An approach to identifies metabolic biomarker signature for metabolic data by discovering predictive metabolite for predicting survival and classifying patients into risk groups. 
 Classifiers are constructed as a linear combination of predictive/important metabolites, prognostic factors and treatment effects if necessary. 
 Several methods were implemented to reduce the metabolomics matrix such as the  principle component analysis of Wold Svante et al. (1987) <doi:10.1016/0169-7439(87)80084-9> , 
 the LASSO method by Robert Tibshirani (1998) <doi:10.1002/(SICI)1097-0258(19970228)16:4%3C385::AID-SIM380%3E3.0.CO;2-3>, the 
 elastic net approach by Hui Zou and Trevor Hastie (2005) <doi:10.1111/j.1467-9868.2005.00503.x>. 
 Sensitivity analysis on the quantile used for the classification can also be accessed to check the deviation of the classification group based on the quantile specified. 
 Large scale cross validation can be performed in  order to investigate the mostly selected predictive metabolites and for internal validation. During the evaluation process, validation is accessed using the hazard ratios (HR) distribution of the test set and inference is mainly based on resampling and permutations technique.
	"""
	
	homepage = "https://github.com/OlajumokeEvangelina/MetabolicSurv"
	cran = "MetabolicSurv" 

	version("1.1.2", md5="35a0f3095f605ae531b393b7bdb98018")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-superpc", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
