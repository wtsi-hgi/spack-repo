# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbmsdp(RPackage):
	"""Semidefinite Programming for Fitting Block Models of Equal Block
Sizes

	An ADMM implementation of SDP-1, a semidefinite programming relaxation of the maximum likelihood estimator for fitting a block model. SDP-1 has a tendency to produce equal-sized blocks and is ideal for producing a form of network histogram approximating a nonparametric graphon model. Alternatively, it can be used for community detection. (This is experimental code, proceed with caution.)
	"""
	
	cran = "sbmSDP" 

	version("0.2", md5="e92fdfee71ba0bbb2391770397a9299a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
