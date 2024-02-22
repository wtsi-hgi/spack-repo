# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyReglog(RPackage):
	"""Optional Login and Registration Module System for ShinyApps

	RegLog system provides a set of shiny modules to handle register
   procedure for your users, alongside with login, edit credentials and
   password reset functionality. 
   It provides support for popular SQL databases
   and optionally googlesheet-based database for easy setup. For email sending
   it provides support for 'emayili' and 'gmailr' backends. Architecture makes 
   customizing usability pretty straightforward.
   The authentication system created 
   with shiny.reglog is designed to be optional: user don't need to be logged-in 
   to access your application, but when logged-in the user data can be used 
   to read from and write to relational databases.
	"""
	
	homepage = "https://statismike.github.io/shiny.reglog/"
	cran = "shiny.reglog" 

	version("0.5.2", md5="8ba0883bde4f17b86c162ec90c2ed5ba")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-scrypt", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
