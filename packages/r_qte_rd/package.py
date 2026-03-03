# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQteRd(RPackage):
	"""Quantile Treatment Effects under the Regression Discontinuity
Design

	Provides comprehensive methods for testing, estimating, and conducting uniform inference on quantile treatment effects (QTEs) in sharp regression discontinuity (RD) designs, incorporating covariates and implementing robust bias correction methods of Qu, Yoon, Perron (2024) <doi:10.1162/rest_a_01168>.
	"""
	
	cran = "QTE.RD" 

	version("1.0.0", md5="72b69423352619f66b5ae5096d725c2f")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
