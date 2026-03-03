# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHandwriter(RPackage):
	"""Handwriting Analysis in R

	Perform statistical writership analysis of scanned handwritten documents.
             Webpage provided at: <https://github.com/CSAFE-ISU/handwriter>.
	"""
	
	homepage = "https://github.com/CSAFE-ISU/handwriter"
	cran = "handwriter" 

	version("3.0.0", md5="ac2ad84267ff8b6a29f1cb52a2999a4c")
	version("2.0.3", md5="7a411d25ebe65d01812420acd451655e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
