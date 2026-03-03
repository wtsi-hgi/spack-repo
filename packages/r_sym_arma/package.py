# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymArma(RPackage):
	"""Autoregressive and Moving Average Symmetric Models

	Functions for fitting the Autoregressive and Moving Average Symmetric Model for univariate time series introduced by Maior and Cysneiros (2018), <doi:10.1007/s00362-016-0753-z>. Fitting method: conditional maximum likelihood estimation. For details see: Wei (2006), Time Series Analysis: Univariate and Multivariate Methods, Section 7.2.
	"""
	
	cran = "sym.arma" 

	version("1.0", md5="9ae1f65c6d5d27e465182f27f239a62d")

