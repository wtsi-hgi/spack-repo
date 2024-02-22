# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRang(RPackage):
	"""Reconstructing Reproducible R Computational Environments

	Resolve the dependency graph of R packages at a specific time point based on the information from various 'R-hub' web services <https://blog.r-hub.io/>. The dependency graph can then be used to reconstruct the R computational environment with 'Rocker' <https://rocker-project.org>.
	"""
	
	homepage = "https://github.com/gesistsa/rang"
	cran = "rang" 

	version("0.3.0", md5="42f3a338f4a2bb1fc0f4e084b787971c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pkgsearch", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
