# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIstats(RPackage):
	"""A Graphical Interface to Perform STOCSY Analyses on NMR Data

	Launches a 'shiny' based application for Nuclear Magnetic Resonance (NMR)data importation and Statistical TOtal Correlation SpectroscopY (STOCSY) analyses in a full interactive approach. The theoretical background and applications of STOCSY method could be found at Cloarec, O., Dumas, M. E., Craig, A., Barton, R. H., Trygg, J., Hudson, J., Blancher, C., Gauguier, D., Lindon, J. C., Holmes, E. & Nicholson, J. (2005) <doi:10.1021/ac048630x>.
	"""
	
	cran = "iSTATS" 

	version("1.7", md5="7260cd0dec62a1ded814d80729c1f92b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-shinywidgets@0.4.3:", type=("build", "run"))
	depends_on("r-cairo@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-shiny@1.0.2:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
