# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhoami(RPackage):
	"""Username, Full Name, Email Address, 'GitHub' Username of the
Current User

	Look up the username and full name of the current user,
    the current user's email address and 'GitHub' username,
    using various sources of system and configuration information.
	"""
	
	homepage = "https://github.com/r-lib/whoami#readme"
	cran = "whoami" 

	version("1.3.0", md5="b7514ed03127ef65876cd439f66767bb")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
