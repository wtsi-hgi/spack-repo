# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtertools(RPackage):
	"""Tools Developed by the Long Term Ecological Research Community

	Set of the data science tools created by various members of the Long Term 
    Ecological Research (LTER) community. These functions were initially written largely 
    as standalone operations and have later been aggregated into this package.
	"""
	
	homepage = "https://lter.github.io/ltertools/"
	cran = "ltertools" 

	version("1.0.0", md5="9f54f537465766dc4aac6eb6f45af8f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
