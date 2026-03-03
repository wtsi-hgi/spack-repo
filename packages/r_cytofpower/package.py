# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytofpower(RPackage):
	"""Power analysis for CyTOF experiments

	This package is a tool to predict the power of CyTOF experiments in the context of differential state analyses. The package provides a shiny app with two options to predict the power of an experiment: i. generation of in-sicilico CyTOF data, using users input ii. browsing in a grid of parameters for which the power was already precomputed.
	"""
	
	bioc = "CyTOFpower" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CyTOFpower_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CyTOFpower/CyTOFpower_1.8.0.tar.gz"]

	version("1.8.0", md5="ea70d698bf8ba363250de04f634c5f74")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cytoglmm", type=("build", "run"))
	depends_on("r-diffcyt", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
