# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcbd(RPackage):
	"""'GPU'/CPU Benchmarking in Debian-Based Systems

	'GPU'/CPU Benchmarking on Debian-package based systems
 This package benchmarks performance of a few standard linear algebra
 operations (such as a matrix product and QR, SVD and LU decompositions)
 across a number of different 'BLAS' libraries as well as a 'GPU' implementation.
 To do so, it takes advantage of the ability to 'plug and play' different
 'BLAS' implementations easily on a Debian and/or Ubuntu system.  The current
 version supports
  - 'Reference BLAS' ('refblas') which are un-accelerated as a baseline
  - Atlas which are tuned but typically configure single-threaded
  - Atlas39 which are tuned and configured for multi-threaded mode
  - 'Goto Blas' which are accelerated and multi-threaded
  - 'Intel MKL' which is a commercial accelerated and multithreaded version.
 As for 'GPU' computing, we use the CRAN package
  - 'gputools'
 For 'Goto Blas', the 'gotoblas2-helper' script from the ISM in Tokyo can be
 used. For 'Intel MKL' we use the Revolution R packages from Ubuntu 9.10.
	"""
	
	cran = "gcbd" 

	version("0.2.6", md5="ddf8394c2d7b5f3c4edc61b5e467e984")

	depends_on("r@2.11.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("cuda", type=("build", "link", "run"))
