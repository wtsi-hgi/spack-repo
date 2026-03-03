# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesconnect(RPackage):
	"""Provides User Tokens for Access to ICES Web Services

	Provides user tokens for ICES web services that require
  authentication and authorization.  Web services covered by this
  package are ICES VMS database, the ICES DATSU web services, and the
  ICES SharePoint site.
	"""
	
	cran = "icesConnect" 

	version("1.0.0", md5="0cff5da4e3011d3f1e1615aafa0f23d2")

	depends_on("r-whoami", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
