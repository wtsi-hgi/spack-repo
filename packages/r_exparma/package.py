# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExparma(RPackage):
	"""Fitting of Exponential Autoregressive Moving Average (EXPARMA)
Model

	The amplitude-dependent autoregressive time series model (EXPAR) proposed by Haggan and Ozaki (1981) <doi:10.2307/2335819> was improved by incorporating the moving average (MA) framework for capturing the variability efficiently. Parameters of the EXPARMA model can be estimated using this package. The user is provided with the best fitted EXPARMA model for the data set under consideration.
	"""
	
	cran = "EXPARMA" 

	version("0.1.0", md5="2c931777edd6d5f843eac1529d7a85d3")

	depends_on("r-forecast", type=("build", "run"))
