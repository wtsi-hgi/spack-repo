# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNncc(RPackage):
	"""Nearest Neighbors Matching of Case-Control Data

	Provides nearest-neighbors matching and 
    analysis of case-control data. Cui, Z., Marder, E. P., Click, E. S., 
    Hoekstra, R. M., & Bruce, B. B. (2022) <doi:10.1097/EDE.0000000000001504>.
	"""
	
	cran = "nncc" 

	version("2.0.0", md5="3817650b350580070d1e3910682c5169")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
