# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGne(RPackage):
	"""Computation of Generalized Nash Equilibria

	Compute standard and generalized Nash Equilibria of non-cooperative games. 
 Optimization methods available are nonsmooth reformulation, fixed-point formulation, 
 minimization problem and constrained-equation reformulation. 
 See e.g. Kanzow and Facchinei (2010), <doi:10.1007/s10479-009-0653-x>. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/optimizer/"
	cran = "GNE" 

	version("0.99-5", md5="92c05372181a8a23c1098b1cd6ac642d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
