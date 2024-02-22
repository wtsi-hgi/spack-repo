# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvstat(RPackage):
	"""Configurable Reporting on your External Compute Environment

	Runs a series of configurable tests against a user's compute 
  environment. This can be used for checking that things like a specific 
  directory or an environment variable is available before you start an analysis.
  Alternatively, you can use the package's situation report when filing error
  reports with your compute infrastructure.
	"""
	
	homepage = "https://envstat.sellorm.com"
	cran = "envstat" 

	version("0.0.3", md5="3583c41afd31275fb363b9be82249f07")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
