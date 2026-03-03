# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupergauss(RPackage):
	"""Superfast Likelihood Inference for Stationary Gaussian Time
Series

	Likelihood evaluations for stationary Gaussian time series are typically obtained via the Durbin-Levinson algorithm, which scales as O(n^2) in the number of time series observations.  This package provides a "superfast" O(n log^2 n) algorithm written in C++, crossing over with Durbin-Levinson around n = 300.  Efficient implementations of the score and Hessian functions are also provided, leading to superfast versions of inference algorithms such as Newton-Raphson and Hamiltonian Monte Carlo.  The C++ code provides a Toeplitz matrix class packaged as a header-only library, to simplify low-level usage in other packages and outside of R.
	"""
	
	cran = "SuperGauss" 

	version("2.0.3", md5="ce5fd79b062c0e0197d1d1fb90dd988f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("fftw@3.1.2:", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
