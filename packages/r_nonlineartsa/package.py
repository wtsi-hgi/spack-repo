# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonlineartsa(RPackage):
	"""Nonlinear Time Series Analysis

	Function and data sets in the book entitled "Nonlinear Time Series Analysis with R Applications" B.Guris (2020). The book will be published in Turkish and the original name of this book will be "R Uygulamali Dogrusal Olmayan Zaman Serileri Analizi". It is possible to perform nonlinearity tests, nonlinear unit root tests, nonlinear cointegration tests and estimate nonlinear error correction models by using the functions written in this package. The Momentum Threshold Autoregressive (MTAR), the Smooth Threshold Autoregressive (STAR) and the Self Exciting Threshold Autoregressive (SETAR) type unit root tests can be performed using the functions written. In addition, cointegration tests using the Momentum Threshold Autoregressive (MTAR), the Smooth Threshold Autoregressive (STAR) and the Self Exciting Threshold Autoregressive (SETAR) models can be applied. It is possible to estimate nonlinear error correction models. The Granger causality test performed using nonlinear models can also be applied.
	"""
	
	cran = "NonlinearTSA" 

	version("0.5.0", md5="b3502d50beeca1668993f60ce071b2f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-tsdyn", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
