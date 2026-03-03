# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvfiller(RPackage):
	"""Fill Data Points

	Provides numerous functions to fill data.
    These can be applied either to missing or skewed data.
    The functions are designed within the scope of Student Analytics. 
	"""
	
	homepage = "https://github.com/vusaverse/vvfiller"
	cran = "vvfiller" 

	version("0.6.7", md5="5d8cf5cdd0ddc60327c8dcdb1c5e6765")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
