# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvms(RPackage):
	"""Cross-Validation for Model Selection

	Cross-validate one or multiple regression and classification models
    and get relevant evaluation metrics in a tidy format. Validate the
    best model on a test set and compare it to a baseline evaluation.
    Alternatively, evaluate predictions from an external model. Currently
    supports regression and classification (binary and multiclass).
    Described in chp. 5 of Jeyaraman, B. P., Olsen, L. R., 
    & Wambugu M. (2019, ISBN: 9781838550134).
	"""
	
	homepage = "https://github.com/ludvigolsen/cvms"
	cran = "cvms" 

	version("1.6.1", md5="bc8dcb85bd09dd622f61738905795475")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-groupdata2@2.0.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lme4@1.1.23:", type=("build", "run"))
	depends_on("r-mumin@1.43.17:", type=("build", "run"))
	depends_on("r-parameters@0.15:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-proc@1.16:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rearrr@0.3:", type=("build", "run"))
	depends_on("r-recipes@0.1.13:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
