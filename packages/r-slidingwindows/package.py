# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlidingwindows(RPackage):
	"""Methods for Time Series Analysis

	A collection of functions to perform Detrended Fluctuation Analysis (DFA exponent), GUEDES et al. (2019) <doi:10.1016/j.physa.2019.04.132> , Detrended cross-correlation coefficient (RHODCCA), GUEDES & ZEBENDE (2019) <doi:10.1016/j.physa.2019.121286>, DMCA cross-correlation coefficient and Detrended multiple cross-correlation coefficient (DMC), GUEDES & SILVA-FILHO & ZEBENDE (2018) <doi:10.1016/j.physa.2021.125990>, both with sliding windows approach. 
	"""
	
	homepage = "https://github.com/efguedes/SlidingWindows"
	cran = "SlidingWindows" 

	version("0.2.0", md5="063fea0fc18a1cadddfacfa0bda029b3")

	depends_on("r-dcca", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-nonlineartseries", type=("build", "run"))
	depends_on("r-tsentropies", type=("build", "run"))
