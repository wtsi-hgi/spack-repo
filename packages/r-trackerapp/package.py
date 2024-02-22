# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrackerapp(RPackage):
	"""Interface for the Analysis of Running, Cycling and Swimming Data
from GPS-Enabled Tracking Devices

	Provides an integrated user interface and workflow for
             the analysis of running, cycling and swimming data from GPS-enabled
             tracking devices through the 'trackeR' <https://CRAN.R-project.org/package=trackeR> R package.
	"""
	
	homepage = "https://github.com/trackerproject/trackeRapp"
	cran = "trackeRapp" 

	version("1.2", md5="2c2769312f131d283a534b82008bf766")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tracker@1.5:", type=("build", "run"))
	depends_on("r-colorspace@1.4.1:", type=("build", "run"))
	depends_on("r-zoo@1.8.7:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-mgcv@1.8.31:", type=("build", "run"))
	depends_on("r-plotly@4.9.2:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))
	depends_on("r-changepoint@2.2.2:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7.1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.1:", type=("build", "run"))
	depends_on("r-sf@0.9.2:", type=("build", "run"))
	depends_on("r-mapdeck@0.3.2:", type=("build", "run"))
	depends_on("r-v8@3.0.2:", type=("build", "run"))
