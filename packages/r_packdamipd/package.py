# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackdamipd(RPackage):
	"""Decision Analysis Modelling Package with Parameters Estimation
Ability from Individual Patient Level Data

	A collection of functions to construct Markov model for model-based 
    cost-effectiveness analysis. This includes creating Markov model (both time
    homogenous and time dependent models), decision analysis, sensitivity 
    analysis (deterministic and probabilistic). The package allows estimation 
    of parameters for the Markov model from a given individual patient level 
    data, provided the data file follows some standard data entry rules. 
	"""
	
	homepage = "https://github.com/sheejamk/packDAMipd"
	cran = "packDAMipd" 

	version("1.1.0", md5="e0f4ad7aa9cc40327e158ecadfcb19b8")
	version("0.2.2", md5="46f64e9a822ef32c713898c57f3cc810")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-survregcenscov", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
	depends_on("r-ipdfilecheck", type=("build", "run"))
	depends_on("r-valueeq5d", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
	depends_on("r-gvlma", type=("build", "run"))
	depends_on("r-relaimpo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-islr", type=("build", "run"))
