# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeslife(RPackage):
	"""Bayesian Projection of Life Expectancy

	Making probabilistic projections of life expectancy for all countries of the world, using a Bayesian hierarchical model <doi:10.1007/s13524-012-0193-x>. Subnational projections are also supported.
	"""
	
	homepage = "https://bayespop.csss.washington.edu"
	cran = "bayesLife" 

	version("5.2-0", md5="c388e24c9cb3a340471d4b72ab01b233")

	depends_on("r-bayestfr@7.3.0:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wpp2019", type=("build", "run"))
	depends_on("r-hett", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
