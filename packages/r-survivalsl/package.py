# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalsl(RPackage):
	"""Super Learner for Survival Prediction from Censored Data

	Several functions and S3 methods to construct a super learner in the presence of censored times-to-event and to evaluate its prognostic capacities.
	"""
	
	cran = "survivalSL" 

	version("0.92", md5="38b436f762628f0f5b625a3e47706233")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-date", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
	depends_on("r-survivalmodels", type=("build", "run"))
	depends_on("r-hdnom", type=("build", "run"))
	depends_on("r-glmnetutils", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
