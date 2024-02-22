# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbbe(RPackage):
	"""Model Based Bio-Equivalence

	Uses several Nonlinear Mixed effect (NONMEM) models (as NONMEM control files)
    to perform bootstrap model averaging and Monte Carlo Simulation for Model Based 
    Bio-Equivalence (MBBE). Power is returned as the fraction of the simulations with 
    successful bioequivalence (BE) test, for maximum concentration (Cmax), Area under the 
    curve to the last observed value (AUClast) and Area under the curve extrapolate to 
    infinity (AUCinf). See Hooker, A. (2020) Improved bioequivalence assessment through 
    model-informed and model-based strategies <https://www.fda.gov/media/138035/download>.
	"""
	
	homepage = "https://github.com/certara/mbbe"
	cran = "mbbe" 

	version("0.1.0", md5="117447e5239b3ed4aeeb0f2282a004cc")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-pknca", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr@0.3.1:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ps", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
