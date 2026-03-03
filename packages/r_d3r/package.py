# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3r(RPackage):
	"""'d3.js' Utilities for R

	Provides a suite of functions to help ease the use of 'd3.js' in R.
              These helpers include 'htmltools::htmlDependency' functions, hierarchy
              builders, and conversion tools for 'partykit', 'igraph,' 'table',
              and 'data.frame' R objects into the 'JSON' that 'd3.js' expects.
	"""
	
	homepage = "https://github.com/timelyportfolio/d3r"
	cran = "d3r" 

	version("1.1.0", md5="0a6676743c509c88a3653bd91f2591d6")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
