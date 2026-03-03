# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAihuman(RPackage):
	"""Experimental Evaluation of Algorithm-Assisted Human
Decision-Making

	Provides statistical methods for analyzing experimental 
    evaluation of the causal impacts of algorithmic recommendations 
    on human decisions developed by Imai, Jiang, Greiner, Halen, and 
    Shin (2023) <doi:10.1093/jrsssa/qnad010>.
    The data used for this paper, and made available here, are interim, 
    based on only half of the observations in the study and (for those 
    observations) only half of the study follow-up period. We use them 
    only to illustrate methods, not to draw substantive conclusions.
	"""
	
	homepage = "https://github.com/sooahnshin/aihuman"
	cran = "aihuman" 

	version("0.1.0", md5="a636866ef04b04b41eba2d30a10ee9b8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
