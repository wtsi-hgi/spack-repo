# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWig(RPackage):
	"""Import WIG Data into R in Long Format

	Import WIG data into R in long format.
	"""
	
	homepage = "https://github.com/ramiromagno/wig"
	cran = "wig" 

	version("0.1.0", md5="fadd0cb53695c758ca147bbf147bed07")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
