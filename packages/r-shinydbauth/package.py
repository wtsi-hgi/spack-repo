# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinydbauth(RPackage):
	"""Simple Authentification for 'shiny' Applications

	Provides a simple authentification mechanism for single 'shiny' applications.
    Authentification and password change functionality are performed calling user provided functions that typically access some database backend.
    Source code of main applications is protected until authentication is successful.
	"""
	
	homepage = "https://github.com/diegoefe/shinydbauth"
	cran = "shinydbauth" 

	version("1.0.0.1", md5="1002c5ae513d1691584326aff87e2fbb")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-dt@0.5:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-billboarder", type=("build", "run"))
	depends_on("r-scrypt", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
