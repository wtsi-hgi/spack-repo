# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbarts(RPackage):
	"""Discrete Bayesian Additive Regression Trees Sampler

	Fits Bayesian additive regression trees (BART; Chipman, George, and McCulloch (2010) <doi:10.1214/09-AOAS285>) while allowing the updating of predictors or response so that BART can be incorporated as a conditional model in a Gibbs/Metropolis-Hastings sampler. Also serves as a drop-in replacement for package 'BayesTree'.
	"""
	
	homepage = "https://github.com/vdorie/dbarts"
	cran = "dbarts" 

	version("0.9-26", md5="abc708a8a35c1b56c4d08fe126adb431")

	depends_on("r@3.1.0:", type=("build", "run"))
