# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnections(RPackage):
	"""Integrates with the 'RStudio' Connections Pane and 'pins'

	Enables 'DBI' compliant packages to integrate with the 'RStudio' connections 
  pane, and the 'pins' package. It automates the display of schemata, tables, views, as well 
  as the preview of the table's top 1000 records. 
	"""
	
	homepage = "https://github.com/rstudio/connections"
	cran = "connections" 

	version("0.2.0", md5="a939222606deff976d32913987ebb335")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-pins", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-rscontract", type=("build", "run"))
