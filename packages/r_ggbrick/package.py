# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbrick(RPackage):
	"""Waffle Style Chart with a Brick Layout in 'ggplot2'

	A new take on the bar chart. Similar to a waffle style chart but
  instead of squares the layout resembles a brick wall.
	"""
	
	cran = "ggbrick" 

	version("0.3.0", md5="9da909aded1f43dac95ece86ae6bc56c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
