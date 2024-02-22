# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffer(RPackage):
	"""Metrics of Difference for Comparing Pairs of Maps or Pairs of
Variables

	Metrics of difference for comparing pairs of variables or pairs of maps representing real or categorical variables at original and multiple resolutions.
	"""
	
	homepage = "https://github.com/amsantac/diffeR"
	cran = "diffeR" 

	version("0.0-8", md5="88b8334cfae73eea64a342c833a3e94a")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
