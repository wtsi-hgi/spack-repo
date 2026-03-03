# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgolay(RPackage):
	"""Efficient Savitzky-Golay Filtering

	Smoothing signals and computing their derivatives is a common
 requirement in signal processing workflows. Savitzky-Golay filters are a
 established method able to do both (Savitzky and Golay, 1964 <doi:10.1021/ac60214a047>).
 This package implements one dimensional Savitzky-Golay filters that can be applied to
 vectors and matrices (either row-wise or column-wise).
 Vectorization and memory allocations have been profiled to reduce computational
 fingerprint. Short filter lengths are implemented in the direct space, while
 longer filters are implemented in frequency space, using a Fast Fourier
 Transform (FFT).
	"""
	
	homepage = "https://github.com/zeehio/sgolay"
	cran = "sgolay" 

	version("1.0.3", md5="80abdde8d2fb8ed2a997cb8a0e9a4893")

	depends_on("r-signal", type=("build", "run"))
