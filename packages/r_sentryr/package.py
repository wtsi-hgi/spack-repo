# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSentryr(RPackage):
	"""Send Errors and Messages to Sentry

	Unofficial client for 'Sentry' <https://sentry.io>,
  a self-hosted or cloud-based error-monitoring service. It will inform about
  errors in real-time, and includes integration with the 'Plumber' package.
	"""
	
	homepage = "https://github.com/jcpsantiago/sentryR"
	cran = "sentryR" 

	version("1.1.2", md5="9572d7643ecd4447fb96793197e11284")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
