# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzcox(RPackage):
	"""Easily Process a Batch of Cox Models

	A tool to operate a batch of univariate or multivariate Cox
    models and return tidy result.
	"""
	
	homepage = "https://github.com/ShixiangWang/ezcox"
	cran = "ezcox" 

	version("1.0.4", md5="66453cb6fbaeaadf9b087b2b189a54b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-forestmodel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
