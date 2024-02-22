# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutostsm(RPackage):
	"""Automatic Structural Time Series Models

	Automatic model selection for structural time series decomposition into trend, cycle, and seasonal components, plus optionality for structural interpolation, using the Kalman filter. 
  Koopman, Siem Jan and Marius Ooms (2012) "Forecasting Economic Time Series Using Unobserved Components Time Series Models" <doi:10.1093/oxfordhb/9780195398649.013.0006>.
  Kim, Chang-Jin and Charles R. Nelson (1999) "State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications" <doi:10.7551/mitpress/6444.001.0001><http://econ.korea.ac.kr/~cjkim/>. 
	"""
	
	cran = "autostsm" 

	version("3.1.3", md5="c0cb2ff90d1a0908df0fa7b2ac90558a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maxlik@1.5.2:", type=("build", "run"))
	depends_on("r-forecast@8.15:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-strucchange@1.5:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-dosnow@1.0.19:", type=("build", "run"))
	depends_on("r-lmtest@0.9.38:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-sandwich@3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-kalmanfilter@2.0.1:", type=("build", "run"))
