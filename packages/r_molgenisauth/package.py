# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMolgenisauth(RPackage):
	"""'OpenID Connect' Discovery and Authentication

	Discover 'OpenID Connect' endpoints and authenticate
    using device flow. Used by 'MOLGENIS' packages.
	"""
	
	homepage = "https://github.com/molgenis/molgenis-r-auth/"
	cran = "MolgenisAuth" 

	version("0.0.25", md5="6ad9c30cb1d570e40bea3bdbf8e4844b")

	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-urltools@1.7:", type=("build", "run"))
