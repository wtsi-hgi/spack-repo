# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutomrp(RPackage):
	"""Improving MrP with Ensemble Learning

	A tool that improves the prediction performance of multilevel
    regression with post-stratification (MrP) by combining a number of machine
    learning methods. For information on the method, please refer to Broniecki, 
	Wüest, Leemann (2020) ''Improving Multilevel Regression with 
	Post-Stratification Through Machine Learning (autoMrP)'' in the 
	'Journal of Politics'. Final pre-print version: 
	<https://lucasleemann.files.wordpress.com/2020/07/automrp-r2pa.pdf>.
	"""
	
	homepage = "https://github.com/retowuest/autoMrP"
	cran = "autoMrP" 

	version("1.0.6", md5="b00ff7345271090c8bc6ad5b3e8164f7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-lme4@1.1:", type=("build", "run"))
	depends_on("r-gbm@2.1.5:", type=("build", "run"))
	depends_on("r-e1071@1.7.3:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-glmmlasso@1.5.1:", type=("build", "run"))
	depends_on("r-ebmaforecast@1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
	depends_on("r-dorng@1.8.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-knitr@1.29:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-vglmer@1.0.3:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
