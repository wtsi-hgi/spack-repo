# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidypredict(RPackage):
	"""Run Predictions Inside the Database

	It parses a fitted 'R' model object, and returns a formula in
    'Tidy Eval' code that calculates the predictions.  It works with
    several databases back-ends because it leverages 'dplyr' and 'dbplyr'
    for the final 'SQL' translation of the algorithm. It currently
    supports lm(), glm(), randomForest(), ranger(), earth(),
    xgb.Booster.complete(), cubist(), and ctree() models.
	"""
	
	homepage = "https://tidypredict.tidymodels.org"
	cran = "tidypredict" 

	version("0.5", md5="abf2f576e202e257d7640f15ee04c2ee")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
