# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsmpv(RPackage):
	"""Biomarker Confirmation, Selection, Modelling, Prediction, and
Validation

	
   There are diverse purposes such as biomarker confirmation, novel biomarker discovery, constructing predictive models, model-based prediction, and validation. 
   It handles binary, continuous, and time-to-event outcomes at the sample or patient level.
   - Biomarker confirmation utilizes established functions like glm() from 'stats', coxph() from 'survival', surv_fit(), and ggsurvplot() from 'survminer'.
   - Biomarker discovery and variable selection are facilitated by three LASSO-related functions LASSO2(), LASSO_plus(), and LASSO2plus(), leveraging the 'glmnet' R package with additional steps.
   - Eight versatile modeling functions are offered, each designed for predictive models across various outcomes and data types.
     1) LASSO2(), LASSO_plus(), LASSO2plus(), and LASSO2_reg() perform variable selection using LASSO methods and construct predictive models based on selected variables.
     2) XGBtraining() employs 'XGBoost' for model building and is the only function not involving variable selection.
     3) Functions like LASSO2_XGBtraining(), LASSOplus_XGBtraining(), and LASSO2plus_XGBtraining() combine LASSO-related variable selection with 'XGBoost' for model construction.
   - All models support prediction and validation, requiring a testing dataset comparable to the training dataset.
   Additionally, the package introduces XGpred() for risk prediction based on survival data, with the XGpred_predict() function available for predicting risk groups in new datasets.
   The methodology is based on our new algorithms and various references:
   - Hastie et al. (1992, ISBN 0 534 16765-9), 
   - Therneau et al. (2000, ISBN 0-387-98784-3), 
   - Kassambara et al. (2021) <https://CRAN.R-project.org/package=survminer>,
   - Friedman et al. (2010) <doi:10.18637/jss.v033.i01>,
   - Simon et al. (2011) <doi:10.18637/jss.v039.i05>,
   - Harrell (2023) <https://CRAN.R-project.org/package=rms>,
   - Harrell (2023) <https://CRAN.R-project.org/package=Hmisc>,
   - Chen and Guestrin (2016) <arXiv:1603.02754>,
   - Aoki et al. (2023) <doi:10.1200/JCO.23.01115>.
	"""
	
	cran = "csmpv" 

	version("1.0.3", md5="087e246a4d425842bec36df2604a3935")
	version("1.0.2", md5="907c64ff39d192402f1c916708493454")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-forestmodel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
