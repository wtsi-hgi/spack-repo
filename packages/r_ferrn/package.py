# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFerrn(RPackage):
	"""Facilitate Exploration of touRR optimisatioN

	Diagnostic plots for optimisation, with a focus on projection pursuit. These show paths the optimiser 
    takes in the high-dimensional space in multiple ways: by reducing the dimension using principal component analysis, and
    also using the tour to show the path on the high-dimensional space. Several botanical colour palettes are included, reflecting the 
    name of the package. A paper describing the methodology can be found at <https://journal.r-project.org/archive/2021/RJ-2021-105/index.html>.
	"""
	
	homepage = "https://github.com/huizezhang-sherry/ferrn/"
	cran = "ferrn" 

	version("0.0.2", md5="75da71814e5c7c4379e75ec1a0a45db1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-geozoo", type=("build", "run"))
	depends_on("r-tourr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
