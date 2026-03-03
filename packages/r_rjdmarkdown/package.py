# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjdmarkdown(RPackage):
	"""'rmarkdown' Extension for Formatted 'RJDemetra' Outputs

	Functions to have nice 'rmarkdown' outputs of the 
  seasonal and trading day adjustment models made with 'RJDemetra'.
	"""
	
	homepage = "https://github.com/AQLT/rjdmarkdown"
	cran = "rjdmarkdown" 

	version("0.2.2", md5="a7fe8c13834a3aefebe9e5a33151b9e4")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rjdemetra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
