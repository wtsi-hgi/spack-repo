# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondis(RPackage):
	"""Censored Data Imputation for Direct Modeling

	Impute the survival times for censored observations based on their conditional survival distributions derived from the Kaplan-Meier estimator. 'CondiS' can replace the censored observations with the best approximations from the statistical model, allowing for direct application of machine learning-based methods. When covariates are available, 'CondiS' is extended by incorporating the covariate information through machine learning-based regression modeling ('CondiS_X'), which can further improve the imputed survival time.
	"""
	
	cran = "CondiS" 

	version("0.1.2", md5="bc3edd6b0502d281483bc1ca26ca1801")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
