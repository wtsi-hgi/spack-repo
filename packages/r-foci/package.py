# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoci(RPackage):
	"""Feature Ordering by Conditional Independence

	Feature Ordering by Conditional Independence (FOCI) is a variable selection algorithm based on the measure of conditional dependence.
    For more information, see the paper: Azadkia and Chatterjee (2019),"A simple measure of conditional dependence" <arXiv:1910.12327>.
	"""
	
	cran = "FOCI" 

	version("0.1.3", md5="e37dc7be246a6a5e43fe3d8c350a5ee8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
