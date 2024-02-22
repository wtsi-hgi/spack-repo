# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpcr(RPackage):
	"""Ensemble Penalized Cox Regression for Survival Prediction

	The top-performing ensemble-based Penalized Cox Regression (ePCR) framework developed during the DREAM 9.5 mCRPC Prostate Cancer Challenge <https://www.synapse.org/ProstateCancerChallenge> presented in Guinney J, Wang T, Laajala TD, et al. (2017) <doi:10.1016/S1470-2045(16)30560-5> is provided here-in, together with the corresponding follow-up work. While initially aimed at modeling the most advanced stage of prostate cancer, metastatic Castration-Resistant Prostate Cancer (mCRPC), the modeling framework has subsequently been extended to cover also the non-metastatic form of advanced prostate cancer (CRPC). Readily fitted ensemble-based model S4-objects are provided, and a simulated example dataset based on a real-life cohort is provided from the Turku University Hospital, to illustrate the use of the package. Functionality of the ePCR methodology relies on constructing ensembles of strata in patient cohorts and averaging over them, with each ensemble member consisting of a highly optimized penalized/regularized Cox regression model. Various cross-validation and other modeling schema are provided for constructing novel model objects.
	"""
	
	cran = "ePCR" 

	version("0.11.0", md5="386f26a685e8cf7a9118ab91264c2e6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-hamlet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-timeroc", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-bolstad2", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
