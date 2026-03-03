# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdtsa(RPackage):
	"""Time Series Analysis

	Analyzes autocorrelation and partial autocorrelation using surrogate methods and 
  bootstrapping, and computes the acceleration constants for the vectorized moving block 
  bootstrap provided by this package. It generates percentile, bias-corrected, and accelerated 
  intervals and estimates partial autocorrelations using Durbin-Levinson. This package 
  calculates the autocorrelation power spectrum, computes cross-correlations between two 
  time series, computes bandwidth for any time series, and performs autocorrelation frequency 
  analysis. It also calculates the periodicity of a time series.
	"""
	
	cran = "ADTSA" 

	version("1.0.1", md5="94a278426db310405e214929f498d35d")

