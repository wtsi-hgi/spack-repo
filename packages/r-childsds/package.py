# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChildsds(RPackage):
	"""Data and Methods Around Reference Values in Pediatrics

	Calculation of standard deviation scores and percentiles adduced from different
    standards (WHO, UK, Germany, Italy, China, etc). Also, references for laboratory values in
    children and adults are available, e.g., serum lipids, iron-related blood parameters, IGF, liver enzymes. See package documentation for full list.
	"""
	
	cran = "childsds" 

	version("0.8.0", md5="14e177a0a7503e9cce47cfe47793a5af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-purrrlyr", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
