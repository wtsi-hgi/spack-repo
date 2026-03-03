# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmultinom(RPackage):
	"""One-Sided Multinomial Probabilities

	Implements multinomial CDF (P(N1<=n1, ..., Nk<=nk)) and tail probabilities (P(N1>n1, ..., Nk>nk)), as well as probabilities with both constraints (P(l1<N1<=u1, ..., lk<Nk<=uk)). Uses a method suggested by Bruce Levin (1981) <doi:10.1214/aos/1176345593>.
	"""
	
	cran = "pmultinom" 

	version("1.0.0", md5="eabce904c11113f94bf3955869aead11")

	depends_on("r-fftw", type=("build", "run"))
