# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvsim(RPackage):
	"""Electric Vehicle Charging Sessions Simulation

	Simulation of Electric Vehicles charging sessions using 
    Gaussian models, together with time-series power demand calculations. 
    The simulation methodology is published in 
    Cañigueral et al. (2023, ISBN:0957-4174) <doi:10.1016/j.eswa.2023.120318>.
	"""
	
	homepage = "https://mcanigueral.github.io/evsim/"
	cran = "evsim" 

	version("1.4.0", md5="e7402387d42077a58ee28d3bc24b3d64")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
