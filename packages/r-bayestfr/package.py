# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestfr(RPackage):
	"""Bayesian Fertility Projection

	Making probabilistic projections of total fertility rate for all countries of the world, using a Bayesian hierarchical model <doi:10.1007/s13524-011-0040-5> <doi:10.18637/jss.v106.i08>. Subnational probabilistic projections are also supported <doi:10.4054/DemRes.2018.38.60>.
	"""
	
	homepage = "https://bayespop.csss.washington.edu"
	cran = "bayesTFR" 

	version("7.4-2", md5="ea034de8c1526edab55999d45440dc6c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-wpp2019", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
