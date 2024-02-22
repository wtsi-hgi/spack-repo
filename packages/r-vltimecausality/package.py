# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVltimecausality(RPackage):
	"""Variable-Lag Time Series Causality Inference Framework

	A framework to infer causality on a pair of time series of real numbers based on variable-lag Granger causality and transfer entropy. Typically, Granger causality and transfer entropy have an assumption of a fixed and constant time delay between the cause and effect. However, for a non-stationary time series, this assumption is not true. For example, considering two time series of velocity of person A and person B where B follows A. At some time, B stops tying his shoes, then running to catch up A. The fixed-lag assumption is not true in this case. We propose a framework that allows variable-lags between cause and effect in Granger causality and transfer entropy to allow them to deal with variable-lag non-stationary time series. Please see Chainarong Amornbunchornvej, Elena Zheleva, and Tanya Berger-Wolf (2021) <doi:10.1145/3441452> when referring to this package in publications.  
	"""
	
	homepage = "https://github.com/DarkEyes/VLTimeSeriesCausality"
	cran = "VLTimeCausality" 

	version("0.1.4", md5="a538a94e5db520cb250a6aea7a6a7634")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-rtransferentropy", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
