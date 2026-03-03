# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayestree(RPackage):
	"""Bayesian Additive Regression Trees

	This is an implementation of BART:Bayesian Additive Regression Trees,
        by Chipman, George, McCulloch (2010).
	"""
	
	homepage = "https://www.r-project.org"
	cran = "BayesTree" 

	version("0.3-1.5", md5="c99c5e4a0ac531fd448c7ecb436765dc")

	depends_on("r-nnet", type=("build", "run"))
