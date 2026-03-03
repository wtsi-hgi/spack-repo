# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHassaniSilva(RPackage):
	"""A Test for Comparing the Predictive Accuracy of Two Sets of
Forecasts

	A non-parametric test founded upon the principles of the Kolmogorov-Smirnov (KS) 
  test, referred to as the KS Predictive Accuracy (KSPA) test. The KSPA test is able to serve
  two distinct purposes. Initially, the test seeks to determine whether there exists a 
  statistically significant difference between the distribution of forecast errors, and 
  secondly it exploits the principles of stochastic dominance to determine whether the 
  forecasts with the lower error also reports a stochastically smaller error than forecasts 
  from a competing model, and thereby enables distinguishing between the predictive accuracy 
  of forecasts. KSPA test has been described in : Hassani and Silva (2015) <doi:10.3390/econometrics3030590>.
	"""
	
	cran = "Hassani.Silva" 

	version("1.0", md5="e5c4d9186910a3eae0ab0b39af284a6a")

