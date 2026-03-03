# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStochqn(RPackage):
	"""Stochastic Limited Memory Quasi-Newton Optimizers

	Implementations of stochastic, limited-memory quasi-Newton optimizers,
	similar in spirit to the LBFGS (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) algorithm,
	for smooth stochastic optimization. Implements the following methods:
	oLBFGS (online LBFGS) (Schraudolph, N.N., Yu, J. and Guenter, S., 2007 <http://proceedings.mlr.press/v2/schraudolph07a.html>),
	SQN (stochastic quasi-Newton) (Byrd, R.H., Hansen, S.L., Nocedal, J. and Singer, Y., 2016 <arXiv:1401.7020>),
	adaQN (adaptive quasi-Newton) (Keskar, N.S., Berahas, A.S., 2016, <arXiv:1511.01169>).
	Provides functions for easily creating R objects
	with partial_fit/predict methods from some given objective/gradient/predict functions.
	Includes an example stochastic logistic regression using these optimizers.
	Provides header files and registered C routines for using it directly from C/C++.
	"""
	
	homepage = "https://github.com/david-cortes/stochQN"
	cran = "stochQN" 

	version("0.1.2-1", md5="d5c856ea63bc98275a6e4f2c7f11b448")

