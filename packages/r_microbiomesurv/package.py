# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomesurv(RPackage):
	"""Biomarker Validation for Microbiome-Based Survival
Classification and Prediction

	An approach to identify microbiome biomarker for time to event data by discovering microbiome for predicting survival and classifying subjects into risk groups.
 Classifiers are constructed as a linear combination of important microbiome and treatment effects if necessary. 
 Several methods were implemented to estimate the microbiome risk score such as the LASSO method by Robert Tibshirani (1998) <doi:10.1002/(SICI)1097-0258(19970228)16:4%3C385::AID-SIM380%3E3.0.CO;2-3>, Elastic net approach by Hui Zou and Trevor Hastie (2005) <doi:10.1111/j.1467-9868.2005.00503.x>, supervised principle component analysis of Wold Svante et al. (1987) <doi:10.1016/0169-7439(87)80084-9>, and supervised partial least squares analysis by Inge S. Helland <https://www.jstor.org/stable/4616159>.
 Sensitivity analysis on the quantile used for the classification can also be accessed to check the deviation of the classification group based on the quantile specified. Large scale cross validation can be performed in order to investigate the mostly selected microbiome and for internal validation.
 During the evaluation process, validation is accessed using the hazard ratios (HR) distribution of the test set and inference is mainly based on resampling and permutations technique.
	"""
	
	homepage = "https://github.com/N-T-Huyen/MicrobiomeSurv"
	cran = "MicrobiomeSurv" 

	version("0.1.0", md5="b8fbf9430af841b1b57e1afca44480bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-superpc", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-microbiome", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
