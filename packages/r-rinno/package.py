# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRinno(RPackage):
	"""An Installation Framework for Shiny Apps

	Installs shiny apps packaged as stand-alone Electron apps using Inno Setup, an open source software that builds installers for Windows programs <http://www.jrsoftware.org/ishelp/>.
	"""
	
	homepage = "www.ficonsulting.com"
	cran = "RInno" 

	version("1.0.1", md5="fbc5daee82ba9a2042bb864671dd8f14")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue@1.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-installr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
