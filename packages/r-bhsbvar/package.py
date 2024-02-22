# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhsbvar(RPackage):
	"""Structural Bayesian Vector Autoregression Models

	Provides a function for estimating the parameters of Structural Bayesian Vector Autoregression models with the method developed by Baumeister and Hamilton (2015) <doi:10.3982/ECTA12356>, Baumeister and Hamilton (2017) <doi:10.3386/w24167>, and Baumeister and Hamilton (2018) <doi:10.1016/j.jmoneco.2018.06.005>. Functions for plotting impulse responses, historical decompositions, and posterior distributions of model parameters are also provided.
	"""
	
	cran = "BHSBVAR" 

	version("3.1.1", md5="87053552216b0413e4d0a471d75e3d23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
