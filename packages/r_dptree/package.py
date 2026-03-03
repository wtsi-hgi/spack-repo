# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDptree(RPackage):
	"""Dirichlet-Based Polya Tree

	Contains functions to perform copula estimation 
	by the non-parametric Bayesian method, 
	Dirichlet-based Polya Tree. See Ning (2018) <doi:10.1080/00949655.2017.1421194>.
	"""
	
	cran = "DPtree" 

	version("1.0.1", md5="1f08477c998dec743b17659325476977")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
