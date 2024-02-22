# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoewesadditivity(RPackage):
	"""Loewe's Additivity

	Estimate model parameters to determine whether two compounds have synergy, antagonism, or Loewe's Additivity.
	"""
	
	cran = "loewesadditivity" 

	version("0.1.0", md5="cd6834561ab27e0c56e3780de295b12e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
