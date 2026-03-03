# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsmextract(RPackage):
	"""Download and Import Open Street Map Data Extracts

	Match, download, convert and import Open Street Map data extracts 
    obtained from several providers. 
	"""
	
	homepage = "https://docs.ropensci.org/osmextract/"
	cran = "osmextract" 

	version("0.5.0", md5="043107a5ed0116a25889390b8313a11a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@0.8.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
