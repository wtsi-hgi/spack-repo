# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeatstats(RPackage):
	"""Neat and Painless Statistical Reporting

	User-friendly, clear and simple statistics, primarily for
  publication in psychological science. The main functions are wrappers for
  other packages, but there are various additions as well. Every relevant step
  from data aggregation to reportable printed statistics is covered for basic
  experimental designs.
	"""
	
	homepage = "https://github.com/gasparl/neatstats"
	cran = "neatStats" 

	version("1.13.3", md5="561fe171a3d3adeb7f8134540b22ff85")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ez", type=("build", "run"))
	depends_on("r-exact", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
