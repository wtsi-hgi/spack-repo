# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecomposedpsf(RPackage):
	"""Time Series Prediction with PSF and Decomposition Methods (EMD
and EEMD)

	Predict future values with hybrid combinations of Pattern Sequence based
        Forecasting (PSF), Autoregressive Integrated Moving Average (ARIMA), Empirical Mode
        Decomposition (EMD) and Ensemble Empirical Mode Decomposition (EEMD) methods based
        hybrid methods.
	"""
	
	homepage = "https://www.neerajbokde.in/software/"
	cran = "decomposedPSF" 

	version("0.2", md5="332dde2158cd8341046ce570a46d36b2")

	depends_on("r-psf", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
