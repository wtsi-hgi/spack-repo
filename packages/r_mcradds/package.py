# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcradds(RPackage):
	"""Processing and Analyzing of Diagnostics Trials

	Provides methods and functions to analyze the quantitative or 
    qualitative performance for diagnostic assays, and outliers detection, 
    reader precision and reference range are discussed. Most of the methods 
    and algorithms refer to CLSI (Clinical & Laboratory Standards Institute) 
    recommendations and NMPA (National Medical Products Administration) 
    guidelines. In additional, relevant plots are constructed by 'ggplot2'.
	"""
	
	homepage = "https://github.com/kaigu1990/mcradds"
	cran = "mcradds" 

	version("1.1.0", md5="96de2a012899226d45768c430cb7eb96")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formatters", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mcr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vca", type=("build", "run"))
