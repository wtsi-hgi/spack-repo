# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamisc(RPackage):
	"""Meta-Analysis of Diagnosis and Prognosis Research Studies

	Facilitate frequentist and Bayesian meta-analysis of diagnosis and prognosis research studies. It includes functions to  summarize multiple estimates of prediction model discrimination and calibration performance (Debray et al., 2019) <doi:10.1177/0962280218785504>. It also includes functions to evaluate funnel plot asymmetry (Debray et al., 2018) <doi:10.1002/jrsm.1266>. Finally, the package provides functions for developing multivariable prediction models from datasets with clustering (de Jong et al., 2021) <doi:10.1002/sim.8981>. 
	"""
	
	homepage = "https://github.com/smartdata-analysis-and-statistics/metamisc"
	cran = "metamisc" 

	version("0.4.0", md5="a709599ba12b01fa7b3e51e9116ebac5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-metafor@2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
