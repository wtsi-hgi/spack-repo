# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlpestimator(RPackage):
	"""Performs a BLP Demand Estimation

	Provides the estimation algorithm to perform the demand estimation described in Berry, Levinsohn and Pakes (1995) <DOI:10.2307/2171802> . The routine uses analytic gradients and offers a large number of implemented integration methods and optimization routines.
	"""
	
	cran = "BLPestimatoR" 

	version("0.3.4", md5="87c616d8b33de9dac98f41dac6994bd2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvquad", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
