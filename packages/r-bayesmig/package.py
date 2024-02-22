# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmig(RPackage):
	"""Bayesian Projection of Migration

	Producing probabilistic projections of net migration rate for all countries of the world
    or for subnational units using a Bayesian hierarchical model by Azose an Raftery (2015) <doi:10.1007/s13524-015-0415-0>.
	"""
	
	homepage = "http://bayespop.csss.washington.edu"
	cran = "bayesMig" 

	version("0.4-6", md5="2e3a90967f773f0045a30157961a05b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bayestfr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-wpp2019", type=("build", "run"))
