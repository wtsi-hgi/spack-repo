# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXadmix(RPackage):
	"""Subsetting and Plotting Optimized for Admixture Data

	A few functions which provide a quick way of subsetting
    genomic admixture data and generating customizable stacked barplots.
	"""
	
	homepage = "https://github.com/SpaceCowboy-71/xadmix"
	cran = "xadmix" 

	version("1.0.0", md5="78c2947b554b7646a7b0b809d2e1f9b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
