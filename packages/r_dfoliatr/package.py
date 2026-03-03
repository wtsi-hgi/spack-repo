# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfoliatr(RPackage):
	"""Detection and Analysis of Insect Defoliation Signals in Tree
Rings

	Tools to identify, quantify, analyze, and visualize growth
    suppression events in tree rings that are often produced by insect
    defoliation. Described in Guiterman et al. (2020) <doi:10.1016/j.dendro.2020.125750>.
	"""
	
	homepage = "https://chguiterman.github.io/dfoliatR/"
	cran = "dfoliatR" 

	version("0.3.0", md5="cc18ec7773862d3909d45c6bfcdbf5ec")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
