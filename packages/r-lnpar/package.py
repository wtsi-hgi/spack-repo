# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLnpar(RPackage):
	"""Estimation and Testing for a Lognormal-Pareto Mixture

	Estimates a lognormal-Pareto mixture by maximizing the profile likelihood function. A likelihood ratio test for discriminating between lognormal and Pareto tail is also implemented. See Bee, M. (2022) <doi:10.1007/s11634-022-00497-4>.
	"""
	
	cran = "LNPar" 

	version("0.1.0", md5="7085ca08f1f0b8dbd85008e761140523")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
