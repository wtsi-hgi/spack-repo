# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNparc(RPackage):
	"""Non-parametric analysis of response curves for thermal proteome profiling experiments

	Perform non-parametric analysis of response curves as described by Childs, Bach, Franken et al. (2019): Non-parametric analysis of thermal proteome profiles reveals novel drug-binding proteins.
	"""
	
	bioc = "NPARC"

	version("1.20.0", commit="9eafecb642092b9355c17d06db47df6956900dd5")
	version("1.14.0", commit="5f7d872848eda33551c7c3827b9d14e2149210f6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
