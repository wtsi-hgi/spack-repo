# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObl(RPackage):
	"""Optimum Block Length

	Obtain optimum block from Non-overlapping Block Bootstrap method.
	"""
	
	cran = "OBL" 

	version("0.2.1", md5="f84330fe69aa40141708c87dc43bf97f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
