# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcp2(RPackage):
	"""Approximate Bayesian Computational Model for Estimating P2

	Tests the goodness of fit of a distribution of offspring to the Normal, Poisson, and Gamma distribution and estimates the proportional paternity of the second male (P2) based on the best fit distribution.
	"""
	
	cran = "ABCp2" 

	version("1.2", md5="e920282d5a369df71e15241be40cb60e", url="https://cran.r-project.org/src/contrib/ABCp2_1.2.tar.gz")

	depends_on("r-mass", type=("build", "run"))
