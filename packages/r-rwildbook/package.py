# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwildbook(RPackage):
	"""Interface for the 'Wildbook' Wildlife Data Management Framework

	Provides an interface with the 'Wildbook' mark-recapture ecological database framework. It 
    helps users to pull data from the 'Wildbook' framework and format data for further analysis
    with mark-recapture applications like 'Program MARK' (which can be accessed via the 'RMark' package in 'R').
    Further information on the 'Wildbook' framework is available at: <http://www.wildbook.org/doku.php>. 
	"""
	
	cran = "RWildbook" 

	version("0.9.3", md5="dd49a6f4985584096237181e2c437ea7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-marked", type=("build", "run"))
