# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSams(RPackage):
	"""Merge-Split Samplers for Conjugate Bayesian Nonparametric Models

	Markov chain Monte Carlo samplers for posterior simulations of conjugate Bayesian nonparametric
    mixture models. Functionality is provided for Gibbs sampling as in Algorithm 3 of Neal (2000)
    <DOI:10.1080/10618600.2000.10474879>, restricted Gibbs merge-split sampling as described in Jain & Neal
    (2004) <DOI:10.1198/1061860043001>, and sequentially-allocated merge-split sampling <DOI:10.1080/00949655.2021.1998502>, as well as
    summary and utility functions.
	"""
	
	cran = "sams" 

	version("0.4.3", md5="883c7df3ed4b344d2ee353d010b1de88")

	depends_on("r@3.5:", type=("build", "run"))
