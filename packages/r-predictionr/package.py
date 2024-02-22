# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictionr(RPackage):
	"""Prediction for Future Data from any Continuous Distribution

	Functions to get prediction intervals and prediction points of future observations from any continuous distribution.
	"""
	
	cran = "PredictionR" 

	version("1.0-12", md5="926d97dd7f8255a3a3d0b5765b902c00")

	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-renext", type=("build", "run"))
