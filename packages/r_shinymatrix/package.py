# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymatrix(RPackage):
	"""Shiny Matrix Input Field

	Implements a custom matrix input field. 
	"""
	
	cran = "shinyMatrix" 

	version("0.6.0", md5="6797ddf5188ed081ce86678254cf4b01")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
