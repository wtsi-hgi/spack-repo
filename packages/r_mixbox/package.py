# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixbox(RPackage):
	"""Observed Fisher Information Matrix for Finite Mixture Model

	Developed for the following tasks. 1- simulating realizations from the canonical, 
              restricted, and unrestricted finite mixture models. 2- Monte Carlo approximation for
              density function of the finite mixture models. 3- Monte Carlo approximation for the 
              observed Fisher information matrix, asymptotic standard error, and the corresponding  
              confidence intervals for parameters of the mixture models sing the method proposed by
              Basford et al. (1997) <https://espace.library.uq.edu.au/view/UQ:57525>.
	"""
	
	cran = "mixbox" 

	version("1.2.3", md5="a8fba7436ed7ae59a8a043e13e5c3eb2")
	version("1.2.2", md5="528ee97476f1d32c76d2e2d2fc2b4b77")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
