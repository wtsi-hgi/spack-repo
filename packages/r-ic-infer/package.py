# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcInfer(RPackage):
	"""Inequality Constrained Inference in Linear Normal Situations

	Implements inequality constrained inference. This includes parameter estimation in normal (linear) models under linear equality and inequality constraints, as well as normal likelihood ratio tests involving inequality-constrained hypotheses. For inequality-constrained linear models, averaging over R-squared for different orderings of regressors is also included.
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/"
	cran = "ic.infer" 

	version("1.1-7", md5="3d6f12f4f7469ea839b1d3e4cb92570f")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-kappalab", type=("build", "run"))
