# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmli(RPackage):
	"""Computationally Efficient Maximum Likelihood Identification of
Linear Dynamical Systems

	Provides implementations of computationally efficient maximum likelihood parameter estimation algorithms for models that represent linear dynamical systems. Currently, one such algorithm is implemented for the one-dimensional cumulative structural equation model with shock-error output measurement equation and assumptions of normality and independence. The corresponding scientific paper is yet to be published, therefore the relevant reference will be provided later.
	"""
	
	cran = "EMLI" 

	version("0.2.0", md5="eec8a65c49f159c98b6362b712db8aef")

