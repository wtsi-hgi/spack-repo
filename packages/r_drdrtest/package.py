# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrdrtest(RPackage):
	"""A Nonparametric Doubly Robust Test for Continuous Treatment
Effect

	Implement the statistical test proposed in Weng et al. (2021) to test whether
    the average treatment effect curve is constant and whether a discrete covariate is a significant effect modifier.
	"""
	
	cran = "DRDRtest" 

	version("0.1", md5="46446f0c57480ece03afe53558839267")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
