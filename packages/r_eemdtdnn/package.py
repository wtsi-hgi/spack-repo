# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REemdtdnn(RPackage):
	"""EEMD and Its Variant Based Time Delay Neural Network Model

	Forecasting univariate time series with different decomposition based time delay neural network models. For method details see Yu L, Wang S, Lai KK (2008). <doi:10.1016/j.eneco.2008.05.003>. 
	"""
	
	cran = "eemdTDNN" 

	version("0.1.0", md5="6420d32ecfeb61aba1707ca599499f16")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))
