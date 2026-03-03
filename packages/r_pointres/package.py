# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPointres(RPackage):
	"""Analyzing Pointer Years and Components of Resilience

	Functions to calculate and plot event and pointer years as well as resilience indices. Designed for dendroecological applications, but also suitable to analyze patterns in other ecological time series.
	"""
	
	cran = "pointRes" 

	version("2.0.2", md5="025701f09957899915e1f8a98774da65")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tripler", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
