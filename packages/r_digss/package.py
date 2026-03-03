# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigss(RPackage):
	"""Determination of Intervals Using Georeferenced Survey Simulation

	Simulation tool to estimate the rate of success that surveys possessing user-specific characteristics have in identifying archaeological sites (or any groups of clouds of objects), given specific parameters of survey area, survey methods, and site properties. The survey approach used is largely based on the work of Kintigh (1988) <doi:10.2307/281113>.
	"""
	
	homepage = "https://github.com/markhubbe/DIGSS"
	cran = "DIGSS" 

	version("1.0.2", md5="bb8d5557d0854194a35782a5fd2a48a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
