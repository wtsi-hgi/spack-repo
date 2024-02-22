# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFftwtools(RPackage):
	"""Wrapper for 'FFTW3' Includes: One-Dimensional Univariate,
	One-Dimensional Multivariate, and Two-Dimensional Transform.

	Provides a wrapper for several 'FFTW' functions. This package provides
	access to the two-dimensional 'FFT', the multivariate 'FFT', and the
	one-dimensional real to complex 'FFT' using the 'FFTW3' library. The
	package includes the functions fftw() and mvfftw() which are designed to
	mimic the functionality of the R functions fft() and mvfft().  The 'FFT'
	functions have a parameter that allows them to not return the redundant
	complex conjugate when the input is real data."""

	cran = "fftwtools"

	version("0.9-11", md5="00731a7e2b23d9f9cff0953b5aeae5f5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("fftw@3.1.2", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
