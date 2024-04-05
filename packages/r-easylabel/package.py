# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasylabel(RPackage):
	"""Interactive Scatter Plot and Volcano Plot Labels

	Interactive labelling of scatter plots, volcano plots and 
    Manhattan plots using a 'shiny' and 'plotly' interface. Users can hover 
    over points to see where specific points are located and click points 
    on/off to easily label them. Labels can be dragged around the plot to place 
    them optimally. Plots can be exported directly to PDF for publication.
	"""
	
	cran = "easylabel" 

	version("0.2.8", md5="3241af5b15e43abf9bb1d3c9f5cf3561")
	version("0.2.7", md5="0ea6d53ee109a09dc976f54a6a4700e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
