# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtip(RPackage):
	"""Inequality, Welfare and Poverty Indices and Curves using the
EU-SILC Data

	R tools to measure and compare inequality, welfare and poverty using the EU statistics on income and living conditions surveys.
	"""
	
	cran = "rtip" 

	version("1.1.1", md5="a62d37e20c05476c346d05d151fa8671")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-boot@1.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-rootsolve@1.7:", type=("build", "run"))
