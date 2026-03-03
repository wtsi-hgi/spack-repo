# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarima(RPackage):
	"""Multivariate ARIMA and ARIMA-X Analysis

	Multivariate ARIMA and ARIMA-X estimation using Spliid's 
    algorithm (marima()) and simulation (marima.sim()).
	"""
	
	cran = "marima" 

	version("2.2", md5="d4ed509e53612f09c04da251444481b1")

