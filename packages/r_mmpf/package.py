# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmpf(RPackage):
	"""Monte-Carlo Methods for Prediction Functions

	Marginalizes prediction functions using Monte-Carlo integration and computes permutation importance.
	"""
	
	cran = "mmpf" 

	version("0.0.5", md5="e3db54089496b0537601c5b9d2e37f68")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
