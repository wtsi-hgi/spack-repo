# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsconctdply(RPackage):
	"""Deploys Multiple 'Shiny' Apps using Configuration File

	Provides a tool for mass deployment of shiny apps to 'RStudio Connect' or 'Shiny Server'. Multiple user accounts and servers can be configured for deployment.
	"""
	
	cran = "Rsconctdply" 

	version("0.1.3", md5="b6dbb1ef4b347c33eba917ed6cdbc3cb")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rsconnect", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
