# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredtoolsts(RPackage):
	"""Time Series Prediction Tools

	Makes the time series prediction easier by automatizing this process
  using four main functions: prep(), modl(), pred() and postp(). Features different
  preprocessing methods to homogenize variance and to remove trend and seasonality.
  Also has the potential to bring together different predictive models to make comparatives.
  Features ARIMA and Data Mining Regression models (using caret).
	"""
	
	homepage = "https://github.com/avm00016/predtoolsTS"
	cran = "predtoolsTS" 

	version("0.1.1", md5="c4f7db36d4131ed90829eee1aef36f61")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-tspred", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
