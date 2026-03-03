# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCadence(RPackage):
	"""Conditional Density Estimation Network Construction and
Evaluation

	Parameters of a user-specified probability distribution are modelled by a multi-layer perceptron artificial neural network. This framework can be used to implement probabilistic nonlinear models including mixture density networks, heteroscedastic regression models, zero-inflated models, etc. following Cannon (2012) <doi:10.1016/j.cageo.2011.08.023>.
	"""
	
	cran = "CaDENCE" 

	version("1.2.5", md5="496da8dbcbc237e973c643a34c88598b")

	depends_on("r-pso", type=("build", "run"))
