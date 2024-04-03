# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeumilkr(RPackage):
	"""Heuristic Capacitated Vehicle Routing Problem Solver

	Implements the Clarke-Wright algorithm to find a quasi-optimal solution to the Capacitated Vehicle Routing Problem. See Clarke, G. and Wright, J.R. (1964) <doi:10.1287/opre.12.4.568> for details. The implementation is accompanied by helper functions to inspect its solution.
	"""
	
	homepage = "https://github.com/lschneiderbauer/heumilkr"
	cran = "heumilkr" 

	version("0.2.0", md5="f7e02288056794db8990ba51092cf265")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-xml2@1.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
