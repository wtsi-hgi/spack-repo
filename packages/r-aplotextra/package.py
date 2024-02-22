# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAplotextra(RPackage):
	"""Creating Composite Plots using 'aplot'

	Many complex plots are actually composite plots, such as 'oncoplot', 'funkyheatmap', 'upsetplot', etc. We can produce subplots using 'ggplot2' and combine them to create composite plots using 'aplot'. In this way, it is easy to customize these complex plots, by adding, deleting or modifying subplots in the final plot. This package provides a set of utilities to help users to create subplots and complex plots.
	"""
	
	homepage = "https://github.com/YuLab-SMU/aplotExtra"
	cran = "aplotExtra" 

	version("0.0.2", md5="c2fc4015b1fa580e5a451ae7e43d1ab4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-aplot@0.1.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggfun@0.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggstar", type=("build", "run"))
	depends_on("r-yulab-utils@0.0.8:", type=("build", "run"))
