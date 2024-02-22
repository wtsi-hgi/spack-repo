# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYuimagui(RPackage):
	"""A Graphical User Interface for the 'yuima' Package

	Provides a graphical user interface for the 'yuima' package.
	"""
	
	homepage = "https://yuimaproject.com"
	cran = "yuimaGUI" 

	version("1.3.1", md5="79d7e0551db1c6a3e1985135181314e8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-yuima", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-sde", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ghyp", type=("build", "run"))
