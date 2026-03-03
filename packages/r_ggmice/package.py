# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmice(RPackage):
	"""Visualizations for 'mice' with 'ggplot2'

	Enhance a 'mice' imputation workflow with visualizations for
    incomplete and/or imputed data. The plotting functions produce
    'ggplot' objects which may be easily manipulated or extended. Use
    'ggmice' to inspect missing data, develop imputation models, evaluate
    algorithmic convergence, or compare observed versus imputed data.
	"""
	
	homepage = "https://github.com/amices/ggmice"
	cran = "ggmice" 

	version("0.1.0", md5="6cf16d039dbca1f9ff9be97788f75948")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
