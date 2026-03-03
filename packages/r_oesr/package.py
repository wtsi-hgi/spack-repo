# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROesr(RPackage):
	"""Methods for the Office of Evaluation Sciences

	Methods for statistical analysis and reporting preferred by the US Office of Evaluation Sciences (OES). This package prepares data from standard model output objects (such as from code{lm()} and code{estimatr::lm_robust()}) and creates visualizations of treatment effects from the prepared quantities, according to the standards of the US Office of Evaluation Sciences.
	"""
	
	cran = "oesr" 

	version("0.1.0", md5="3e629e94730f8311853e6ce863a41188")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
