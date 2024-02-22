# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollocinfer(RPackage):
	"""Collocation Inference for Dynamic Systems

	These functions implement collocation-inference
    for continuous-time and discrete-time stochastic processes.
    They provide model-based smoothing, gradient-matching,
    generalized profiling and forwards prediction error methods.
	"""
	
	homepage = "http://www.bscb.cornell.edu/~hooker"
	cran = "CollocInfer" 

	version("1.0.4", md5="c4e809252e675107531585b3d321688c")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
