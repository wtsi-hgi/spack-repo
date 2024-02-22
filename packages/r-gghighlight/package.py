# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghighlight(RPackage):
	"""Highlight Lines and Points in 'ggplot2'

	Make it easier to explore data with highlights.
	"""
	
	homepage = "https://yutannihilation.github.io/gghighlight/"
	cran = "gghighlight" 

	version("0.4.1", md5="d75daa671fae8f9684f71f60aa837b40")

	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
