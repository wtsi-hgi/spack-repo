# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoicer(RPackage):
	"""Voice Analytics for Social Scientists

	Simplifies and largely automates practical voice analytics for social science research. This package offers an accessible and easy-to-use interface, including an interactive Shiny app, that simplifies the processing, extraction, analysis, and reporting of voice recording data in the behavioral and social sciences. The package includes batch processing capabilities to read and analyze multiple voice files in parallel, automates the extraction of key vocal features for further analysis, and automatically generates APA formatted reports for typical between-group comparisons in experimental social science research. A more extensive methodological introduction that inspired the development of the 'voiceR' package is provided in Hildebrand et al. 2020 <doi:10.1016/j.jbusres.2020.09.020>.  
	"""
	
	cran = "voiceR" 

	version("0.1.0", md5="e8a250938acca664ee65c3aaa5f7128e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fsa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phia", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-soundgen", type=("build", "run"))
	depends_on("r-rcompanion", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
