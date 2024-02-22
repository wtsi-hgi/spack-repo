# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcputility(RPackage):
	"""Wrapper for SQL Server bcp Utility

	Provides functions to utilize a command line utility that does bulk inserts and exports from SQL Server databases. 
	"""
	
	homepage = "https://bcputility.roh.engineering"
	cran = "bcputility" 

	version("0.4.0", md5="99829c3c9a5a83fcc15cd45346c96b16")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
