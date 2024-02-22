# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsnell(RPackage):
	"""Snell Scoring

	The Snell scoring procedure, implemented in R. This procedure was first described by E.J Snell (1964) <doi:10.2307/2528498> and was later used by Tong et al (1977) <doi:10.4141/cjas77-001> in dairy.
	"""
	
	homepage = "https://github.com/pfpetrowski/rsnell"
	cran = "rsnell" 

	version("0.1", md5="f06b3ef6718fb9167f0089f0e178a013")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
