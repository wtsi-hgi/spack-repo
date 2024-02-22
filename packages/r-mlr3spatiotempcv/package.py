# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3spatiotempcv(RPackage):
	"""Spatiotemporal Resampling Methods for 'mlr3'

	Extends the mlr3 ML framework with spatio-temporal resampling
    methods to account for the presence of spatiotemporal autocorrelation
    (STAC) in predictor variables. STAC may cause highly biased
    performance estimates in cross-validation if ignored.
	"""
	
	homepage = "https://mlr3spatiotempcv.mlr-org.com/"
	cran = "mlr3spatiotempcv" 

	version("2.3.0", md5="15b877affc61fa23170161b57dfb8d81")

	depends_on("r-mlr3@0.12:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-mlr3misc@0.11:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
