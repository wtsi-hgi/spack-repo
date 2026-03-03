# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWoodsimulatr(RPackage):
	"""Generate Simulated Sawn Timber Strength Grading Data

	Tools for generating simulated sawn timber
    strength grading data with a main focus on statistical simulation based on
    covariance matrices. Simulation data
    for Norway spruce sawn timber from Austria and reference values of means and
    standard deviations of grade determining properties from literature
    for a number of European countries are provided, as well.
	"""
	
	cran = "WoodSimulatR" 

	version("0.6.1", md5="ca061bd06b507c3fe816ea65e4dfe170")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
