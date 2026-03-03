# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWppexplorer(RPackage):
	"""Explorer of World Population Prospects

	Explore data in the 'wpp2019' (or 2017, 2015, ...) package using a 'shiny' interface.
	"""
	
	cran = "wppExplorer" 

	version("2.3-4", md5="b2c972c794e512a4f2881bc7198905dc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-wpp2019", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
