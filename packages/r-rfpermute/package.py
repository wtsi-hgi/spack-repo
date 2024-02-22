# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfpermute(RPackage):
	"""Estimate Permutation p-Values for Random Forest Importance
Metrics

	Estimate significance of importance metrics
    for a Random Forest model by permuting the response
    variable. Produces null distribution of importance
    metrics for each predictor variable and p-value of
    observed. Provides summary and visualization functions for 'randomForest' 
    results.
	"""
	
	homepage = "https://github.com/EricArcher/rfPermute"
	cran = "rfPermute" 

	version("2.5.2", md5="0088b09e40884dc2725a2029fed405c0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind@1.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-randomforest@4.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-swfscmisc@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
