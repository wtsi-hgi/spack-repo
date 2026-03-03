# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSasr(RPackage):
	"""'SAS' Interface

	Provides a 'SAS' interface, through 'SASPy'(<https://sassoftware.github.io/saspy/>) and 'reticulate'(<https://rstudio.github.io/reticulate/>).
  This package helps you create 'SAS' sessions, execute 'SAS' code in remote 'SAS' servers, retrieve execution results and log, and exchange datasets between 'SAS' and 'R'.
  It also helps you to install 'SASPy' and create a configuration file for the connection. Please review the 'SASPy' license file as instructed so that you comply with its separate and independent license.
	"""
	
	homepage = "https://github.com/insightsengineering/sasr/"
	cran = "sasr" 

	version("0.1.2", md5="3e611d032a69754586c172a2ce4e4b8f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
