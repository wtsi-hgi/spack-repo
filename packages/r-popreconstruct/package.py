# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopreconstruct(RPackage):
	"""Reconstruct Human Populations of the Recent Past

	Implements the Bayesian hierarchical model described by Wheldon, Raftery, Clark and Gerland (see: <doi:10.1080/01621459.2012.737729>) for simultaneously estimating age-specific population counts, fertility rates, mortality rates and net international migration flows, at the national level.
	"""
	
	cran = "popReconstruct" 

	version("1.0-6", md5="a8f9922d6976545e3b0db6193d558c65")

	depends_on("r-coda", type=("build", "run"))
