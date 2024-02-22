# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddinsjoaomelo(RPackage):
	"""Addins Made of Joao Melo

	Provide addins for 'RStudio'.
  It currently contains 3 addins. The first to add a shortcut for the double pipe. The second is to add a shortcut for the same operator. And the third to simplify the creation of vectors from texts pasted from the computer transfer area.
	"""
	
	cran = "addinsJoaoMelo" 

	version("0.1.0", md5="e4923f60fb78ecd3e4f8a3540f492b08")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
