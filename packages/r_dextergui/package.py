# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDextergui(RPackage):
	"""A Graphical User Interface for Dexter

	Classical Test and Item analysis, 
  Item Response analysis and data management for educational and psychological tests.
	"""
	
	homepage = "https://dexter-psychometrics.github.io/dexter/"
	cran = "dextergui" 

	version("0.2.6", md5="990661471696e845c508ab34aa3e14a0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dexter@1.2.1:", type=("build", "run"))
	depends_on("r-shiny@1.3:", type=("build", "run"))
	depends_on("r-shinybs@0.6:", type=("build", "run"))
	depends_on("r-dt@0.9:", type=("build", "run"))
	depends_on("r-htmltools@0.4:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.3:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-shinyfiles@0.9.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rcurl@1.95:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-readxl@1.1:", type=("build", "run"))
	depends_on("r-writexl@1:", type=("build", "run"))
	depends_on("r-readods@1.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ggextra@0.8:", type=("build", "run"))
	depends_on("r-ggridges@0.5.1:", type=("build", "run"))
	depends_on("r-networkd3@0.4:", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
