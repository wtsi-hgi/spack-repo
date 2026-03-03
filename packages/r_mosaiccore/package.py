# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaiccore(RPackage):
	"""Common Utilities for Other MOSAIC-Family Packages

	Common utilities used in other MOSAIC-family packages are 
    collected here.
	"""
	
	homepage = "https://github.com/ProjectMOSAIC/mosaicCore"
	cran = "mosaicCore" 

	version("0.9.4.0", md5="942de1ff61d90fc522e8671b9c12f628")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
