# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompran(RPackage):
	"""Complexome Profiling Analysis package

	This package is for analysis of SILAC labeled complexome profiling data. It uses peptide table in tab-delimited format as an input and produces ready-to-use tables and plots.
	"""
	
	bioc = "ComPrAn" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ComPrAn_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ComPrAn/ComPrAn_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="b314d05828ddfbbf17adf9d02e7aa992de05a6318e9c88a156cadcd7b7c68a1b")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
