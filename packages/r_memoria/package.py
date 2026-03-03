# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemoria(RPackage):
	"""Quantifying Ecological Memory in Palaeoecological Datasets and
Other Long Time-Series

	Tools to quantify ecological memory in long time-series with Random Forest models (Breiman 2001 <doi:10.1023/A:1010933404324>) fitted with the 'ranger' library (Wright and Ziegler 2017 <doi:10.18637/jss.v077.i01>). Particularly oriented to palaeoecological datasets and simulated pollen curves produced by the 'virtualPollen' package, but also applicable to other long time-series involving a set of environmental drivers and a biotic response.
	"""
	
	cran = "memoria" 

	version("1.0.0", md5="a08d97f730ac9b6ecdd4dfb4296404ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hh", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
