# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaculr(RPackage):
	"""Analyze Metaculus Predictions and Questions

	Login, download, and analyze questions predicted by you and/or the 
    Metaculus community by interacting with the Metaculus API, currently
    located at <https://www.metaculus.com/api2/>.
	"""
	
	homepage = "https://ntrlshrp.gitlab.io/metaculr"
	cran = "MetaculR" 

	version("0.4.1", md5="f31647a9f41f406011171fddfcac3b42")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-verification", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
