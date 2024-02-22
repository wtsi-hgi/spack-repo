# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPencopulacond(RPackage):
	"""Estimating Non-Simplified Vine Copulas Using Penalized Splines

	Estimating Non-Simplified Vine Copulas Using Penalized Splines.
	"""
	
	cran = "pencopulaCond" 

	version("0.2", md5="47f60806d096f99797bc42853f9a39a9")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-pacotest", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
