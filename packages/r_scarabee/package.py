# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScarabee(RPackage):
	"""Optimization Toolkit for Pharmacokinetic-Pharmacodynamic Models

	A port of the Scarabee toolkit originally written as a 
  Matlab-based application. scaRabee provides a framework for simulation and optimization 
  of pharmacokinetic-pharmacodynamic models at the individual and population level.
  It is built on top of the neldermead package, which provides the direct search 
  algorithm proposed by Nelder and Mead for model optimization.
	"""
	
	cran = "scaRabee" 

	version("1.1-4", md5="7a366a49e7ef70658e422354215057ed")

	depends_on("r-neldermead@1.0.8:", type=("build", "run"))
	depends_on("r-optimsimplex@1.0.5:", type=("build", "run"))
	depends_on("r-optimbase@1.0.8:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
