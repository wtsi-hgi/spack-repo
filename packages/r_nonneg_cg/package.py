# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonnegCg(RPackage):
	"""Non-Negative Conjugate-Gradient Minimizer

	Minimize a differentiable function subject to all the variables being non-negative (i.e. >= 0),
  using a Conjugate-Gradient algorithm based on a modified Polak-Ribiere-Polyak formula as described in
  (Li, Can, 2013, <https://www.hindawi.com/journals/jam/2013/986317/abs/>).
	"""
	
	homepage = "https://github.com/david-cortes/nonneg_cg"
	cran = "nonneg.cg" 

	version("0.1.6-1", md5="df15344bb3daf6b85058ce9515b5bee3")

	depends_on("r-rcpp", type=("build", "run"))
