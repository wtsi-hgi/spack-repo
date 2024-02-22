# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtibble(RPackage):
	"""Create Tibbles and Lists of 'ggplot' Figures for Reporting

	
  Create tibbles and lists of 'ggplot' figures that can be modified as easily as
  regular 'ggplot' figures.  Typical use cases are for creating reports or web
  pages where many figures are needed with different data and similar
  formatting.
	"""
	
	homepage = "https://billdenney.github.io/ggtibble/"
	cran = "ggtibble" 

	version("1.0.0", md5="f5b10a71a3c4cc2b6059886d0aec14d2")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
