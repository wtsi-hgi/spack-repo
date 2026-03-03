# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyInfo(RPackage):
	"""'shiny' Info

	Displays simple diagnostic information of the 'shiny' project in the user interface of the app.
	"""
	
	cran = "shiny.info" 

	version("0.2.0", md5="cbd56802ea381748e1d6f82f95f1cff0")

	depends_on("r-git2r@0.22.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
