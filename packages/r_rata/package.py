# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRata(RPackage):
	"""Automated Test Assembly

	Automated test assembly of linear and adaptive tests using the 
    mixed-integer programming. The full documentation and tutorials are at 
    <https://github.com/xluo11/Rata>.
	"""
	
	homepage = "https://github.com/xluo11/Rata"
	cran = "Rata" 

	version("0.0.2", md5="0065898c9e7760eda23e0838ca2ea6fc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glpkapi", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-rirt", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
