# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvprof(RPackage):
	"""Electric Vehicle Charging Sessions Profiling and Modelling

	Tools for modelling electric vehicle charging sessions into
    generic groups with similar connection patterns called "user profiles",
    using Gaussian Mixture Models clustering. The clustering and profiling
    methodology is described in Cañigueral and Meléndez (2021, ISBN:0142-0615) 
    <doi:10.1016/j.ijepes.2021.107195>.
	"""
	
	homepage = "https://github.com/mcanigueral/evprof/"
	cran = "evprof" 

	version("1.1.2", md5="5e63095aa156550af9929f14d7dd8d83")
	version("1.1.1", md5="bf59693da4887a3e5796d4689ad03928")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
