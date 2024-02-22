# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmix(RPackage):
	"""Bayesian Inference on Univariate Normal Mixtures

	A program for Bayesian analysis of univariate normal mixtures with an unknown number
  of components, following the approach of Richardson and Green (1997) <doi:10.1111/1467-9868.00095>.
  This makes use of reversible jump Markov chain Monte Carlo methods that are capable of jumping
  between the parameter sub-spaces corresponding to different numbers of components in the mixture.
  A sample from the full joint distribution of all unknown variables is thereby generated,
  and this can be used as a basis for a thorough presentation of many aspects of the posterior
  distribution. 
	"""
	
	cran = "Nmix" 

	version("2.0.5", md5="9db4635ef69cde350f9d6b18d8b07aeb")

