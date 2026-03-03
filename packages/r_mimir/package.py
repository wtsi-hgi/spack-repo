# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimir(RPackage):
	"""Metabolomics-Based Models for Imputing Risk

	Provides an intuitive framework for ad-hoc statistical analysis of 1H-NMR metabolomics by Nightingale Health. It allows to easily explore new metabolomics measurements assayed by Nightingale Health, comparing the distributions with a large Consortium (BBMRI-nl); project previously published metabolic scores [<doi:10.1016/j.ebiom.2021.103764>, <doi:10.1161/CIRCGEN.119.002610>, <doi:10.1038/s41467-019-11311-9>, <doi:10.7554/eLife.63033>, <doi:10.1161/CIRCULATIONAHA.114.013116>, <doi:10.1007/s00125-019-05001-w>]; and calibrate the metabolic surrogate values to a desired dataset.   
	"""
	
	cran = "MiMIR" 

	version("1.5", md5="c4457ad2eaca5acb555cff0c5bce8804")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
