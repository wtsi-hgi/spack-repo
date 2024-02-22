# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgroups(RPackage):
	"""Pedigree and Genetic Groups

	Calculates additive and dominance genetic relationship matrices and their inverses, in matrix and tabular-sparse formats. It includes functions for checking and processing pedigree, calculating inbreeding coefficients (Meuwissen & Luo, 1992 <doi:10.1186/1297-9686-24-4-305>), as well as functions to calculate the matrix of genetic group contributions (Q), and adding those contributions to the genetic merit of animals (Quaas (1988) <doi:10.3168/jds.S0022-0302(88)79691-5>). Calculation of Q is computationally extensive. There are computationally optimized functions to calculate Q.
	"""
	
	homepage = "https://github.com/nilforooshan/ggroups"
	cran = "ggroups" 

	version("2.1.2", md5="13efc20eff4900f8e5328b34780e7979")

