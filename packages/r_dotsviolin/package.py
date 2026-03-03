# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDotsviolin(RPackage):
	"""Dot Plots Mimicking Violin Plots

	Modifies dot plots to have different sizes of dots mimicking violin plots and identifies
  modes or peaks for them based on frequency and kernel density estimates 
  (Rosenblatt, 1956) <doi:10.1214/aoms/1177728190> (Parzen, 1962) <doi:10.1214/aoms/1177704472>.
	"""
	
	cran = "dotsViolin" 

	version("0.0.1", md5="b7154d69d9c4c678d7898995f85900ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
