# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepana(RPackage):
	"""Repeatable Analysis in R

	Set of utilities to facilitate the reproduction of analysis in R.
 It allow to make_structure(), clean_structure(), and run and log programs in a
 predefined order to allow secondary files, analysis and reports be constructed in
 an ordered and reproducible form.
	"""
	
	homepage = "https://github.com/johnaponte/repana"
	cran = "repana" 

	version("2.1.0", md5="347819093a0588dd41b3819a1d0efb8b")

	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-pool", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
