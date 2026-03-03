# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrm(RPackage):
	"""Provides R-Language Code to Examine Quantitative Risk Management
Concepts

	Provides functions/methods to accompany the book
 Quantitative Risk Management: Concepts, Techniques and Tools by
 Alexander J. McNeil, Ruediger Frey, and Paul Embrechts.
	"""
	
	cran = "QRM" 

	version("0.4-31", md5="54e56731f6a262b153030521fd6f3fbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
