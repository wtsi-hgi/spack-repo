# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenstat(RPackage):
	"""Statistical analysis of phenotypic data

	Package contains methods for statistical analysis of phenotypic data.
	"""
	
	bioc = "PhenStat" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PhenStat_2.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PhenStat/PhenStat_2.38.0.tar.gz"]

	version("2.38.0", md5="f28cba815b5f6e8b3350c926d1d05907")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-smoothwin", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msgps", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
