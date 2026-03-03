# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpseudomarg(RPackage):
	"""Constructs a Correlated Pseudo-Marginal Sampler

	The primary function makeCPMSampler() generates a sampler function which performs the correlated pseudo-marginal method of Deligiannidis, Doucet and Pitt (2017) <arXiv:1511.04992>. If the 'rho=' argument of makeCPMSampler() is set to 0, then the generated sampler function performs the original pseudo-marginal method of Andrieu and Roberts (2009) <DOI:10.1214/07-AOS574>. The sampler function is constructed with the user's choice of prior, parameter proposal distribution, and the likelihood approximation scheme. Note that this algorithm is not automatically tuned--each one of these arguments must be carefully chosen. 
	"""
	
	cran = "cPseudoMaRg" 

	version("1.0.1", md5="8f23198745e22918b8bfaf206572d7bd")

