# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrapo(RPackage):
	"""Financial Risk Modelling and Portfolio Optimisation with R

	Accompanying package of the book 'Financial Risk Modelling
        and Portfolio Optimisation with R', second edition. The data sets used in the book are contained in this package.
	"""
	
	cran = "FRAPO" 

	version("0.4-1", md5="29399b8490aba662699c6e17335adbb7")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-cccp", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
