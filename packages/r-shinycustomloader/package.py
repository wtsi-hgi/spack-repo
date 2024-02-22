# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinycustomloader(RPackage):
	"""Custom Loader for Shiny Outputs

	A custom css/html or gif/image file for the loading screen in R 'shiny'. It also can use the marquee to have custom text loading screen. 
	"""
	
	cran = "shinycustomloader" 

	version("0.9.0", md5="fa9fd3390e3664f9b027c4ef2bb3682c")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
