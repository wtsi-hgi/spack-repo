# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2pptx(RPackage):
	"""Object Oriented R -> PowerPoint

	Provides a friendly, object oriented API for creating PowerPoint
    slide decks in R.
	"""
	
	homepage = "https://mattle24.github.io/r2pptx/"
	cran = "r2pptx" 

	version("0.1.0", md5="ea1117debb363a083743b679135364a3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
