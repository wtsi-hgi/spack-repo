# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampsizeval(RPackage):
	"""Sample Size for Validation of Risk Models with Binary Outcomes

	Estimation of the required sample size to validate a risk model for binary outcomes, based on the sample size equations proposed by Pavlou et al. (2021) <doi:10.1177/09622802211007522>. For precision-based sample size calculations, the user is required to enter the anticipated values of the C-statistic and outcome prevalence, which can be obtained from a previous study. The user also needs to specify the required precision (standard error) for the C-statistic, the calibration slope and the calibration in the large. The calculations are valid under the assumption of marginal normality for the distribution of the linear predictor. 
	"""
	
	homepage = "https://github.com/mpavlou/sampsizeval"
	cran = "sampsizeval" 

	version("1.0.0.0", md5="309bb31d6bd96ece04f7db43de1b74fa")

	depends_on("r-sn", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
