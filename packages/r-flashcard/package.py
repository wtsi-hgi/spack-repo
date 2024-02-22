# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlashcard(RPackage):
	"""Create a Flash Card

	Create a flip over style Flash Card with desired data frame for Shiny application.
	"""
	
	cran = "flashCard" 

	version("0.1.0", md5="f1caea515cb89954756971dc12010c47")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
