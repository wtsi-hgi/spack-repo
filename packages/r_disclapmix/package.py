# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisclapmix(RPackage):
	"""Discrete Laplace Mixture Inference using the EM Algorithm

	Make inference in a mixture of discrete Laplace distributions using the EM algorithm. This can e.g. be used for modelling the distribution of Y chromosomal haplotypes as described in [1, 2] (refer to the URL section).
	"""
	
	homepage = "http://dx.doi.org/10.1016/j.jtbi.2013.03.009"
	cran = "disclapmix" 

	version("1.7.4", md5="d1f2cf8e643b727fc54055bda286d4b3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-disclap@1.4:", type=("build", "run"))
	depends_on("r-cluster@1.14.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
