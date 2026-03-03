# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmRank(RPackage):
	"""Fit, Simulate and Diagnose Exponential-Family Models for
Rank-Order Relational Data

	A set of extensions for the 'ergm' package to fit weighted networks whose edge weights are ranks. See Krivitsky and Butts (2017) <doi:10.1177/0081175017692623> and Krivitsky, Hunter, Morris, and Klumb (2021) <arXiv:2106.04997>.
	"""
	
	homepage = "https://statnet.org"
	cran = "ergm.rank" 

	version("4.1.0", md5="ea685fbae5617b0b1c3a9b9129125706")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-statnet-common@4.2:", type=("build", "run"))
