# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegressionfactory(RPackage):
	"""Expander Functions for Generating Full Gradient and Hessian from
Single-Slot and Multi-Slot Base Distributions

	The expander functions rely on the mathematics developed for the Hessian-definiteness invariance theorem for linear projection transformations of variables, described in authors' paper, to generate the full, high-dimensional gradient and Hessian from the lower-dimensional derivative objects. This greatly relieves the computational burden of generating the regression-function derivatives, which in turn can be fed into any optimization routine that utilizes such derivatives. The theorem guarantees that Hessian definiteness is preserved, meaning that reasoning about this property can be performed in the low-dimensional space of the base distribution. This is often a much easier task than its equivalent in the full, high-dimensional space. Definiteness of Hessian can be useful in selecting optimization/sampling algorithms such as Newton-Raphson optimization or its sampling equivalent, the Stochastic Newton Sampler. Finally, in addition to being a computational tool, the regression expansion framework is of conceptual value by offering new opportunities to generate novel regression problems.
	"""
	
	cran = "RegressionFactory" 

	version("0.7.4", md5="848f1fb550fc72b402c49fe9644f0f55")

