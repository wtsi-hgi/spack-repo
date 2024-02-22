# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHweintrinsic(RPackage):
	"""Objective Bayesian Testing for the Hardy-Weinberg Equilibrium
Problem

	General (multi-allelic) Hardy-Weinberg equilibrium problem from an objective Bayesian testing standpoint. This aim is achieved through the identification of a class of priors specifically designed for this testing problem. A class of intrinsic priors under the full model is considered. This class is indexed by a tuning quantity, the training sample size, as discussed in Consonni, Moreno and Venturini (2010). These priors are objective, satisfy Savage's continuity condition and have proved to behave extremely well for many statistical testing problems.
	"""
	
	homepage = "https://onlinelibrary.wiley.com/doi/10.1002/sim.4084/abstract"
	cran = "HWEintrinsic" 

	version("1.2.3", md5="0ed8625a2fcd9a7c4fca207070bc1a44")

