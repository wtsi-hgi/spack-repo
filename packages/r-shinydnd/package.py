# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinydnd(RPackage):
	"""Shiny Drag-n-Drop

	Add functionality to create drag and drop div elements in shiny.
	"""
	
	homepage = "https://github.com/ayayron/shinydnd"
	cran = "shinyDND" 

	version("0.1.0", md5="35a8964c985518a749d3eae7388cb3a3")

	depends_on("r-shiny@0.11:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
