# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCognitor(RPackage):
	"""Authentication for 'Shiny' Apps with 'Amazon Cognito'

	Provides authentication for Shiny applications using 'Amazon Cognito' ( <https://aws.amazon.com/es/cognito/>).
	"""
	
	cran = "cognitoR" 

	version("1.0.5", md5="d3c27ed696ff6d8286d6cdbecafc5b7e")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-paws", type=("build", "run"))
