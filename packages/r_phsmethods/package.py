# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhsmethods(RPackage):
	"""Standard Methods for Use in Public Health Scotland

	A collection of methods for commonly undertaken analytical
    tasks, primarily developed for Public Health Scotland (PHS) analysts,
    but the package is also generally useful to others working in the
    healthcare space, particularly since it has functions for working with
    Community Health Index (CHI) numbers. The package can help to make
    data manipulation and analysis more efficient and reproducible.
	"""
	
	homepage = "https://github.com/Public-Health-Scotland/phsmethods"
	cran = "phsmethods" 

	version("1.0.2", md5="90246e816506571a899fa55c2b82beb2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
