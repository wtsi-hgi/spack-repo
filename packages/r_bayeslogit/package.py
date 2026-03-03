# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayeslogit(RPackage):
	"""PolyaGamma Sampling

	Tools for sampling from the PolyaGamma distribution based on Polson, Scott, and Windle (2013) <doi:10.1080/01621459.2013.829001>.  Useful for logistic regression.
	"""
	
	homepage = "https://github.com/jwindle/BayesLogit"
	cran = "BayesLogit" 

	version("2.1", md5="f5531669f5872e803438b72ea5dd06fc")

	depends_on("r@3.6:", type=("build", "run"))
