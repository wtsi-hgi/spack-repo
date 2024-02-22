# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynamicgp(RPackage):
	"""Modelling and Analysis of Dynamic Computer Experiments

	Emulating and solving inverse problems for dynamic computer experiments.
	     It contains two major functionalities: (1) localized GP model for large-scale
	     dynamic computer experiments using the algorithm proposed by
	     Zhang et al. (2018) <arXiv:1611.09488>; (2) solving inverse problems
	     in dynamic computer experiments. The current version only supports 64-bit
	     version of R.
	"""
	
	cran = "DynamicGP" 

	version("1.1-9", md5="76b85259f5b2a3fd4cc3e1e81925c392")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
