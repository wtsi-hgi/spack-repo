# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHassaniSacf(RPackage):
	"""Computing Lower Bound of Ljung-Box Test

	The Ljung-Box test is one of the most important tests for time series diagnostics and model selection. 
    The  Hassani SACF (Sum of the Sample Autocorrelation Function) Theorem , however, indicates that the sum of sample autocorrelation function is always fix for 
    any stationary time series with arbitrary length. This package confirms for sensitivity of the Ljung-Box test to 
    the number of lags involved in the test and therefore it should be used with extra caution.
    The Hassani SACF Theorem has been described in : Hassani, Yeganegi and M. R. (2019) <doi:10.1016/j.physa.2018.12.028>.
	"""
	
	cran = "Hassani.SACF" 

	version("2.0", md5="9a950236666732ad49556e2cbd8e9adb")

