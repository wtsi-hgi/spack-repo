# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghoriplot(RPackage):
	"""Horizon Plots for 'ggplot2'

	A user-friendly, highly customizable R package for building
    horizon plots in the 'ggplot2' environment.
	"""
	
	homepage = "https://rivasiker.github.io/ggHoriPlot/"
	cran = "ggHoriPlot" 

	version("1.0.1", md5="e0f0034cb4f5e7b25a5aedf2b2b7232d")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
