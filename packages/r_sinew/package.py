# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinew(RPackage):
	"""Package Development Documentation and Namespace Management

	Manage package documentation and namespaces from the command line. 
             Programmatically attach namespaces in R and Rmd script, populates 
             'Roxygen2' skeletons with information scraped from within functions and 
             populate the Imports field of the DESCRIPTION file.
	"""
	
	homepage = "https://github.com/yonicd/sinew"
	cran = "sinew" 

	version("0.4.0", md5="bf607228845853b02c39c0e593b1c632")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-sos", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
