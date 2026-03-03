# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcep(RPackage):
	"""Survival Analysis for Weighted Composite Endpoints

	Analyze given data frame with multiple endpoints and return Kaplan-Meier survival probabilities together with the specified confidence interval. See Nabipoor M, Westerhout CM, Rathwell S, and Bakal JA (2023) <doi:10.1186/s12874-023-01857-0>.
	"""
	
	homepage = "https://github.com/sarah-0k/wcep"
	cran = "wcep" 

	version("1.0.2", md5="20f84353b475fb4652c57db7048045f2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-coin@1.3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
