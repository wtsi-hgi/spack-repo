# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlsbandit(RPackage):
	"""Data Viewer for Bureau of Labor Statistics Data

	Allows users to easily visualize data from the BLS (United States of America Bureau of Labor Statistics) <https://www.bls.gov>. Currently unemployment data series U1-U6 are available. Not affiliated with the Bureau of Labor Statistics or United States Government.
	"""
	
	cran = "blsBandit" 

	version("0.1", md5="e8e89b0f610a9e9e576ba3092ced1c14")

	depends_on("r-dbi@1.1.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.4:", type=("build", "run"))
	depends_on("r-plotly@4.10.2:", type=("build", "run"))
	depends_on("r-rsqlite@2.2.16:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-zoo@1.8.12:", type=("build", "run"))
