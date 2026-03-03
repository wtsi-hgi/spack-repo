# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddinslist(RPackage):
	"""Discover and Install Useful RStudio Addins

	Browse through a continuously updated list of existing RStudio 
    addins and install/uninstall their corresponding packages.
	"""
	
	homepage = "https://github.com/daattali/addinslist"
	cran = "addinslist" 

	version("0.5.0", md5="94562edd71aae066e6c8748e4b7b701d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-dt@0.1:", type=("build", "run"))
	depends_on("r-miniui@0.1:", type=("build", "run"))
	depends_on("r-shiny@0.13.2:", type=("build", "run"))
	depends_on("r-shinyjs@0.6:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.1:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rvest@0.3.1:", type=("build", "run"))
	depends_on("r-xml2@0.1.2:", type=("build", "run"))
