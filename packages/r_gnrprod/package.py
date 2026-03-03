# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnrprod(RPackage):
	"""Estimates Gross Output Functions

	Estimation of gross output production functions and productivity in the presence of numerous fixed (nonflexible) and a single flexible input using the nonparametric identification strategy specified in Gandhi, Navarro, and Rivers (2020) <doi:10.1086/707736>. Monte Carlo evidence from the paper demonstrates high performance in estimating production function elasticities.
	"""
	
	cran = "gnrprod" 

	version("1.1.2", md5="1d565091b5b8ac4718d65364b3b17e3f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
