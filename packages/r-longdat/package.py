# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongdat(RPackage):
	"""A Tool for 'Covariate'-Sensitive Longitudinal Analysis on
'omics' Data

	This tool takes longitudinal dataset as input and analyzes if there is significant 
             change of the features over time (a proxy for treatments), while detects and controls 
             for 'covariates' simultaneously. 'LongDat' is able to take in several data types as input, 
             including count, proportion, binary, ordinal and continuous data. The output table contains 
              p values, effect sizes and 'covariates' of each feature, making the downstream analysis easy.
	"""
	
	homepage = "https://github.com/CCY-dev/LongDat"
	cran = "LongDat" 

	version("1.1.2", md5="ac27f0c7661e8cb9b0b99925faf7598b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-bestnormalize", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
