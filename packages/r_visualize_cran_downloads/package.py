# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisualizeCranDownloads(RPackage):
	"""Visualize Downloads from 'CRAN' Packages

	Visualize the trends and historical downloads from packages in the 'CRAN' repository. Data is obtained by using the 'API' to query the database from the 'RStudio' 'CRAN' mirror.
	"""
	
	homepage = "https://github.com/mponce0/Visualize.CRAN.Downloads"
	cran = "Visualize.CRAN.Downloads" 

	version("1.0.3", md5="f049d0ca43480520a56c65b67b37dd2e")

	depends_on("r-cranlogs", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
