# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivatr(RPackage):
	"""Utilities for Parsing and Plotting Activities

	This contains helpful functions for parsing, managing, plotting, and
    visualizing activities, most often from GPX (GPS Exchange Format) files
    recorded by GPS devices. It allows easy parsing of the source files into
    standard R data formats, along with functions to compute derived data for
    the activity, and to plot the activity in a variety of ways.
	"""
	
	homepage = "https://github.com/dschafer/activatr"
	cran = "activatr" 

	version("0.2.0", md5="93a43957feabd52d892fb4ba998278a4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-geosphere@1.5:", type=("build", "run"))
	depends_on("r-ggmap@3:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-slider@0.3:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
