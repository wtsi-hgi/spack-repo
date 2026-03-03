# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinydrive(RPackage):
	"""File Sharing Shiny Module

	Shiny module for easily sharing files between users. Admin can add, remove, edit and download file.
    User can only download file. It's also possible to manage files using R functions directly.
	"""
	
	cran = "shinydrive" 

	version("0.1.3", md5="d3d864f34ea93a1c78aec4e0902431ff")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
