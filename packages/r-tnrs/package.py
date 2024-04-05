# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTnrs(RPackage):
	"""Taxonomic Name Resolution Service

	Provides access to the Taxonomic Name Resolution Service <https://github.com/ojalaquellueva/tnrsapi> through R.  The user supplies plant taxonomic names and the package returns resolved taxonomic names along with information on decisions.  Optionally, the package can also be used to parse taxonomic names. 
	"""
	
	cran = "TNRS" 

	version("0.3.5", md5="a76b8c9f4414f967412b50205964abc2")
	version("0.3.4", md5="717f07cf8e3b065a3c7052b69ca7e09c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
