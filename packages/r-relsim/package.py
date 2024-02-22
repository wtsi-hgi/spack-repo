# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelsim(RPackage):
	"""Relative Simulator

	A set of tools to explore the behaviour statistics used for forensic DNA interpretation when close relatives are involved. The package also offers some useful tools for exploring other forensic DNA situations.
	"""
	
	cran = "relSim" 

	version("1.0.0", md5="1c8eacf7972fbddc2930dd2d2163df81")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-multicool", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
