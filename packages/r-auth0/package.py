# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuth0(RPackage):
	"""Authentication in Shiny with Auth0

	Uses Auth0 API (see <https://auth0.com> for more 
    information) to use a simple authentication system. It provides 
    tools to log in and out a shiny application using social networks or a list
    of e-mails.
	"""
	
	homepage = "https://curso-r.github.io/auth0/"
	cran = "auth0" 

	version("0.2.3", md5="4ba82744293345773e180b9175f867f1", url="https://cran.r-project.org/src/contrib/auth0_0.2.3.tar.gz")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
