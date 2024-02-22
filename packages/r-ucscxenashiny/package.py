# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcscxenashiny(RPackage):
	"""Interactive Analysis of UCSC Xena Data

	Provides functions and a Shiny application for downloading,
    analyzing and visualizing datasets from UCSC Xena
    (<http://xena.ucsc.edu/>), which is a collection of UCSC-hosted public
    databases such as TCGA, ICGC, TARGET, GTEx, CCLE, and others.
	"""
	
	homepage = "https://github.com/openbiox/UCSCXenaShiny"
	cran = "UCSCXenaShiny" 

	version("1.1.10", md5="8cdbb835e84233d0dca9109a2d353f04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-ezcox", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-ggpubr@0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny@1.3.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ucscxenatools", type=("build", "run"))
