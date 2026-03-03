# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowgate(RPackage):
	"""Interactive Cytometry Gating in R

	flowGate adds an interactive Shiny app to allow manual GUI-based gating of flow cytometry data in R. Using flowGate, you can draw 1D and 2D span/rectangle gates, quadrant gates, and polygon gates on flow cytometry data by interactively drawing the gates on a plot of your data, rather than by specifying gate coordinates. This package is especially geared toward wet-lab cytometerists looking to take advantage of R for cytometry analysis, without necessarily having a lot of R experience.
	"""
	
	bioc = "flowGate" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowGate_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowGate/flowGate_1.2.0.tar.gz"]

	version("1.2.0", md5="d5b19dee6139d26306d14563f445a64f")

	depends_on("r-flowworkspace@4.0.6:", type=("build", "run"))
	depends_on("r-ggcyto@1.16:", type=("build", "run"))
	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-biocmanager@1.30.10:", type=("build", "run"))
	depends_on("r-flowcore@2.0.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
