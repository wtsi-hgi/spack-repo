# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBumbl(RPackage):
	"""Tools for Modeling Bumblebee Colony Growth and Decline

	Bumblebee colonies grow during worker production, then decline after switching to production of reproductive individuals (drones and gynes).  This package provides tools for modeling and visualizing this pattern by identifying a switchpoint with a growth rate before and a decline rate after the switchpoint. The mathematical models fit by bumbl are described in Crone and Williams (2016) <doi:10.1111/ele.12581>.
	"""
	
	homepage = "https://github.com/Aariq/bumbl"
	cran = "bumbl" 

	version("1.0.3", md5="ea472f543e0991eb676d2071b24727a8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
