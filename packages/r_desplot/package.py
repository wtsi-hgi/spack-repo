# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesplot(RPackage):
	"""Plotting Field Plans for Agricultural Experiments

	A function for plotting maps of agricultural field experiments that are laid out in grids.  See Ryder (1981) <doi:10.1017/S0014479700011601>.
	"""
	
	homepage = "https://kwstat.github.io/desplot/"
	cran = "desplot" 

	version("1.10", md5="c873da7e906894d3671f1b1b02e9b60c")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
