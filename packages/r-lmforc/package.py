# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmforc(RPackage):
	"""Linear Model Forecasting

	Introduces in-sample, out-of-sample, pseudo out-of-sample, and
    benchmark linear model forecast tests and a new class for working with 
    forecast data: Forecast.
	"""
	
	cran = "lmForc" 

	version("0.1.0", md5="fe88195dfe5647bf47d2a2932f1bc826")

	depends_on("r@3.6:", type=("build", "run"))
