# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymanager(RPackage):
	"""Authentication Management for 'Shiny' Applications

	Simple and secure authentification mechanism for single 'Shiny' applications.
    Credentials are stored in an encrypted 'SQLite' database. Source code of main application
    is protected until authentication is successful.
	"""
	
	homepage = "https://github.com/datastorm-open/shinymanager"
	cran = "shinymanager" 

	version("1.0.410", md5="d5c4711312e295b09dcdd35cdac7ba88")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-dt@0.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-billboarder", type=("build", "run"))
	depends_on("r-scrypt", type=("build", "run"))
