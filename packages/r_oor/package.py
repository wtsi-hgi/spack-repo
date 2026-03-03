# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROor(RPackage):
	"""Optimistic Optimization in R

	Implementation of optimistic optimization methods for global optimization of deterministic or stochastic functions. The algorithms feature guarantees of the convergence to a global optimum. They require minimal assumptions on the (only local) smoothness, where the smoothness parameter does not need to be known. They are expected to be useful for the most difficult functions when we have no information on smoothness and the gradients are unknown or do not exist. Due to the weak assumptions, however, they can be mostly effective only in small dimensions, for example, for hyperparameter tuning.
	"""
	
	homepage = "https://github.com/mbinois/OOR"
	cran = "OOR" 

	version("0.1.4", md5="25ca11c4f0e413f082aff129634af178")

