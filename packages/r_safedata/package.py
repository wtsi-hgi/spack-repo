# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafedata(RPackage):
	"""Interface to Data from the SAFE Project

	The SAFE Project (<https://www.safeproject.net/>) is a large 
	scale ecological experiment in Malaysian Borneo that explores the impact 
	of habitat fragmentation and conversion on ecosystem function and services. 
	Data collected at the SAFE Project is made available under a common format 
	through the Zenodo data repository and this package makes it easy to 
	discover and load that data into R.
	"""
	
	homepage = "https://imperialcollegelondon.github.io/safedata/index.html"
	cran = "safedata" 

	version("1.1.3", md5="e782afe7c636f87c5472941d9e62a98e")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
