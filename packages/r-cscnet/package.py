# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCscnet(RPackage):
	"""Fitting and Tuning Regularized Cause-Specific Cox Models with
Elastic-Net Penalty

	Flexible tools to fit, tune and obtain absolute risk predictions from regularized cause-specific cox models with elastic-net penalty.
	"""
	
	cran = "CSCNet" 

	version("0.1.2", md5="d8e985c517ce36f2461bdbabf48ae1d1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyverse@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-survival@3.3.1:", type=("build", "run"))
	depends_on("r-prodlim@2019.11.13:", type=("build", "run"))
	depends_on("r-riskregression@2022.3.22:", type=("build", "run"))
	depends_on("r-glmnet@4.1.4:", type=("build", "run"))
	depends_on("r-caret@6.0.92:", type=("build", "run"))
	depends_on("r-recipes@0.2:", type=("build", "run"))
	depends_on("r-future@1.26.1:", type=("build", "run"))
	depends_on("r-furrr@0.3:", type=("build", "run"))
