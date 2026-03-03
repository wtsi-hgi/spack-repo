# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCauscor(RPackage):
	"""Calculate Correlations and Estimate Causality

	This tool performs pairwise correlation analysis and estimate causality.
    Particularly, it is useful for detecting the metabolites that would be altered by the gut bacteria.
	"""
	
	homepage = "https://github.com/sugym/CausCor"
	cran = "CausCor" 

	version("0.1.3", md5="8716efe75bde239cbc5ea564ebe8db44")

	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
