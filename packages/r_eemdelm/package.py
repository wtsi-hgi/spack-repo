# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REemdelm(RPackage):
	"""Ensemble Empirical Mode Decomposition and Its Variant Based ELM
Model

	Forecasting univariate time series with different decomposition based Extreme Learning Machine models. For method details see Yu L, Wang S, Lai KK (2008). <doi:10.1016/j.eneco.2008.05.003>, Parida M, Behera MK, Nayak N (2018). <doi:10.1109/ICSESP.2018.8376723>. 
	"""
	
	cran = "EEMDelm" 

	version("0.1.1", md5="85a3e496654e300014574e257f1525ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))
