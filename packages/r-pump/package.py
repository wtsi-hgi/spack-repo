# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPump(RPackage):
	"""Power Under Multiplicity Project

	Estimates power, minimum detectable effect size (MDES) and sample size requirements. The context is multilevel randomized experiments with multiple outcomes. The estimation takes into account the use of multiple testing procedures. Development of this package was supported by a grant from the Institute of Education Sciences (R305D170030). For a full package description, including a detailed technical appendix, see <doi:10.18637/jss.v108.i06>.
	"""
	
	homepage = "https://github.com/MDRCNY/PUMP"
	cran = "PUMP" 

	version("1.0.3", md5="65a58b1aed60db8cb86514755a6bcb17")
	version("1.0.2", md5="dbcef63a76d61b1622a8573776b5bd8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-randomizr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
