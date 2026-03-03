# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchemr(RPackage):
	"""Convert Images to Usable Color Schemes

	A fast and adaptable tool to convert photos and images into usable colour schemes for data visualisation. Contains functionality to extract colour palettes from images, as well for the conversion of images between colour spaces.
	"""
	
	cran = "schemr" 

	version("0.2.0", md5="ca2fac5b21acbe02d93823a3509b5dcd")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-openimager", type=("build", "run"))
